#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
long long x[100];
int n;
int getmin(int ind,long long a)
{
	//cout<<ind<<" "<<a<<endl;
	if(ind==n) return 0;
	if(x[ind]<a) return getmin(ind+1,a+x[ind]);
	return min(n-ind,a==1?(1<<31)-1:1+getmin(ind,2*a-1));
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		long long a;
		cin>>a>>n;
		for(int i=0;i<n;i++) 
		{
			cin>>x[i];
		}
		int ret=0;
		sort(x,x+n);
		cout<<"Case #"<<tt<<": "<<getmin(0,a)<<"\n";
	}
	return 0;
}
