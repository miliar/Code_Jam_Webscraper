#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int numcase;
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++)
	{
		long long k,c,s;
		cin>>k>>c>>s;
		printf("Case #%d: ",ii);
		if(k=s)
		{
			for(int i = 1;i<=k;i++)
				cout<<i<<' ';
			cout<<endl;
		}
	}
}
