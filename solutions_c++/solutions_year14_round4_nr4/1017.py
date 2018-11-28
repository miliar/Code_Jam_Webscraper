//Program: d
//Author: gary
//Date: 31/05/2014
#include <bits/stdc++.h>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef pair<int, int> i2;
typedef long long ll;
const int INF = 1e9;
const int MAX_N = 10;

struct node {
  node(){for(int i=0;i<26;i++)ch[i]=NULL;}
  node* ch[26];
};

struct trie {
  int nodes;
  node* root;
  trie(){
    nodes = 0;
    root = createnode();
  }

  node* createnode(){
    nodes ++;
    return new node();
  }

  void add(string s){
    node* cur = root;
    int i = 0, n = SZ(s);
    while(i < n){
      int j = s[i] - 'A';
      if(cur->ch[j] == NULL){
	cur->ch[j] = createnode();
      }
      cur = cur->ch[j];
      i++;
    }
  }
  void del(node* n){
    for(int i = 0; i < 26; i++)
      if(n->ch[i] != NULL){
	del(n->ch[i]);
	delete(n->ch[i]);
      }
  }
};

int T, N, M;
string S[MAX_N];
int A[MAX_N];
int X, Y;

int calc(){
  int res = 0;
  for(int i = 0; i < N; i++){
    trie t;
    // todo: check all non empty?
    for(int j = 0; j < M; j++){
      if(A[j] == i){
	t.add(S[j]);
      }
    }
    res += t.nodes;
    t.del(t.root);
  }
  return res;
}

int flag[MAX_N];

void rec(int i){
  if(i == M){
    memset(flag, 0, sizeof flag);
    for(int j = 0; j < M; j++)
      flag[A[j]]++;
    for(int j = 0; j < N; j++)
      if(flag[j] == 0)
	return;

    int r = calc();
    if(r > X){
      X = r;
      Y = 0;
    }
    if(r == X)
      Y ++;
  } else {
    for(int j = 0; j < N; j++){
      A[i] = j;
      rec(i + 1);
    }
  }
}

int main(){
  ios::sync_with_stdio(0);
  cin >> T;
  for(int caseNo = 1; caseNo <= T; caseNo++){
    cout << "Case #" << caseNo << ": ";
    cin >> M >> N;
    for(int i = 0; i < M; i++)
      cin >> S[i];
    X = Y = 0;
    rec(0);
    cout << X << " " << Y << endl;
  }
  return 0;
}
