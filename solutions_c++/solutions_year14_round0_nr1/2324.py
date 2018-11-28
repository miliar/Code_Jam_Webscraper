#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<stack>
#include<cstring>
#include<map>
#include<set>
using namespace std;
#define MOD 1000000007
int x[6][6];
int y[6][6];
int main()
{
	int i,j,a[22],b[22];
	int n,m;
	int t,T;
	int re;
	int count=0;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A.out","wt",stdout);
	cin>>T;
	for(t=1;t<=T;t++)
	{
		count=0;
		for(i=0;i<=16;i++)
			a[i]=b[i]=0;
		cin>>n;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				cin>>x[i][j];
				if(i==n-1)
					a[x[i][j]]++;
			}
		cin>>m;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				cin>>y[i][j];
				if(i==m-1)
					b[y[i][j]]++;
			}
		for(i=1;i<=16;i++)
			if(a[i]&&b[i])
			{
				count++;
				re=i;
			}
		if(count==1)
		{
			cout<<"Case #"<<t<<": "<<re<<endl;
		}
		else if(count==0)
		{
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		}
		else
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
	}
    return 0;
}