#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include <iomanip>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<stack>
#include<cstring>
#include<map>
#include<set>
using namespace std;
#define MOD 1000000007
int a[777];
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		int re=0;
		int i,n,j,x,num,m;
		cin>>n>>m;
		for(i=1;i<=m;i++)
			a[i]=0;
		for(i=0;i<n;i++)
		{
			cin>>x;
			a[x]++;
		}
		for(i=m;i>0;i--)
		{
			if(i+i<=m)
			{
				if(a[i]%2==0)
				{
					re+=a[i]/2;
					a[i]=0;
					continue;
				}
				else
				{
					re+=a[i]/2;
					a[i]=1;
				}
			}
			num=a[i];
			a[i]=0;
			re+=num;
			for(j=i-1;j>0&&num>0;j--)
			{
				if(j+i>m)
					continue;
				if(a[j]==num)
				{
					a[j]=0;
					num=0;
				}
				else if(a[j]<num)
				{
					num-=a[j];
					a[j]=0;
				}
				else
				{
					a[j]-=num;
					num=0;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<re<<endl;
		/*sort(b,b+n);
		cout<<m<<endl;
		for(i=0;i<n;i++)
			cout<<b[i]<<' ';
		cout<<endl;
		for(i=0;i<n;i++)
			cout<<m-b[i]<<' ';
		cout<<endl;*/
	}
	//system("pause");
    return 0;
}