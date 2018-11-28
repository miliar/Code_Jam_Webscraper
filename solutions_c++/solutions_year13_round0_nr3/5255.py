#include<iostream>
#include "math.h"
#include <stdio.h>
using namespace std;
bool symm(long long m)
{
	long long temp = m,n=0;
	while (temp)
	{
		n = n*10+temp%10;
		temp = temp/10;
	}
	return (m == n);
}
int main()
{
	int  n;long long a,b,ans;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>n;
	for(int t=1;t<=n;t++)
	{
		ans = 0;
		cin>>a>>b;
		for(int i=1;i*i<=b;i++)
		{
			if(symm(i)&& i*i>=a)
			{
				if(symm(i*i))
					ans++;
			}
		}
		
		cout<<"Case #"<<t<<": "<<ans<<endl;		
	}
	
	return 0;
}
