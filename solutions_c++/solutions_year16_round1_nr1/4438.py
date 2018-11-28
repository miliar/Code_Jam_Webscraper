/*
          ______      
||  //   | _____|   ||  //
|| //    ||         || //
||//     ||_____    ||//
||\\     | _____|   ||\\
|| \\    ||         || \\   ll Once(ll KEK){
||  \\   ||_____    ||  \\ 		return Forever(KEK);
||   \\  |______|   ||   \\ }
                     
*/
#include<bits/stdc++.h>

using namespace std;
const int N6 = 1e6 + 6, N3 = 1e3 + 6, oo =  1e9 + 9, base = 1e9 + 7;
const long long ool = 1e18 + 9;

typedef unsigned long long ull;
typedef long long ll;
typedef double ld;
typedef pair <int, int> PII;
typedef pair <ll, ll> PLL;

#define F first
#define S second
#define pb push_back
#define right(x) x << 1 | 1
#define left(x) x << 1	
#define	forn(x, a, b) for (int x = a; x <= b; ++x)
#define for1(x, a, b) for (int x = a; x >= b; --x)
#define mp make_pair

int main(){
	ios_base :: sync_with_stdio(0);
	cin.tie(0);	
	
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);

	int t;
	cin >> t;
	forn(test, 1, t){
		string s;
		cin >> s;
		int n = s.size();

		int mx = s[0] - 'A';
		string ans = "";
		ans += s[0];

		forn(i, 1, n - 1){
			if(s[i] - 'A' >= mx){
				mx = s[i] - 'A';
				ans = s[i] + ans;
			}
			else
				ans += s[i];
		}

		cout << "Case #" << test << ": " << ans << "\n";
	}
		
	return 0;
}