#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
#define ll long long
#define inf 1000000000
#define L(s) ((int)(s).size())
#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define x first
#define y second
#define all(s) (s).begin(), (s).end()
#define mp make_pair
int tc;
double x,f,c;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tc;
	for(int tn = 1; tn <= tc; ++tn) {
		cin >> c >> f >> x;
		double v = 2, t = 0;
		while(1) {
			double simple = x / v;
			double diff = c / v + x / (f + v);
			if (simple < diff) {
				t += simple;
				break;
			} else {
				t += c / v;
				v += f;
			}
		}
		printf("Case #%d: %0.9lf\n", tn, t);
	}
}