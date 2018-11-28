
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
typedef std::pair<double, double> pdd;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(int i = 0; i<(int)N; i++)
#define fornj(N)         for(int j = 0; j<(int)N; j++)
#define fornk(N)         for(int k = 0; k<(int)N; k++)
#define forn1(N)          for(int i = 1; i<=(int)N; i++)
#define fornj1(N)         for(int j = 1; j<=(int)N; j++)
#define fornk1(N)         for(int k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define v vector
#define File "Patterns"
#define ll long long
#define print(n) printf("%d ", (n));
#define printll(n) printf("%I64d", (n));
#define printline() printf("\n");
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
#define x first
#define y second
#define double long double
using namespace std;

v<v<bool> >ans;
v<v<int>>ans2;
v<int>ansdef;
bool check_div(v<bool>a, int base, int mod) {
	int nnow = 0;
	forn(a.size()) {
		nnow *= base;
		nnow += a[i];
		nnow %= mod;

	}
	if (nnow != 0)
		return 0;
	else return 1;

}
void generate(int len, int amount) {
	v<bool>def;
	forn(len)def.push_back(0);
	
	def[0] = def.back() = 1;
	def[2] = def[4] = 1;



	for (int i1 = 1; i1 < len - 1; i1+=2)
		for(int i2 = i1+2; i2 < len - 1; i2 += 2)
			for (int i3 = i2+2; i3 < len - 1; i3 += 2)
				for (int i4 = i3+2; i4 < len - 1; i4 += 2)
					for (int i5 = i4+2; i5 < len - 1; i5 += 2) 
						for (int i6 = i5+2; i6 < len - 1; i6 += 2) 
							for (int i7 = i6+2; i7 < len - 1; i7 += 2) 
								for (int i8 = i7+2; i8 < len - 1; i8 += 2) {
					if (ans.size() == amount)return;
					v<bool>now = def;
					now[i1] = now[i2] = now[i3] = now[i4] = now[i5] = now[i6] = now[i7] = now[i8] = 1;
					for (int i = 2; i < 16; i++) {
						if (!check_div(now, 6, i))continue;
						ans.push_back(now);
						ans2.push_back(ansdef);
						ans2.back()[6] = i;
						break;
					}

				}
}

v<int> divisors(v<bool> a) {
	v<int>ret;
	forn(15)ret.push_back(0);
	for (int i = 2; i <= 10; i++) {
		for (int j = 2; j < 30;j++)if (check_div(a, i, j)) {
			ret[i] = j;
			break;
		}

		if (ret[i] == 0) {
			ret[0] = -1;
			return ret;
		}
	}
	return ret;

}


void generate2(int len, int amount) {
	v<bool>def;
	v<int>defint;
	forn(20)defint.push_back(0);
	forn(len)def.push_back(0);
	for (int i = (1 << (len-1)) + 1;; i+=2) {
		if (ans.size() == amount)return;
		v<bool>curnum;
		for (int j = 15; j >= 0; j--)curnum.push_back(1 << j & i);
		v<int>nowans = divisors(curnum);
		if (nowans[0] == -1)continue;
		ans.push_back(curnum);
		ans2.push_back(nowans);


	}


}



ll gen_number(v<bool>a, ll b) {
	ll ret = 0;
	ll state = 1;
	for (int i = a.size() - 1; i >= 0; i--) {
		ret += state*a[i];
		state *= b;
	}
	return ret;

}



int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif
	forn(15)ansdef.push_back(0);
	ansdef[2] = ansdef[4] = ansdef[8] = ansdef[10] = 3;
	ansdef[3] = ansdef[5] = ansdef[7] = ansdef[9] = 2;
	int T; cin >> T;
	int N, J; cin >> N >> J;
	if (N>30)generate(N, J);
	else generate2(N, J);
	forn(ans.size()) {
		for (int j = 2; j <= 10; j++)if(!check_div(ans[i],j,ans2[i][j]))
		int asdf = 15;

	}
	cout << "Case #1:\n";
	forn(ans.size()) {
		fornj(ans[i].size())cout << ans[i][j];
		for (int k = 2; k <= 10; k++) {
			cout << " " << ans2[i][k];

		}
		cout << endl;

	}

	return 0;

}

