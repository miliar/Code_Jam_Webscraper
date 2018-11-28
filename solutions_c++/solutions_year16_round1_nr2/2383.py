#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int a[50][50];
int d[100][50];
int c[100];
int n,l;
int ans;
int sgt(int s1,int s2)
{
	int i,j,k;
	for(i=0;i<n;i++)
	{
		if(d[s1][i]>=d[s2][i])return 0;
	}
	return 1;
}
int gt(int s1,int s2)
{
	int i,j,k;
	for(i=0;i<n;i++)
	{
		if(d[s1][i]>d[s2][i])return 1;
		if(d[s1][i]<d[s2][i])return 0;
	}
	return 1;
}
int funn(int s)
{
	int i,j,k;
	if(s!=l-1)
	{
		for(i=s-1;i>=0;i--)
		{
			if(!c[i])break;
		}
		if((i>=0)&&(!sgt(i,s+1)))return 0;
	}
	for(i=s+1;i+1<l;i++)
	{
		if(!sgt(i,i+1))return 0;
	}
	for(i=0,k=0;i<l;i++)
	{
		if(c[i])
		{
//			cout<<i<<" ";
			for(j=0;j<n;j++)a[k][j]=d[i][j];
			k++;
		}
	}
//	cout<<endl;
	for(i=0,k=0;i<l;i++)
	{
		if(!c[i])
		{
			for(j=0;(j<n)&&(a[j][k]==d[i][j]);j++);
			if(j==n)k++;
			else
			{
				ans=k;
				break;
			}
		}
	}
	if(i==l)
	{
		ans=k;
		return 1;
	}
	ans=k;
	for(k++;i<l;i++)
	{
		if(!c[i])
		{
			for(j=0;(j<n)&&(a[j][k]==d[i][j]);j++);
			if(j==n)k++;
			else
			{
				return 0;
			}
		}
	}
	return 1;
}
int cmpt(int s1,int s2)
{
	if(!sgt(s1,s2))return 0;
	int i,j,k;
	if(s1+1<s2 && s1!=0)
	{
		for(i=s1-1;i>=0;i--)
		{
			if(!c[i])break;
		}
		if((i>=0)&&(!sgt(i,s1+1)))return 0;
	}
	for(i=s1+1;i+1<s2;i++)
	{
		if(!sgt(i,i+1))return 0;
	}
	return 1;
}
int fun(int s,int r)
{
	int i,j,k;
	c[s]=1;
	r--;
	if(r==0)
	{
		if(funn(s))return 1;
		c[s]=0;
		return 0;
	}
	for(i=s+1;(i<l)&&(i<(l-r+1));i++)
	{
		if(cmpt(s,i))
		{
			if(fun(i,r))return 1;
		}
	}
	c[s]=0;
	return 0;
}
void srt()
{
	int i,j,k;
	int tm;
	for(i=0;i<l;i++)
	{
		for(j=l-2;j>=i;j--)
		{
			if(gt(j,j+1))
			{
				for(k=0;k<n;k++)
				{
					tm=d[j][k];
					d[j][k]=d[j+1][k];
					d[j+1][k]=tm;
				}
			}
		}
	}
}
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>n;
		l=2*n-1;
		for(i=0;i<l;i++)
		{
			c[i]=0;
			for(j=0;j<n;j++)cin>>d[i][j];
		}
		srt();
//		for(i=0;i<l;i++)
//		{
//			for(j=0;j<n;j++)cout<<d[i][j];
//			cout<<endl;
//		}
//		cout<<fun(0,n)<<" "<<ans<<endl;
		for(i=0;i<n;i++)
		{
			if(fun(i,n))break;
		}
		cout<<"Case #"<<cs<<": ";
		for(i=0;i<n;i++)cout<<a[i][ans]<<" ";
		cout<<endl;
	}
	return 0;
}
