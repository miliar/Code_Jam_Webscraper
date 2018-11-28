#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
const int N = 1005;
const int M = 101;
string ret[N];
int fac[N][11],t,n,tot;
char sta[N];
void dfs(int k)
{
	if(t==tot)return ;
	if(k==n)
	{
		int b;
		for(b=2;b<=10;b++)
		{
			int f=0;
			for(int j=2;j<=M;j++)
			{
				int x=0,v=1;
				for(int i=0;i<n;i++)
				{
					if(sta[i]=='1')
					{
						x=(x+v)%j;
					}
					v=v*b%j;
				}
				if(!x)
				{
					f=1;
					fac[t][b]=j;
					break;
				}
			}
			if(!f)break;
		}
		if(b==11)
		{
			ret[t]="";
			for(int i=n-1;i>=0;i--)ret[t]+=sta[i];
			t++;
		}
		return ;
	}
	if(!k||k==n-1)
	{
		sta[k]='1';
		dfs(k+1);
	}
	else
	{
		sta[k]='0';
		dfs(k+1);
		sta[k]='1';
		dfs(k+1);
	}
}
int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	srand(time(NULL));
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d:\n",ca++);
		scanf("%d%d",&n,&tot);
		dfs(0);
		for(int i=0;i<tot;i++)
		{
			cout << ret[i];
			for(int j=2;j<=10;j++)
			{
				cout << " " << fac[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}

