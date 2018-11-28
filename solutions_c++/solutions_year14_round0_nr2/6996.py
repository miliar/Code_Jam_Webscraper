#include<iostream>
#include <iomanip>

using namespace std;


double calc(double c, double f, double x)
{
	double r=2;
	double sec=0;
	if (x/r<c/r)
	{
		sec=x/r;
	}
	else
	{
		while(x/r > (c/(r)+x/(r+f)))
		{
		sec+=c/r;
		r+=f;
		}
		sec+=x/r;
	}
	
	return sec;
}



int main ()
{
	 freopen("B-large.in","r",stdin);
     freopen("solution.out","w",stdout); 


	int t;
	cin>>t;
	double c,f,x;
	
	for(int i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		cout<<"Case #"<<i<<": "<<std::fixed << std::setprecision(7)<<calc(c,f,x)<<endl;
	}
	return 0;
}