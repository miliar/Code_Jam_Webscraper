#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<list>
#include<sstream>
#include<utility>
using namespace std;
typedef int LL;
//typedef __int64 LL;
//typedef unsigned __int64 LL;

LL MX(LL a,LL b){return (a>b)?a:b;}
LL MN(LL a,LL b){return (a<b)?a:b;}
//LL ABS(LL a){return (a<0)?-1*a:a;}
//LL S(LL a){return a*a;}
char str[1000003];
LL id[1000003],val[1000003],L,n;
void f(LL idx)
{
	val[idx]=L-1-(idx+n-1)+1;
}
int main()
{
	LL t,cas=0,i,j,cnt,value;
	__int64 ans,v1;
	freopen("A-large.in","r",stdin);
	freopen("aao.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s%d",str,&n);
		L=strlen(str);
		for(i=0;i<L;i++)
		{
			id[i]=val[i]=0;
		}
		i=0;
		while(i<L)
		{
			cnt=0;
			j=i;
			while(j<L)
			{
				if(str[j]!='a'&&str[j]!='e'&&str[j]!='i'&&str[j]!='o'&&str[j]!='u')
				{
					cnt++;
					if(cnt>=n)
					{
						id[i+cnt-n]=1;
						f(i+cnt-n);
					}
					j++;
				}
				else
				{
					break;
				}
			}
			i=j+1;
		}
		value=0;
		for(i=L-1;i>=0;i--)
		{
			if(id[i]==0)
			{
				val[i]=value;
			}
			else
			{
				value=val[i];
			}
		}
		ans=0;
		for(i=0;i<L;i++)
		{		
			v1=val[i];
			ans+=v1;
		}
		printf("Case #%d: %I64d\n",++cas,ans);
	}
	return 0;
}