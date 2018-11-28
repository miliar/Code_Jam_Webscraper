#include<iostream>
#include<fstream>




using namespace std;

int main()
{
	freopen("B-large.in","r",stdin); 
	freopen("Problem_b_output.txt","w",stdout);
	long long t,p;
	cin>>t;
	for(p=1;p<=t;p++)
	{
		double c,f,x,count,rate,time;
		cin>>c>>f>>x;
		rate=2;
		count=0;
		time=0;
		
		while(count<x)
		{
			if((x/rate)<(c/rate)+(x/(rate+f)))
			{
			time=time+(x/rate);
			count=x;
		    }
			else
			{
			time=time+(c/rate);
			rate=rate+f;
			count=0;
		    }
		}
		
		cout<<"Case #"<<p<<": ";
		cout.setf(ios::fixed);
	    cout.precision(7);
		cout<<time<<endl;
		
		
	}
	
}
