#include<iostream>
#include<cstring>
#include<stack>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<set>
using namespace std;
double a[1002],b[1002];
int n;
void work()
{
	int i,j,k;
	int l,r,t;
	int ans1,ans2;
	int f;
	bool flag;
	set<double> wjj;
	cin>>n;
	ans1=0;
	ans2=0;
	for (i=0;i<n;i++)
		cin>>a[i];
	for (j=0;j<n;j++)
	{
		cin>>b[j];
		wjj.insert(b[j]);
	}
	sort(a,a+n);
	sort(b,b+n);
	for (f=0,t=n-1,i=n-1;i>=0;--i)
	{
		if (a[t]>b[i])
		{
			t--;
			ans1++;
		}
		else
		{
			f++;
		}
	}
	cout<<ans1<<" ";
	for (i=0;i<n;i++)
	{
		if (wjj.upper_bound(a[i])!=wjj.end())
		{
			wjj.erase(wjj.upper_bound(a[i]));
		}
		else
		{
			wjj.erase(wjj.begin());
			ans2++;
		}
	}
	cout<<ans2<<endl;
	return ;
}
int main()
{
	int cas;
	int T;
	freopen("d1.in","r",stdin);
	freopen("d1.out","w",stdout);	
	cas=0;
	cin>>T;
	while (T--)
	{
		cas++;
		cout<<"Case #"<<cas<<": ";
		work();
	}
	return 0;
}
