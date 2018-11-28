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

int solve() {
	vector<bool> ans(16, true);
	int r1, r2;
	cin >> r1;
	int x;
	for (int i = 1; i <= 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> x;
			if (i != r1)
				ans[x - 1] = false;
		}
	}
	cin >> r2;
	for (int i = 1; i < 5; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> x;
			if (i != r2)
				ans[x - 1] = false;
		}
	}
	int res = 0, num = 0;
	for (int i = 0; i < ans.size(); ++i)
		if (ans[i]) {
			++num;
			res = i + 1;
		}
	if (num == 0)
		return 0;
	if (num > 1)
		return -1;
	return res;
}

void printSol(int x) {
	if (x > 0)
		cout << x;
	if (x == 0)
		cout << "Volunteer cheated!";
	if (x == -1)
		cout << "Bad magician!";
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		printSol(solve());
		cout << endl;
		std::cerr << i << endl;
	}
	return 0;
}
