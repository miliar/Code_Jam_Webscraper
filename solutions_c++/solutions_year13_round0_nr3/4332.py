#include<iostream>
using namespace std;
typedef long long LL;
#include<algorithm>

bool ispalin(LL a)
{
	LL rev=0,temp=a;
	while(temp)
	{
		rev = (rev<<3) + (rev<<1) + temp%10;
		temp/=10;
	}
	return rev==a;
}
int main()
{
	int t,tc=0;
	cin>>t;
	LL ans[1000];
	int in=0;
	for(LL i=1;i<=1e7;i++)
	{
		if(ispalin(i)&&ispalin(i*i))
		{
			ans[in++]=i*i;
		}
	}

	while(tc++,t--)
	{
		LL a,b;
		cin>>a>>b;
		int answer=lower_bound(ans,ans+in,b+1)-lower_bound(ans,ans+in,a);
		cout<<"Case #"<<tc<<": "<<answer<<endl;
	}
	return 0;

}
