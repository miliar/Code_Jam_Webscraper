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

int n;
bool u[11];

int main(){
	ios_base :: sync_with_stdio(0);
	cin.tie(0);	

	#ifdef KEK
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif

	int t;
	cin >> t;
	forn(test, 1, t){
		cin >> n;
		memset(u, 0, sizeof u);
		bool ok = 0;
		int x = n;
		if(!n){
			cout << "Case #" << test << ": INSOMNIA\n";
			continue;
		}
		while(!ok){
			int q = x;
			while(q){
				u[q % 10] = 1;
				q /= 10;	
			}
			ok = 1;
			forn(i, 0, 9){
				if(!u[i])
					ok = 0;
			}
			x += n;
		}	
		cout << "Case #" << test << ": " << x - n << "\n";
	}
	
	return 0;
}