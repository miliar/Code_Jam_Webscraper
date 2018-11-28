#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

bool is_prime(ll n) {
  for(ll i=2;i<=sqrt(n);i++) if(n%i == 0) return false;
  return true;
}

ll power(ll a,ll b) {
  ll res = 1;
  while(b) {
    if(b&1) res = res*a;
    a = a*a;
    b >>= 1;
  }
  return res;
}

bool ok(string s) {
  int L = s.length();
  int cnt = 0;
  for(int i=2;i<=10;i++) {
    ll S = 0;
    for(int j=0;j<L;j++) {
       if(s[j] == '1') S += power(i,j);
    }
    if(!is_prime(S)) cnt++;
  }
  if(cnt == 9) return true;
  return false;
}

ll divisor(ll n) {
  for(ll i=2;i<=sqrt(n);i++) {
    if(n%i == 0) return i;
  }
}

void solve(string s) {
  int L = s.length();
  for(int i=2;i<=10;i++) {
    ll S = 0;
    for(int j=0;j<L;j++) {
       if(s[j] == '1') S += power(i,j);
    }
    cout << divisor(S) << " ";
  }
}

void ulti(string s) {
  for(int i=s.length()-1;i>=0;i--) cout << s[i];
  cout << " ";
}

int main() {
  freopen("C-small-attempt0.in","r",stdin);
  freopen("ans.txt","w",stdout);
  int TC,N,J,CNT;
  cin >> TC;
  for(int cas=1;cas<=TC;cas++) {
    printf("Case #%d:\n",cas);
    cin >> N >> J;
    CNT = 0;
    for(int i=0;i<(1<<N);i++) {
        string s = "";
        for(int j=0;j<N;j++) {
            if(i & (1<<j)) s += '1';
            else s += '0';
        }
        if(s[0] == '1' && s[N-1] == '1') {
            if(ok(s)) {
              ulti(s);
              solve(s);
              CNT++;
              cout << endl;
              if(CNT == J) break;
            }
        }
    }
  }
  return 0;
}
