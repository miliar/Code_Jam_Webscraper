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
		map<int, int> mp;
		int n;
		cin >> n;
		rep(i,(2*n-1)*n) {
			int a;
			cin >> a;
			++mp[a];
		}
		cout << "Case #" << icase + 1 << ":";
		for (auto a:mp) {
			if (a.second & 1)cout << ' ' << a.first;
		}
		cout << endl;
	}


	return 0;
}