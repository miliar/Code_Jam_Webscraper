#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <functional>
#include <complex>
#include <iomanip>

using namespace std;

typedef long long ll;


int nodes;

struct Trie{
  map<char, Trie*> cs;

  ~Trie(){
    for(map<char, Trie*>::iterator iter = cs.begin(); iter != cs.end(); ++iter)
      delete iter->second;
    cs.clear();
  }
};

Trie* trie_add(Trie* t, const string &key, int offset = 0){
  if(t->cs.find(key[offset]) == t->cs.end()){
    ++nodes;
    t->cs[key[offset]] = new Trie();
  }
  if(offset+1 < key.size())
    return trie_add(t->cs[key[offset]], key, offset+1);
  return t->cs[key[offset]];
}

Trie* trie_find(Trie *t, const string &key, int offset = 0){
  if(t->cs.find(key[offset]) == t->cs.end())
    return NULL;
  if(offset+1 < key.size())
    return trie_find(t->cs[key[offset]], key, offset+1);
  return t->cs[key[offset]];
}



int M, N;

string s[1000];
Trie* t[100];
int assign[1000];
int have[100];
int maxAns, maxCnt;

void calc(void){
  nodes = N;
  for(int i = 0; i < M; ++i){
    trie_add(t[assign[i]], s[i]);
  }

  if(maxAns < nodes){
    maxAns = nodes;
    maxCnt = 1;
  }
  else if(maxAns == nodes){
    ++maxCnt;
  }
}

void recur(int depth){
  if(depth == M){
    bool ok = true;
    for(int i = 0; i < N; ++i){
      t[i] = new Trie();
      ok &= have[i] > 0;
    }
    if(ok)
      calc();
    for(int i = 0; i < N; ++i)
      delete t[i];
    return;
  }

  for(int i = 0; i < N; ++i){
    assign[depth] = i;
    ++have[i];
    recur(depth+1);
    --have[i];
  }
}

int main(void){
  int T;
  cin >> T;
  for(int tt = 0; tt < T; ++ tt){
    cin >> M >> N;
    for(int i = 0 ; i < M; ++i)
      cin >> s[i];

    fill_n(have, N, 0);
    maxAns = maxCnt = 0;
    recur(0);

    cout << "Case #" << tt+1 << ": " << maxAns << " " << maxCnt << endl;
  }

  return 0;
}
