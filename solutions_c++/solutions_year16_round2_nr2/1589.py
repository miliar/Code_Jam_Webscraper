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

string I1, I2; 
vector<string> S1, S2; 
void gen(int i, string S, int tp) {
  if(i == SZ(S)) {
    if(tp == 1) S1.pb(S); 
    else S2.pb(S); 
    return; 
  }

  if(S[i] != '?') { 
    gen(i + 1, S, tp); 
    return; 
  }
  for(char j = '0'; j <= '9'; ++j) {
    S[i] = j; 
    gen(i + 1, S, tp); 
  }
}
void solve() {
  int t; scanf("%d", &t); 
  for(int cs = 1; cs <= t; ++cs) {
    cin >> I1 >> I2; 
    printf("Case #%d: ", cs); 
    S1.clear(); S2.clear(); 
    gen(0, I1, 1); 
    gen(0, I2, 2); 
    pair<int, int> ans(10101, 10101); 
    pair<string, string> anss; 
    int dif = 10101; 
    for(int i = 0; i < SZ(S1); ++i) {
      for(int j = 0; j < SZ(S2); ++j) {
        int a = atoi(S1[i].c_str()); 
        int b = atoi(S2[j].c_str()); 
        if(abs(a - b) < dif) {
          dif = abs(a - b); 
          anss = mp(S1[i], S2[j]); 
          ans = mp(a, b); 
        }else if(abs(a - b) == dif) {
          if(a < ans.fr) ans = mp(a, b), anss = mp(S1[i], S2[j]); 
        }
      }
    }
    printf("%s %s\n", anss.fr.c_str(), anss.sc.c_str()); 
  }
}
int main() {
#ifndef ONLINE_JUDGE 
  freopen("in.txt", "r", stdin); 
  freopen("out.txt", "w", stdout); 
#endif
  solve(); 
}