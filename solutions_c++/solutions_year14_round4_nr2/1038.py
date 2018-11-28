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
int a[1111];
struct data{
	int v;
	int p;
}d[1111];
bool cmp(data d1,data d2)
{
	return d1.v<d2.v;
}
int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		int i,n,j;
		int re=0;
		int l=0,r;
		cin>>n;
		r=n-1;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			d[i].v=a[i];
			d[i].p=i;
		}
		sort(d,d+n,cmp);
		for(i=0;i<n;i++)
		{
			if(d[i].p-l>=r-d[i].p)
			{
				re+=r-d[i].p;
				r--;
				for(j=i+1;j<n;j++)
				{
					if(d[j].p>d[i].p)
						d[j].p--;
				}
			}
			else
			{
				re+=d[i].p-l;
				l++;
				for(j=i+1;j<n;j++)
				{
					if(d[j].p<d[i].p)
						d[j].p++;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<re<<endl;
	}
	//system("pause");
    return 0;
}