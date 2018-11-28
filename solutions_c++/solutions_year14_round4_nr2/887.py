#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
int n, v[1000];
int calc(vector<int> s){
	vector<int> z(v, v + n);
	int res = 0;
	for (int i = 0; i < n; ++i)
		for (int j = i; j < n;++j)
			if (s[i] == z[j]){
				while (j>i){
					swap(z[j], z[j - 1]);
					--j;
					++res;
				}
				break;
			}
	return res;
}
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T){
		printf("Case #%d: ", T);
		scanf("%d", &n);
		int mid = -(1<<30);
		for (int i = 0; i < n; ++i){
			scanf("%d", &v[i]);
			mid = max(mid, v[i]);
		}
		int res = 1 << 29;
		if (n == 1)
			res = 0;
		vector<int> rem, left, right;
		{
			rem.clear();
			for (int j = 0; j < n; ++j)
				if (v[j]!=mid)
					rem.push_back(v[j]);
			for (int i = 0; i < (1 << (n - 1)); ++i){
				left.clear();
				right.clear();
				for (int j = 0; j < rem.size();++j)
				if ((i >> j) & 1)
					left.push_back(rem[j]);
				else
					right.push_back(rem[j]);
				sort(left.begin(), left.end());
				sort(right.begin(), right.end());
				reverse(right.begin(), right.end());
				left.push_back(mid);
				for (int i = 0; i < right.size(); ++i)
					left.push_back(right[i]);
				res = min(res, calc(left));
			}
		}
		printf("%d\n", res);
	}
	return 0;
}