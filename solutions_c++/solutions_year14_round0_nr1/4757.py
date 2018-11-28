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
#include <queue>

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
	int t, arr[5][5], arr2[5][5], a, b, y;
	cin >> t;

	for (int T = 1; T <= t; T++) {
		cin >> a;
		For(i, 1, 5)
			For (j, 1, 5) 
				cin >> arr[i][j];

		cin >> b;
		For(i, 1, 5)
			For (j, 1, 5) 
				cin >> arr2[i][j];

		VI v;
		For (i, 1, 5) {
			For (j, 1, 5) {
				if (arr2[b][j] == arr[a][i]) v.PB(arr[a][i]);
			}
		}
		cout << "Case #" << T << ": ";
		if (v.SZ == 1) {
			cout << v[0] << endl;
		}
		else if (v.SZ == 0) {
			cout << "Volunteer cheated!" << endl;
		}
		else {
			cout << "Bad magician!" << endl;
		}
	}

	
	return 0;
}
