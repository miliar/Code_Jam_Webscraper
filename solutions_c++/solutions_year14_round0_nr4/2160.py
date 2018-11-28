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
int n;
double na[1111], ke[1111];
int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tc;
	for(int tn = 1; tn <= tc; ++tn) {
		cin >> n;
		for(int i = 0; i < n; ++i) cin >> na[i];
		for(int i = 0; i < n; ++i) cin >> ke[i];
		sort(na, na + n);
		sort(ke, ke + n);
		int j = 0, na_s_2 = 0;
		for(int i = 0; i < n; ++i) {
			while (j < n && ke[j] < na[i]) ++j;
			if (j == n) ++na_s_2; else ++j;
		}
		j = 0;
		int na_s_1 = 0;
		for(int i = 0; i < n; ++i) {
			if (na[i] > ke[j]) {
				++j;
				++na_s_1;
			} 
		}
		printf("Case #%d: %d %d\n", tn, na_s_1, na_s_2);
	}
}