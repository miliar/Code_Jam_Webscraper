#include <iostream>
#include<cstdio>

using namespace std;

int main() {
	double t,c,f,x,prev,ans,ans1;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		ans=x/2.0;
		prev=c/2;
		int k=1;
		double var;
		while(1)
		{
			
			var=x/(k*f+2.0);
			ans1=prev+var;
			if(ans1>ans)
			break;
			else
			{
				ans=ans1;
				prev=prev+c/(k*f+2.0);
				k++;
			}
			
		}
		cout<<"Case #"<<i<<": ";
		printf("%0.7f\n",ans);
	}
	return 0;
}