#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = int(1e6 + 5);

int a[N], pr[4][4];
bool s[4][4];

pair<int, int> operator * (pair<int, int> a, pair<int, int> b) {
	return mp(pr[a.first][b.first], s[a.first][b.first] ^ a.second ^ b.second);
}

pair<int, int> power(pair<int, int> v, LL p) {
	if (!p) return mp(0, 0);
	if (p & 1) {
		return v * power(v, p - 1); 
	}
	pair<int, int> x = power(v, p / 2);
	return x * x;
}

LL l, x;

pair<int, int> calc(int x) {
	pair<int, int> v = mp(0, 0);
	for (int i = x; i < l; i++) {
		v = v * mp(a[i], 0);						
	}
	return v;
}

int main() {
	pr[0][0] = 0;
	pr[0][1] = 1;
	pr[0][2] = 2;
	pr[0][3] = 3;
	pr[1][0] = 1;
	pr[1][1] = 0;
	pr[1][2] = 3;
	pr[1][3] = 2;
	pr[2][0] = 2;
	pr[2][1] = 3;
	pr[2][2] = 0;
	pr[2][3] = 1;
	pr[3][0] = 3;
	pr[3][1] = 2;
	pr[3][2] = 1;
	pr[3][3] = 0;
	s[1][1] = s[2][2] = s[3][3] = s[1][3] = s[2][1] = s[3][2] = 1;

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {					
		string str;
		cin >> l >> x;
		cin >> str;		
		
		for (int j = 0; j < l; j++) {
			switch (str[j]) {
				case 'i': a[j] = 1; break;
				case 'j': a[j] = 2; break;
				case 'k': a[j] = 3; break;
			}
		}

		bool ok = 0;

		int iter = 0;
		int stage = 1, cnt = 0;
		pair<int, int> v = mp(0, 0);
		for (LL j = 0;; j = (j + 1) % l) {
			if (j == 0) cnt++;
			iter++;
			v = v * mp(a[j], 0);							
			if (v.first == stage && v.second == 0) {				
				stage++;
				v = mp(0, 0);				
				if (stage == 4) {
					//cerr << j << endl;			
					pair<int, int> v1 = calc(j + 1), v2 = power(calc(0), x - cnt);
					//cerr << j << endl;
					if (v1 * v2 == mp(0, 0)) {
						ok = 1;
					}
					break;
				}
			}	
			if (iter == min(LL(1e8), x * l)) {
				//cerr << i << " " << stage << endl;
				break;
			}
		}		
		
		if (ok) {
			printf("Case #%d: YES\n", i + 1);
		}
		else {
			printf("Case #%d: NO\n", i + 1);
		}
	}
	return 0;
}       
