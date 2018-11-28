#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
using namespace std;
int sx[4];
int ans[100001][3];
int n,r,p,s;
string solve(int d,int dep)
{
	if(dep==n)
	{
		if(d==1)
			return "R";
		if(d==2)
			return "P";
		if(d==3)
			return "S";
	}
	if(d==1)
	{
		string s1=solve(1,dep+1);
		string s2=solve(2,dep+1);
		if(s1<s2)
			return s1+s2;
		else
			return s2+s1;
	}
	if(d==2)
	{
		string s1=solve(2,dep+1);
		string s2=solve(3,dep+1);
		if(s1<s2)
			return s1+s2;
		else
			return s2+s1;
	}
	if(d==3)
	{
		string s1=solve(3,dep+1);
		string s2=solve(1,dep+1);
		if(s1<s2)
			return s1+s2;
		else
			return s2+s1;
	}
}
int main()
{
//	freopen("A-small-attempt2.in","r",stdin);
//	freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,k=0;
	scanf("%d",&T);
	while(T>0)
	{
		T--;
		k++;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		int i;
		bool flag=false;
		int flag1=0;
		printf("Case #%d: ",k);
		for(i=1;i<=3;i++)
		{
			memset(sx,0,sizeof(sx));
			sx[i]=1;
			int ss=0;
			while(ss<n)
			{
				ss++;
				int s1=sx[1],s2=sx[2],s3=sx[3];
				sx[1]=s1+s3;
				sx[2]=s2+s1;
				sx[3]=s3+s2;
			}
			if(sx[1]==r&&sx[2]==p&&sx[3]==s)
			{
				//printf("POSSIBLE\n");
				flag=true;
				flag1=i;
				break;
			}
		}
		if(!flag)
			printf("IMPOSSIBLE\n");
		else
		{
			cout<<solve(flag1,0);
			/*memset(sx,0,sizeof(sx));
			memset(ans,0,sizeof(ans));
			sx[flag1]=1;
			int l=1;
			ans[l][0]=flag1;
			int ss=0;
			while(ss<n)
			{
				ss++;
				int t=l;
				for(i=1;i<=t;i++)
				{
					l++;
					if(ans[i][0]==1)
					{
						ans[ans[i][1]][0]=l;
						ans[l][1]=ans[i][1];
						ans[i][1]=l;
						ans[l][0]=2;
						ans[l][2]=i;
					}
					else if(ans[i][0]==2)
					{
						ans[ans[i][1]][0]=l;
						ans[l][1]=ans[i][1];
						ans[i][1]=l;
						ans[l][0]=3;
						ans[l][2]=i;
					}
					else if(ans[i][0]==3)
					{
						ans[ans[i][2]][1]=l;
						ans[l][2]=ans[i][2];
						ans[i][2]=l;
						ans[l][0]=1;
						ans[l][1]=i;
					}
				}
			}
			int beg=0;
			for(i=1;i<=l;i++)
			{
				if(ans[i][2]==0)
				{
					beg=i;
					break;
				}
			}
			int d=beg;
			while(ans[d][1]!=0)
			{
				if(ans[d][0]==1)
					printf("P");
				else if(ans[d][0]==2)
					printf("R");
				else if(ans[d][0]==3)
					printf("S");
				d=ans[d][1];
			}
			if(ans[d][0]==1)
				printf("P");
			else if(ans[d][0]==2)
				printf("R");
			else if(ans[d][0]==3)
				printf("S");*/
			printf("\n");
		}
	}
	return 0;
}
