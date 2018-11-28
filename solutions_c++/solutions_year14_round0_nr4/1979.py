#include<iostream>
#include<cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int t,n;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	cin>>t;
	for(int g=0;g<t;g++)
	{
		cout<<"case #"<<g+1<<": ";
		cin>>n;
		double *q,*p;
		q=new double [n];
		p=new double [n];
		for(int i=0;i<n;i++)
		{
			cin>>p[i];
		}
		for(int i=0;i<n;i++)
		{
			cin>>q[i];
		}
		sort(p,p+n);
		sort(q,q+n);
		int j=n-1;
		int cnt=0;
		for(int i=n-1;i>=0;i--)
		{
			if(q[i]>p[j])cnt++;
			else j--;
		}
		j=n-1;
		int cnt1=0;
		for(int i=n-1;i>=0;i--)
		{
			if(p[i]>q[j])cnt1++;
			else j--;
		}
		cout<<n-cnt<<" "<<cnt1<<endl;
	}
	return 0;
}