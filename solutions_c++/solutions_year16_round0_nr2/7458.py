#include "bits/stdc++.h"
#define _CRT_SECURE_NO_WARNINGS
#define rep(i,n) for(int i = 0;i < n;i++)
#define REP(i,n,k) for(int i = n;i < k;i++)
#define P(p) cout << (p) << endl;
#define sP(p) cout << setprecision(15) << fixed << p << endl;
#define Pi pair<int,int>
#define IINF 1e9
#define LINF 1e18
#define vi vector<int>
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
int dx[] = { 0, 1 };
int dy[] = { 1, 0 };

unsigned long long sttoi(std::string str) {
	unsigned long long ret;
	std::stringstream ss; ss << str;
	ss >> ret;
	return ret;
}

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

ull gcd(ull a, ull b) {
	if (b > a)swap(a, b);
	if (b == 0) return a;
	return gcd(b, a%b);
}

int comb(int n, int k) {
	int ans = 1;
	for (int i = 0; i < min(k, n - k); i++) {
		ans *= n - i;
		ans /= i + 1;
	}
	return ans;
}

int check(map<int,int> m) {
	int ret = 1;
	rep(i, 10) {
		ret *= m[i];
	}
	return ret;
}

void solve() {
  int n;
  cin >> n;
  rep(i,n){
    int cnt = 0;
    string s;
    cin >> s;
    int pos = 0;
    if(s[0] == '-'){
      while(s[pos] == '-'){
        pos++;
      }
      cnt++;
    }
    REP(j,pos,s.length()){
      if(s[j] == '-'){
        int len = 0;
        while(s[j] == '-'){
          len++;
          j++;
        }
        cnt+=2;
      }
    }
    cout << "Case #" << i+1 << ": " << cnt << endl;
  }
}

int main() {
	solve();
	return 0;
}