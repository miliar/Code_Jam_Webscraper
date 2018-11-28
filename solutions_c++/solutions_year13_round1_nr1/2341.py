#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int main()
{
	int T=0,i;
	float r,t;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		int ans = 0,inc = 2;
		float sum = 0;
		//scanf("%%d",&r,&t);
		cin>>r>>t;
		t = t;
		sum = pow(r+1,2)-pow(r,2);
		while(sum<=t)
		{
			sum = sum + pow(r+inc+1,2)-pow(r+inc,2);
			ans++;
			inc+=2;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;

	}
	return 0;
}