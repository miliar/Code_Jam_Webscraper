#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <stack>
#include <deque>

#define PB push_back
#define MP make_pair
#define all(v) v.begin(), v.end()
#define For(i, a, b) for (int i = a; i < b; i++)
#define Rfor(i, b, a) for (int i = b; i > a; i--)
#define Si(a) scanf("%d", &(a))
#define Sl(a) scanf("%lld", &(a))
#define SZ size()
#define F first
#define S second
#define B begin()
#define E end()

#define mod 1000000007

using namespace std;

typedef unsigned long long int ull;
typedef long long int lli;
typedef vector<int> VI;
typedef pair<int, int> pii;

template <typename T>
T power(T a, int n)
{
	T res = 1;
	while (n) {
		if (n % 2 == 1) res = (res * a) % mod;
		n /= 2;
		a = (a * a) % mod;
	}
	return res;
}

int main()
{
	int T;
	int n;
	double x;

	cin >> T;
	For (t, 1, T+1) {
		cin >> n;
		deque<double> nao, ken;
		vector<double> nao2, ken2;
		For (i, 0, n) {
			cin >> x;
			nao.PB(x);
			nao2.push_back(x);
		}
		For (i, 0, n) {
			cin >> x;
			ken.PB(x);
			ken2.push_back(x);
		}
		sort(all(nao));
		sort(all(ken));
		sort(all(nao2));
		sort(all(ken2));
		
		/*
		For (ll, 0, n) printf("%5.3f ", nao[ll]);
		cout << endl;
		For (ll, 0, n) printf("%5.3f ", ken[ll]);
		cout << endl;
		*/

		int a1 = 0;		
		int j = 0;
		int i;
		for (i = n - 1; i >= 0; i--) {
			if (nao.back() > ken[i]) {
				nao.pop_back();
				a1++;
			}
			else {
				nao.pop_front();
			}
		}

		j = 0;
		for (i = 0; i < n && j < n;) {
			while (j < n && ken2[j] < nao2[i]) j++;
			if (j < n) {
				i++;
				j++;
			}
		}

		cout << "Case #" << t << ": " << a1 << " " << n-i << endl;
	}

	
	return 0;
}
