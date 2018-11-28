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

bool a[111];

int get(int pos, int x){
	if(!pos)
		return 0;
	if(a[pos] == (x ^ 1))
		return get(pos - 1, x ^ 1) + 1;
	else
		return get(pos - 1, x);
}

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
		string s;
		cin >> s;
		int n = s.size();
		memset(a, 0, sizeof a);
		forn(i, 0, n - 1){
			a[i + 1] = (s[i] == '+' ? 1 : 0);
		}

		cout << "Case #" << test << ": " << get(n, 1) << "\n";
	}
	
	return 0;
}