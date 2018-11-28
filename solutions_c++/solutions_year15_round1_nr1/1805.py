#include <bits/stdc++.h>
using namespace std;
int n,m,x,y;
int ar[100010];
void solve()
{
	int i,diff=0;
	cin>>n;
	for(i=1;i<=n;i++)
		cin>>ar[i];
	x=0;y=0;
	for(i=1;i<n;i++)
	{
		if(ar[i]>ar[i+1])
			x+=ar[i]-ar[i+1];
	}
	diff=0;
	for(i=2;i<=n;i++)
	{
		if(ar[i-1]>ar[i])
			diff=max(diff,ar[i-1]-ar[i]);
	}

	for(i=1;i<n;i++)
	{
		y+=min(diff,ar[i]);
	}
	return;
}

int main()
{
	int t,test;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		solve();
		cout<<"Case #"<<t<<": "<<x<<" "<<y<<endl;;
	}
	return 0;

}