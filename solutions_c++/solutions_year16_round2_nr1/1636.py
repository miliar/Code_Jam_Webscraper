// make it funny! :D 

#include <bits/stdc++.h> 
using namespace std; 

#define fr first 
#define sc second 
#define mp make_pair 
#define SZ(A) int(A.size())
#define LN(A) strlen(A)
#define All(A) A.begin(), A.end()
#define rAll(A) A.rbegin(), A.rend()
#define pb push_back 
typedef long long ll; 
typedef pair<ll, ll> ii; 
typedef vector<int> vi; 

vi getTheFuckYouCanGet(vector<int> A) {
  vi N; 
  if(A['Z' - 'A']) {
    int mn = A['Z' - 'A']; 
    for(int i = 0; i < A['Z' - 'A']; ++i) N.pb(0); 
    string X = "ZERO"; 
    for(int i = 0; i < SZ(X); ++i) {
      int idx = X[i] - 'A'; 
      A[idx] -= mn; 
    }
  }

  if(A['X' - 'A']) {
    int mn = A['X' - 'A'];
    for(int i = 0; i < A['X' - 'A']; i++) N.pb(6); 
    string Z = "SIX"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }

  if(A['G' - 'A']) {
    int mn = A['G' - 'A'];
    for(int i = 0; i < A['G' - 'A']; i++) N.pb(8); 
    string Z = "EIGHT"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  if(A['W' - 'A']) {
    int mn = A['W' - 'A'];
    for(int i = 0; i < A['W' - 'A']; i++) N.pb(2); 
    string Z = "TWO"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  if(A['T' - 'A']) {
    int mn = A['T' - 'A'];
    for(int i = 0; i < A['T' - 'A']; i++) N.pb(3); 
    string Z = "THREE"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  if(A['U' - 'A']) {
    int mn = A['U' - 'A'];
    for(int i = 0; i < A['U' - 'A']; i++) N.pb(4); 
    string Z = "FOUR"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  if(A['O' - 'A']) {
    int mn = A['O' - 'A'];
    for(int i = 0; i < A['O' - 'A']; i++) N.pb(1); 
    string Z = "ONE"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  if(A['F' - 'A']) {
    int mn = A['F' - 'A'];
    for(int i = 0; i < A['F' - 'A']; i++) N.pb(5); 
    string Z = "FIVE"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  if(A['S' - 'A']) {
    int mn = A['S' - 'A'];
    for(int i = 0; i < A['S' - 'A']; i++) N.pb(7); 
    string Z = "SEVEN"; 
    for(int i = 0; i < SZ(Z); ++i) {
      A[Z[i] - 'A'] -= mn; 
    }
  }
  int mn = 100000; 
  string s = "NINE"; 
  for(int i = 0; i < 4; i++) mn = min(mn, A[s[i] - 'A']); 
  while(mn--) N.pb(9); 
  return N; 
}
char I[2010]; 
void solve() {
  int t; scanf("%d", &t); 
  for(int cs = 1; cs <= t; ++cs) {
    printf("Case #%d: ", cs); 
    scanf("%s", I); 
    int ln = LN(I); 
    vector<int> A(26, 0); 
    for(int i = 0; i < ln; ++i) A[I[i] - 'A']++; 
    vector<int> ans = getTheFuckYouCanGet(A); 
    sort(All(ans)); 
    for(int i: ans) cout << i; 
    cout << "\n"; 
  }
}
int main() {
#ifndef ONLINE_JUDGE 
  freopen("in.txt", "r", stdin); 
  freopen("out.txt", "w", stdout); 
#endif
  solve(); 
}