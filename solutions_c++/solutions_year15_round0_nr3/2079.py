#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
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
const int MAX_N = 10010;

char S[MAX_N];

int F[MAX_N];
int L, X;

int A[4][4] = {
  {1, 2, 3, 4},
  {2, -1, 4, -3},
  {3, -4, -1, 2},
  {4, 3, -2, -1}
};

int signum(int i){
  return i > 0 ? 1 : -1;
}

int magic(int i, int j){
  return signum(i) * signum(j) * A[abs(i) - 1][abs(j) - 1];
}

int translate(char c){
  if(c == 'i') return 2;
  if(c == 'j') return 3;
  if(c == 'k') return 4;
}

int inv(int x){
  if(abs(x) == 1)
    return x;
  return -x;
}

bool solve(){
  scanf("%d%d%s", &L, &X, S);
  
  for(int i = 0; i < L; i++)
    for(int j = 1; j < X; j++)
      S[j * L + i] = S[i];

  // printf("%s\n", S);
  
  L *= X;
  
  F[0] = 1;
  for(int i = 1; i <= L; i++){
    F[i] = magic(F[i - 1], translate(S[i - 1]));
  }

  set<int> s, t;
  for(int i = 1; i < L; i++){
    if(s.find(magic(3, inv(F[i]))) != s.end()) t.insert(inv(F[i]));
    if(F[i] == 2) s.insert(inv(F[i]));
  }

  return t.find(magic(4, inv(F[L]))) != t.end();
}

int main(){
  int T;
  scanf("%d", &T);
  for(int tc = 1; tc <= T; tc++){
    printf("Case #%d: %s\n", tc, solve() ? "YES" : "NO");
  }
  return 0;
}
