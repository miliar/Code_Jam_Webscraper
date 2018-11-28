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
#define SZ 1000000
#define N 16
#define J 50
using namespace std;
typedef long long ll;
vector<int> pm;
bool f[SZ];
ll p[11][20];
int check(ll t)
{
	for(int i=0;i<pm.sz && pm[i]<t;i++)
	{
		if(t%pm[i]==0)return pm[i];
	}
	return -1;
}
int main()
{
	int t,i,j,k,cs,css,t1,t2;
	for(i=2;i<SZ;i++)
	{
		if(f[i]==0)
		{
			pm.PB(i);
			for(j=i+i;j<SZ;j+=i)f[j]=1;
		}
	}
	for(i=2;i<=10;i++)
	{
		p[i][0]=1;
		for(j=1;j<=16;j++)p[i][j]=p[i][j-1]*i;
	}
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cout<<"Case #"<<cs<<": \n";
		k=0;
		for(i=0;k<J;i++)
		{
			ll a[11];
			for(j=2;j<=10;j++)a[j]=p[j][N-1]+1;
			t=i;
			for(j=1;t>0;j++,t/=2)
			{
				if(t%2)
				{
					for(t1=2;t1<=10;t1++)a[t1]+=p[t1][j];
				}
			}
			int b[11];
			for(j=2;j<=10;j++)
			{
				b[j]=check(a[j]);
				if(b[j]<0)break;
			}
			if(j>10)
			{
				char s[20];
				for(j=0;a[2]>0;j++,a[2]/=2)s[j]='0'+a[2]%2;
				for(j--;j>=0;j--)cout<<s[j];
				cout<<" ";
				for(j=2;j<=10;j++)cout<<b[j]<<" ";
				cout<<endl;
				k++;
			}
		}
	}
	return 0;
}
