#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#define _USE_MATH_DEFINES
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>
#include<map>
#include<ctime>
#include<cstdio>

 
using namespace std; 
 
typedef long long ll; 
typedef unsigned int uint; 
typedef unsigned long long ull; 
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<char, char> pcc;
typedef pair<double, double> pdd;

#define show(x) cerr << x
#define debug(x) show(#x << ": " << (x) << endl)

const long double PI = 3.14159265358979323846;  
const long double gammama = 0.57721566490153286060;
const long double eps = 1e-7;
const int INF = 1000 * 1000 * 1000 + 1;
const ll LINF = (ll)1000 * 1000 * 1000 * 1000 * 1000 * 1000;

void print(pii res) {
	cout << res.first << " " << res.second << endl;
}

int get(const vector<double>& a, const vector<double>& b) {
	int n = a.size();
	int res = n;
	int r = 0;
	for (int i = 0; i < n; ++i) {
		while(r < n) 
			if (b[r] < a[i])
				++r;
			else
				break;
		res = min(res, r - i - 1 + n);
	}
	return res;
}

pii solve() {
	int n;
	cin >> n;
	vector<double> a(n), b(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	for (int i = 0; i < n; ++i) 
		cin >> b[i];
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());
	return pii(get(a, b), n - get(b, a));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		
		cout << "Case #" << i + 1 << ": ";
		print(solve());
		std::cerr << i << endl;
	}
	return 0;
}
