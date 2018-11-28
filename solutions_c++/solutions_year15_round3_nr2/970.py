#include <iostream>
#include <string>
#include <sstream>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
#include <bitset>
#include <numeric>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9
#define MOD 1000000007
#define getcx getchar_unlocked
#define putcx putchar_unlocked
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64

void run(int s, string& a, string& tar, string curr, ll& mx, vector<ll>& freq, ll& total) {
	if (curr.size() == s) {
		ll counter = 0;
		for (int i = 0; i < curr.size(); i++) {
			bool flag = true;
			for (int j = 0; j < tar.size(); j++)
				if (curr[i + j] != tar[j]) {
					flag = false; break;
				}
			counter += flag;
		}
		freq[counter]++;
		total++;
		mx = max(mx, counter);
		return;
	}
	for (int i = 0; i < a.size(); i++) {
		run(s, a, tar, curr + a[i], mx, freq,total);
	}
}


int main() {
	ios_base::sync_with_stdio(0);

	int T, k, l, s;
	string tar,a;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> k >> l >> s;
		cin >> a;
		cin >> tar;
		ll mx = 0,total = 0;
		vector<ll> freq(s+1, 0);
		run(s, a, tar, "", mx, freq, total);
		double res = 0;
		for(int i=0;i<freq.size();i++){
			//cout<<freq[i]<<" ";
			res += (mx-i)*(freq[i]*1.0)/ (total*1.0);
		}
		printf("Case #%d: %.7f\n", t,res);
	}

	return 0;
}