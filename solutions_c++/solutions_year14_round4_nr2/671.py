
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

const int mx = 1000+10;
int ori[mx], a[mx], b[mx], n;

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", &ori[i]);

		int cnt = 0, cur = -1;
		for (int i = 0; i < n; i++)
		{
			int mnv = 2100000000, mnid = -1;
			for (int j = 0; j < n; j++)
				if (ori[j] < mnv && ori[j] > cur) mnv = ori[j], mnid = j;
			memcpy(a, ori, sizeof(ori));
			int t1 = 0;
			for (int j = mnid; j < n - 1; j++) 
				if (a[j] < a[j+1]) {swap(a[j], a[j+1]); t1++;}
			memcpy(b, ori, sizeof(ori));
			int t2 = 0;
			for (int j = mnid; j > 0; j--) 
				if (b[j] < b[j-1]) {swap(b[j], b[j-1]); t2++;}
			cur = mnv;
			if (t1 < t2)
			{
				memcpy(ori, a, sizeof(ori)); cnt += t1;
			}
			else
			{
				memcpy(ori, b, sizeof(ori)); cnt += t2;
			}
		}
		printf("Case #%d: %d\n", tc, cnt);
	}

}