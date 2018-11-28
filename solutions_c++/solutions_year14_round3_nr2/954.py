#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:16777216")
#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>
#include <time.h>
#include <list>
#include <iterator>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define pb push_back
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB; 
typedef vector<VI> VVI;
const long double pi = 3.14159265358979323846;
const int inf = (int)1e9;
const LL llinf = (LL)1e18;

const int base = 10;
double eps = 1e-9;

bool pred (const pair<PII,int>& i, const pair<PII,int>& j) {
    if (i.first.second == j.first.second) {
        return i.first.first < j.first.first;
    }
    return i.first.second < j.first.second;
}

LL gcd(LL a, LL b) {
	while(b) {
		a %= b;
		swap(a,b); 
	}
	return a;
}

int xz = 0;

void solve(LL a, LL b) {
	LL g = gcd(a,b);
	a /= g;
	b /= g;
	if (b % 2 != 0) {
		if (a * 2 >= b) {
			xz = 1;
			cout << "1";
		} else {
			cout << "impossible";
		}
		return;
	}
	int ans = 1;
	while(b % 2 == 0) {
		b /= 2;
		if (a >= b) {
			xz = ans;
			cout << ans;
			return;
		}
		++ans;
	}
	if (2 * a - b >= 0) {
		xz = ans;
		cout << ans;
	} else {
		cout << "impossible";
	}
}

int res = inf;

void go(int x, int y, int now) {
	if (2 * x - y >= 0) {
		res = min(res,now + 1);
		return;
	}
	if (y % 2 == 0) {
		y /= 2;
		go(x,y,now + 1);
	}
}

int main(){
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif	
	int t;
	cin >> t;
	FOR(tt,t) {
		int n;
		cin >> n;
		vector<string> s(n);
		VI a(n);		
		FOR(i,n) {
			cin >> s[i];
			a[i] = i;
		}
		int res = 0;		
		do {
			bool check = true;
			VI b(26, -1);
			int k = 0;
			FOR(i,n) {				
				FOR(j,s[a[i]].size()) {
					int x = s[a[i]][j] - 'a';
					if (b[x] == -1) {
						b[x] = k;
						++k;
						continue;
					}
					if (b[x] + 1 != k) {
						check = false;
						break;
					}
					b[x] = k;
					++k;
				}
				if (!check) {
					break;
				}
			}
			if (check) {
				++res;
			}
		} while(next_permutation(a.begin(),a.end()));
		cout << "Case #" << tt + 1 << ": ";
		cout << res;
		cout << "\n";
	}
    return 0;
}
