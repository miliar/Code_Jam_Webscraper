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
	rep(icase,T) {
		/*string ans = "";
		string s;
		cin >> s;
		int n=s.size();
		rep(i,1<<n) {
			string t;
			rep(j, n) {
				if (i >> j & 1)t = t + s[j];
				else t = s[j] + t;
			}
			ans = max(ans, t);
		}*/
		string ans = "";
		string s;
		cin >> s;
		int n = s.size();
		rep(i,n) {
			if (s[i] + ans > ans + s[i])ans = s[i] + ans;
			else ans += s[i];
		}

		cout << "Case #" << icase+1 << ": " << ans << endl;
	}


	return 0;
}