#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define ll long long
#define INF 0x3f3f3f3f
#define LL_INF 0x3f3f3f3f3f3f3f3f
#define MAX

bool judge(string s)
{
	for (int i = 0; i < s.size(); ++i)
		if (s[i] == '-')
			return false;
	return true;
}

int main()
{
	//freopen("debug\\in.txt", "r", stdin);
	//freopen("CON", "w", stdout);
	int i, j, k;
	int test;
	cin >> test;
	int kase = 1;
	while (test--) {
		string str;
		cin >> str;
		vector<vector<string> > vs;
		vector<string> vm;
		vm.push_back(str);
		vs.push_back(vm);
		map<string, int> mp;
		mp[str] = 1;
		i = 0;
		bool flag = 0;
		while (1) {
			vm.clear();
			for (j = 0; j < vs[i].size(); ++j) {
				if (judge(vs[i][j])) {
					flag = 1;
					break;
				}
				int len = vs[i][j].size();
				for (k = 1; k <= len; ++k) {
					string tmp = vs[i][j].substr(0, k);
					reverse(tmp.begin(), tmp.end());
					for (int l = 0; l < tmp.size(); ++l) 
						tmp[l] = (tmp[l] == '+') ? '-' : '+';
					tmp += vs[i][j].substr(k, len);
					if (!mp[tmp]) {
						vm.push_back(tmp);
						mp[tmp] = 1;
					}
				}
			}
			if (flag) break;
			vs.push_back(vm);
			i++;
		}
		printf("Case #%d: %d\n", kase++, vs.size() - 1);
	}
	return 0;
}