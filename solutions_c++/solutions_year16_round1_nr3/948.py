#define _CRT_SECURE_NO_WARNINGS
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cmath>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<numeric>
#include<functional>
#include<algorithm>
#include<bitset>
#include<tuple>
#include<unordered_set>
#include<random>
using namespace std;
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define all(v) v.begin(),v.end()
#define uniq(v) v.erase(unique(all(v)),v.end())


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	rep(icase, T) {
		int ans = 0;
		int n;
		cin >> n;
		int bff[10];
		rep(i,n) {
			int a;
			cin >> a;
			bff[i] = a - 1;
		}
		int p[10];
		rep(i, n)p[i] = i;
		do {
			bool f = true;
			for (int i = 1; i < n;i++) {
				if ((p[1]==bff[p[0]]||p[i]==bff[p[0]]) && (p[0] == bff[p[i]] || p[i - 1] == bff[p[i]]))ans = max(ans,i+1);
				if (i+1< n && p[i+1] != bff[p[i]] && p[i-1] != bff[p[i]])break;
			}
		} while (next_permutation(p, p + n));
		

		cout << "Case #" << icase + 1 << ": " << ans << endl;
	}


	return 0;
}