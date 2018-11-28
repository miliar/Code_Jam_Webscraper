#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <queue>
#include <cstdio>
#include <cmath>
using namespace std;


typedef long long llong;
const int inf = (int)1e9;
const double eps = 1e-9;
const int MAXN = 40;

int a[MAXN] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001};

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		llong A, B;
		cin >> A >> B;
		int res = 0;
		for (int i = 0; i < MAXN; ++i) {
			if (a[i] >= A && a[i] <= B) {
				++res;
			}
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
	
	return 0;
}
