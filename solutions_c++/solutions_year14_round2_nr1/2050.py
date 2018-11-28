#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<algorithm>
#include<vector>
#include<queue>
#include<list>
#include<string>
#include<set>
#include<map>
#include<iomanip>
#include<sstream>
#include<functional>
#include<climits>
#define eps 1e-9
const int mod = 1e9 + 7;
using namespace std;

int main(){

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i){
		int n;
		scanf("%d", &n);
		vector<string> a(n);
		for (int j = 0; j < n; ++j){
			cin >> a[j];
		}
		vector<int> ptrs(n, 0);
		int res = 0;
		bool f = 0, g = 0;
		while (1){
			if (f){
				for (int j = 0; j < n; ++j){
					if (ptrs[j] != a[j].size()){
						printf("Case #%d: Fegla Won\n", i);
						g = 1;
						break;
					}
				}
				break;
			}
			vector<int> has;
			int m = 0;
			char c = a[0][ptrs[0]];
			for (int j = 0; j < n; ++j){
				if (c != a[j][ptrs[j]]){
					printf("Case #%d: Fegla Won\n", i);
					g = 1;
					break;
				}
				int cur = ptrs[j], idx = ptrs[j] - 1;
				while (cur < a[j].size() - 1 && a[j][cur] == a[j][cur + 1]){
					cur++;
				}
				ptrs[j] = cur + 1;
				if (ptrs[j] == a[j].size()) f = 1;
				m += cur - idx;
				has.push_back(cur - idx);
			}
			if (g) break;
			int best = m / n;
			for (int j = 0; j < has.size(); ++j){
				res += abs(best - has[j]);
			}
		}
		if(!g) printf("Case #%d: %d\n", i, res);
	}
	return 0;
}