#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int i,j,s,l=0,test;
	double c,f,x,rate=2,curr=0,ans=0.000000,diff,first,second;
	double sta=0.0000001;
	cin>>test;
	while(test--)
	{
		++l;
		rate=2;
       ans=0.0000000;
		cin>>c>>f>>x;
		while(1)
		{
			first=x/rate;
			second=(c/(rate))+(x/(rate+f));
			diff=first-second;
			if(diff>sta)
			{
				ans=ans+(c/rate);
				rate=rate+f;
			}
			else
			{
				ans=ans+(x/rate);
				break;
			}
			//cout<<ans<<"\n";
		}
		//cout<<"Case #"<<l<<": "<<ans<<"\n";
printf("Case #%d: %.7f\n",l,ans);

	}
	return 0;
	
}