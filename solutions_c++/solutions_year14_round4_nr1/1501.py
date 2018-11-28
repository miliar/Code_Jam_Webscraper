#include <bits/stdc++.h>

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
T power(T a, int n){
	T res = 1;
	while (n) {
		if (n & 1) res = (res * a) % mod;
		n >>= 1; a = (a * a) % mod;
	}
	return res;
}

int main()
{
	int t;
	int n;
	int x;
	int c;
	int arr[100005];

	cin >> t;

	for (int T = 1; T <= t; T++) {
		cin >> n >> x;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		sort(arr, arr+n);
		c = 0;
		int i = 0, j = n - 1;
		while (i <= j) {
			if (arr[i] + arr[j] <= x) {
				c++;
				i++;
				j--;
			}
			else {
				c++;
				j--;
			}
		}
		cout << "Case #" << T<< ": " << c << endl;
	}

	
	return 0;
}
