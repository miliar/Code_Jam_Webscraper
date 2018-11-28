#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double rate= 2.0;
		double time=0.0;
		while(1)
		{
		    double a = (x/rate);
			double b = (c/rate)+ (x/(rate+f));
			//cout<<a<<" "<<b<<endl;
		    //cout<<a<<endl;
		    if(a-b<10e-64)
		      break;
			double temp_time = c/rate;
			rate = rate + f;
			time += temp_time;			
		}
		time +=  (x/rate);
		cout<<"Case #"<<i<<": ";
		printf("%.6f\n",time);
	}
}
