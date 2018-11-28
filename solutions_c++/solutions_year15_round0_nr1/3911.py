/* ***********************************************
Author        :5lyTher1n
Created Time  :2015/4/11 9:56:47
File Name     :F:\Code\GCJ\a.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <time.h>
using namespace std;

int T;
int t = 1;
int n;
long ans,now;
char str[2000];

int main()
{

	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d", &T);
	
	while(T--)
	{
			scanf("%d", &n);
			scanf("%s", str);

			ans = 0;
			now = 0;

			now = str[0] - '0';

			for(int i = 1;i <= n;i++)
			{
				int k = str[i] - '0';
				if(k)
				{
					if(i <= now){now += k; }
					else
					{
						int h = i - now;
						now += h + k;
						ans +=h;
					}
				}
			}
	printf("Case #%d: %ld\n", t++, ans);
	}
	return 0;
}
		

