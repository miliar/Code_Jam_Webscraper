#include <bits/stdc++.h>
using namespace std;
int a[1005];
int main(int argc, char const *argv[])
{
	int T,Smax;
	char ch;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		int sumtilli=0,frdcount=0,frdcounttemp=0;
		cin>>Smax;
		for (int i = 0; i < Smax+1; ++i)
		{
			cin>>ch;
			a[i]=ch-'0';
		}
		for (int i = 0; i < Smax+1; ++i)
		{
			if(a[i]>0 && sumtilli<i)
			{
				frdcounttemp=(i-sumtilli);
				sumtilli+=frdcounttemp;
				frdcount+=frdcounttemp;
			}
			sumtilli+=a[i];
		}
		printf("Case #%d: %d\n",t+1,frdcount);
	}	
	return 0;
}