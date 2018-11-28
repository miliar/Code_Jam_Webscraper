#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	double c,f,x,r,t;
	int n,d=1;
	long long int z;
	cin>>n;
	while(n--)
	{
		cin>>c>>f>>x;
		r=2.0;
		t=0.0;
		if(x<c)
		t=(double)(x/r);
		else
		{
			while(((double)(c/r)+(double)(x/(r+f)))<(double)(x/r))
			{
			 t=(double)(c/r)+t;
			 r=r+f;
		    }
			 
			 t=(double)(x/r)+t;
			 
		}
		//z=t*10000000;
	    //t=z/10000000.0;
	    
		cout<<"Case #"<<setiosflags(ios::fixed | ios::showpoint)<<setprecision(7)<<d<<": "<<t<<"\n";
		d++;		
		
	}
	
	
}
