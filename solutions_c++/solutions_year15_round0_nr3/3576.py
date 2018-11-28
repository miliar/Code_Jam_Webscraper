#include<iostream>
using namespace std;
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<stack>
#include<map>
#include<set>
#include<string.h>
#include<math.h>
#define MOD 1000000007
#define MIN -100000000
#define MAX 100000000
#define ll long long int
/* HOPE n WILL :)
	NGU :)
	_/\_ 	*/
// MG
char s1[100005];
int a[100005][5];
int b[100005];
int m[15][15];
int main()
{
 	ll t,k=1,i,j,flag,temp1,l,s;
	ll ans;
	freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld %lld",&l,&temp1);
		scanf("%s",s1);
		for(i=0;i<temp1;i++)
		{
			for(j=0;j<l;j++)
			{
				if(s1[j]=='i')
					b[i*l+j]=2;
				else if(s1[j]=='j')
					b[i*l+j]=3;
				else if(s1[j]=='k')
					b[i*l+j]=4;
			}
		}
		m[1][1]=1; 
		m[1][2]=2; 
		m[1][3]=3; 
		m[1][4]=4;
		m[2][1]=2; 
		m[2][2]=-1; 
		m[2][3]=4; 
		m[2][4]=-3;
		m[3][1]=3; 
		m[3][2]=-4; 
		m[3][3]=-1; 
		m[3][4]=2;
		m[4][1]=4; 
		m[4][2]=3; 
		m[4][3]=-2; 
		m[4][4]=-1;
		l*=temp1;
		memset(a,0,sizeof(a));
		ans=b[0];
		if(ans==2)
			a[0][2]=1;   
		for(i=1;i<l;i++)
		{
			if(ans>0)
				ans=m[ans][b[i]];
			else 
				ans=-1*m[abs(ans)][b[i]];
			if(ans==2)
				a[i][2]=1;
		}
		ans=1;
		for(i=0;i<l;i++)
		{
			if(a[i][2]==1)
			{
				ans=1;
				for(j=i+1;j<l;j++)
				{
					if(ans>0)
						ans=m[ans][b[j]];
					else 
						ans=-1*m[-1*ans][b[j]];
					if(ans==3)
						a[j][3]=1;
				}
			}
		}
		ans=1;
		flag=0;
		for(i=0;i<l;i++)
		{
			if(a[i][3]==1)
			{
				ans=1;
				for(j=i+1;j<l;j++)
				{
					if(ans>0)
						ans=m[ans][b[j]];
					else 
						ans=-1*m[-1*ans][b[j]];
				}
				if(ans==4)
				{
					flag=1;
					break;
				}
			}
 
		}
		if(flag==1)
			printf("Case #%lld: YES\n",k);
		else
			printf("Case #%lld: NO\n",k);
			k++;
	}
	return 0;
}