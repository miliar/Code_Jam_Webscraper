#include <iostream>
#include <string.h>
#include <stdio.h>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <math.h>

using namespace std;
int cas;
int ans;
int tt,n;
bool f[20];
char s[200][200];
int heh[100];
int lst[26];
void check()
{
	int i,j,k,t;
	memset(lst,0,sizeof(lst));
	t=1;
	for (i=1;i<=n;i++)
	{
		int l;
		l=strlen(s[heh[i]]);
		for (j=0;j<l;j++)
		{
			int kk;
			kk=s[heh[i]][j]-'a';
			if (lst[kk]==0)
			{
				lst[kk]=t;
				t++;
				continue;
			}
			else
			{
				if (t-lst[kk]>1) return;
				lst[kk]=t;
				t++;
			}
		}
	}
	ans+=1;
}
void  dfs(int k)
{
	int i;
	if (k==n)
	{
		check();
		return;
	}
	for (i=1;i<=n;i++)
	{
		if (!f[i]) 
			{
				f[i]=true;
				heh[k+1]=i;
				dfs(k+1);
				f[i]=false;
			}
	}
	return;
}
void work()
{
	int i;
	cin>>n;
	ans=0;
	for (i=1;i<=n;i++)
	{
		scanf("%s",s[i]);
	}
	memset(f,0,sizeof(f));
	dfs(0);
}
int main()
{
	int T;
	cas=0;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>T;
	while (T--)
	{
		cas++;
		work();
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
			
	return 0;
}
