#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double ans = x/2;
		double curr = 2;
		double temp = 0;
		while(x/curr+temp<=ans)
		{
			ans = x/curr+temp;
			temp += c/curr;
			curr+=f;
		}
		printf("Case #%d: %.7f\n",i,ans);
	}
	return 0;
}

