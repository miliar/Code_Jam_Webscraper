//Program: a
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
const int MAX_N = 1e4 + 10;

int T;
int X, N;
int S[MAX_N];

int solve(){
  cin >> N >> X;
  for(int i = 0; i < N; i++)
    cin >> S[i];
  sort(S, S + N);
  int i = 0, j = N - 1;
  int M = 0;
  while(i < N){
    while(j > i && S[i] + S[j] > X){
      j --;
    }
    if(i < j)
      M ++;
    i ++, j --;
  }
  return N - M;
}

int main(){
  ios::sync_with_stdio(0);
  cin >> T;
  for(int caseNo = 1; caseNo <= T; caseNo++){
    cout << "Case #" << caseNo << ": " << solve() << endl;
  }
  return 0;
}
