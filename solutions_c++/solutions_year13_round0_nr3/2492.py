#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
long long f[100000],T,t,n,a,b,ans;

bool palindrome(long long a)
{
	int m=0,b[20],i;
	while(a) b[++m]=a%10,a/=10;
	for(i=1;i<=m/2;i++) if(b[i]!=b[m-i+1]) return 0;
	return 1;
}

int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	for(long long i=1;i<=1e7;i++)
		if(palindrome(i)&&palindrome(i*i)) f[++n]=i*i;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>a>>b;
		ans=upper_bound(f+1,f+n+1,b)-lower_bound(f+1,f+n+1,a);
		cout<<"Case #"<<t<<": "<<ans<<endl;;
	}
}
