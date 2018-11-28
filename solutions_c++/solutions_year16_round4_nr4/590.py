#include<bits/stdc++.h>
using namespace std;
int ans,tmp;
int n,m;
bool flag[50],flag2[10],flag3[10];
int a[10][10];
int lst[100],lst2[100];
bool c1,c2;
void check2(int x)
{
	if (x == n)
	{
		/*
		int tmp = n;
		memset(flag2,0,sizeof flag2);
		for (int i=0;i<n;i++)
		{
			if (flag2[lst2[i]]==false) tmp--;
			flag2[lst2[i]] = true;
		}
		if (tmp != 0) c2 = false;
		*/
		return;
	}
	int self = lst[x];
	bool chosen = false;
	for (int i=0;i<n;i++)
		if (a[self][i] == 1 && flag3[i]==false) {
			chosen = true;
			break;
		}
	if (chosen == false) {
		c2 = false;
		return;
	}
	for (int i=0;i<n;i++)
		if (a[self][i] == 1 && flag3[i]==false)
		{
			flag3[i] = true;
			lst2[x] = i;
			check2(x+1);
			flag3[i] = false;
			if (c2 == false) return;
		}
}
void check(int x)
{
	if (x == n)
	{
		c2 = true;
		check2(0);
		if (c2 == false) c1 = false;
		return;
	}
	for (int i=0;i<n;i++)
		if (flag[i]==false)
		{
			flag[i] = true;
			lst[x] = i;
			check(x+1);
			flag[i] = false;
			if (c1 == false) return;
		}
}
void dfs(int x,int y,int val)
{
	if (val >= ans) return;
	if (x == n)
	{
		c1 = true;
		check(0);
		if (c1) ans = min(ans,val);
		return;
	}
	if (a[x][y] == 1) {
		dfs(x+(y+1)/n,(y+1) % n,val);
		return;
	}
	a[x][y] = 1;
	dfs(x+(y+1)/n,(y+1) % n,val + 1);
	a[x][y] = 0;
	dfs(x+(y+1)/n,(y+1) % n,val);
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int T,test = 0;
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d\n",&n);
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++)
			{
				char x;
				scanf("%c",&x);
				a[i][j] = x - '0';
			}	
			scanf("\n");
		}	
		ans = 100;
		dfs(0,0,0);
		printf("Case #%d: %d\n",++test,ans);
					
	}
	
	
}
