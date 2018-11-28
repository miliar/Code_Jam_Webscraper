#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 1001
int f(int a[MAX+1], int n)
{
	int count=0;
	int u=a[0],i;
	if(a[0]==0)
		count = u =1;
	for(i=1;i<=n;i++)
	{
		if(u < i)
		{
			count += i-u;
			u =i+a[i];
		}
		else
			u+=a[i];
	}
	return count;
}
int main()
{
	int t,s,i,x,a[MAX+1],j,ans;
	cin>>t;
	string str;
	for(j=1;j<=t;j++)
	{
		cin>>s;
		cin>>str;
		for(i=0;i<=s;i++)
			a[i] = int(str[i]-48);
		ans = f(a,s);
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
}
