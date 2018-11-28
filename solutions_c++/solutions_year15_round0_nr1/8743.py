#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <climits>
#include <sstream>
#include <deque>
#include <map>
#include <cmath>
#include <cstring>
#include <fstream>
using namespace std;

template<int N = 1000000 + 5>
struct UFSet {
	int fa[N];
	void init(int n) {
		for (int i = 0; i <= n; ++i) {
			fa[i] = i;
		}
	}
	int find(int x) {
		return x == fa[x] ? x : fa[x] = find(fa[x]);
	}
	void link(int a, int b) {
		a = find(a);
		b = find(b);
		fa[a] = b;
	}
};

template<int r, int c>
struct Mat {
	int data[r][c];
};

template<int m, int p, int n>
Mat<m, n> operator * (const Mat<m, p>& a, const Mat<p, n>& b) {
	Mat<m, n> ans;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			int r = 0;
			for (int k = 0; k < p; ++k) {
				r += a.data[i][k] * b.data[k][j];
			}
			ans.data[i][j] = r;
		}
	}
	return ans;
}

template<int r, int c>
istream& operator >> (istream& cin, Mat<r, c>& o) {
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			cin >> o.data[i][j];
		}
	}
	return cin;
}

template<int r, int c>
ostream& operator << (ostream& cout, const Mat<r, c>& o) {
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			cout << o.data[i][j] << " ";
		}
		cout << endl;
	}
	return cout;
}

template <class T>
T gcd(T a, T b) {
	return b == 0 ? a : gcd(b, a % b);
}

bool isprime(int n) {
	if (n <= 1) return false;
	for (int i = 2; i * i <= n; ++i) {
		if (n % i == 0) return false;
	}
	return true;
}

template<int N = 1000000 + 5>
struct Primes {
	int isprime[N];
	int primes[N];
	int c;

	Primes(int n = N - 1) {
		isprime[1] = false;
		for (int i = 2; i <= n; ++i) {
			isprime[i] = true;
		}
		c = 0;
		for (int i = 2; i <= n; ++i) {
			if (isprime[i]) {
				primes[c++] = i;
				for (int j = i + i; j <= n; j += i) {
					isprime[j] = false;
				}
			}
		}
	}
};

ostream& operator << (ostream& cout, const vector<int>& v) {
	bool first = true;
	for (int i = 0; i < v.size(); ++i) {
		if (first) {
			first = false;
		}
		else {
			cout << " ";
		}
		cout << v[i];
	}
	return cout;
}

istream& operator >> (istream& cin, vector<int>& v) {
	for (int i = 0; i < v.size(); ++i) {
		cin >> v[i];
	}
	return cin;
}

///////////////////////////////////////

int main() {
	int re; cin >> re;
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%*d");
		string s; cin >> s;
		int ans = 0;
		int cnt = 0;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] == '0') {
				continue;
			}
			else {
				if (cnt < i) {
					ans += (i - cnt);
					cnt += (i - cnt);
				}
				cnt += s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", ri, ans);
	}
}