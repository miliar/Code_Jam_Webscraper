//Program: c
//Author: gary
//Date: 30/05/2015
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define dbg(x) cerr << #x << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef pair<int, int> pii;
// const int INF = 1e9;
const int MAX_N = 10000;

int T;
int N;
vector<int> F[MAX_N];

map<string, int> _id;
int B[MAX_N][2];

int getid(string s){
  auto it = _id.find(s);
  int ans = 0;
  if(it == _id.end()){
    ans = SZ(_id);
    _id[s] = ans;
  } else {
    ans = it->se;
  }
  return ans;
}

char sentence[10000000];
int solve(){
  scanf("%d\n", &N);
  _id = map<string, int>();
  for(int i = 0; i < N; i++){
    string word;
    gets(sentence);
    // cout << sentence << endl;
    stringstream ss(sentence);
    F[i].clear();
    while(ss >> word){
      F[i].push_back(getid(word));
    }
  }
  int res = 1111111111;
  for(int mask = 0; mask < (1 << (N - 2)); mask++){
    int nmask = (mask << 2) | 2;
    for(int j = 0; j < SZ(_id); j++)
      B[j][0] = B[j][1] = 0;
    for(int j = 0; j < N; j++){
      for(int v: F[j]){
        B[v][(nmask >> j) & 1] = 1;
      }
    }
    int r = 0;
    for(int j = 0; j < SZ(_id); j++){
      r += (B[j][0] && B[j][1]);
    }
    res = min(res, r);
  }
  return res;
}


int main(){
  scanf("%d", &T);
  for(int tc = 1; tc <= T; tc++){
    printf("Case #%d: %d\n", tc, solve());
  }
  return 0;
}
