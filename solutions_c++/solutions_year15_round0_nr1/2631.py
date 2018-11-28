#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int mx, res = 0;
		string str;
		cin >> mx >> str;
		int cnt = str[0] - '0';
		for (int j = 1; j <= mx; j++) {
			int cnt_here = str[j] - '0';
			if (cnt_here && cnt < j) {
				res += j - cnt;
				cnt = j + cnt_here;		
			}
			else
				cnt += cnt_here;			
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
