#include <bits/stdc++.h>
using namespace std;

bool able[5][5];
char buf[10];

int n;

bool oped[5];bool atwork[5];

bool check(int ind)
{
	if(ind == n + 1)return true;
	for(int j = 1 ; j <= n ; j++)
	{
		if(atwork[j])continue;
		bool bad = true;
		for(int i = 1 ; i <= n ; i++)
		{
			if(!oped[i] && able[j][i])
			{
				bad = false;
				oped[i] = true;
				atwork[j] = true;
				if(!check(ind + 1))
					return false;
				oped[i] = false;
				atwork[j] = false;
			}
		}
		if(bad)return false;
	}
	return true;
}

int ans;

void search(int i , int j , int costnow)
{
	if(i == n + 1 && j == 1)
	{
		memset(oped , 0 , sizeof oped);
		memset(atwork , 0 , sizeof atwork);
		if(check(1))
			if(costnow < ans)
			{
				ans = costnow;
			}
		return;
	}
	if(j == n + 1){search(i + 1 , 1 , costnow);return;}
	if(able[i][j]){search(i , j + 1 , costnow);return;}
	search(i , j + 1 , costnow);
	able[i][j] = true;
	search(i , j + 1 , costnow + 1);
	able[i][j] = false;
}

int main()
{
	int test;scanf("%d" , &test);
	for(int t = 1 ; t <= test ; t++)
	{
		scanf("%d" , &n);
		for(int i = 1 ; i <= n ; i++)
		{
			scanf("%s" , buf + 1);
			for(int j = 1 ; j <= n ; j++)
				able[i][j] = (buf[j] == '1');
		}
		ans = 2100000000;
		search(1 , 1 , 0);
		printf("Case #%d: %d\n" , t , ans);
	}
	return 0;
}