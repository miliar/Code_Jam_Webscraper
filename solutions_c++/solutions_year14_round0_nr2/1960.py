#include "iostream"
#include "fstream"
#include "iomanip"
#include<conio.h>
using namespace std;
double remainingTime(double c,double r,double f)
{
	double time=0;
	int i;
	for(i=0;;i++)
	{
		time+=c/(r+i*f);
		if((c/(r+i*f))<1)
			break;
	}
	return time;
}
int main()
{
	int t,i,j,k,a,b,cnt,ans;
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin>>t;
    int cookies;
    long double time,rate,c,f,x;
    for(i=0;i<t;i++)
    {
    	fin>>c>>f>>x;
    	cookies=0;
    	time=0;
    	rate=2;
    	while(1)
    	{
    		if((c/rate+x/(rate+f))>=x/rate)
    		{
    			time+=(x)/rate;
    			break;
    		}else
    		{
    			time+=c/rate;
    			rate+=f;
    		}
    	}
    	fout<<"Case #"<<i+1<<": "<<std::fixed<<std::setprecision(7)<<time<<endl;
    }
    cout<<"ok";
    getch();
    
}
