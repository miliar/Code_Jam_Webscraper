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


int to_i(string &s) {
	int res = 0;
	for (int i = 0; i<s.size(); i++)res = res * 10 + s[i] - '0';
	return res;
}
string to_s(long long n) {
	string s;
	do { s += n % 10 + '0'; n /= 10; } while (n);
	reverse(s.begin(), s.end());
	return s;
}



int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	rep(tcase,t) {
		string ans = "INSOMNIA";
		long long n,x;
		int cnt = 0,c=0;
		bool f[10] = {};
		cin >> n;
		x = n;
		while(cnt<10){
			c++;
			if (c == 1000000)break;
			string s = to_s(x);
			rep(i, s.size()) {
				if (!f[s[i] - '0'])cnt++;
				f[s[i] - '0'] = true;
			}
			x += n;
		}
		if (cnt==10)ans = to_s(x-n);
		cout << "Case #" << tcase+1 << ": "<<ans<<endl;
	}


	return 0;
}