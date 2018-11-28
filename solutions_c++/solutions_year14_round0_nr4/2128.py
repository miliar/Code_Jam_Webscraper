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
double a[1111];
double b[1111];
int main()
{
	int t,T;
	int i,j,n;
	int count;
	int re;
	freopen("D-large.in","rt",stdin);
	freopen("D.out","wt",stdout);
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n;
		count=0;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		i=n-1;j=n-1;
		for(;i>=0;i--)
		{
			while(j>=0)
			{
				if(a[i]>b[j])
				{
					count++;
					j--;
					break;
				}
				else
				{
					j--;
				}
			}
		}
		re=0;
		i=n-1;j=n-1;
		for(;i>=0;i--)
		{
			while(j>=0)
			{
				if(b[i]>a[j])
				{
					re++;
					j--;
					break;
				}
				else
				{
					j--;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<count<<" "<<n-re<<endl;
	}
    return 0;
}