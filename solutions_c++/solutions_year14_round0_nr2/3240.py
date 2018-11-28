#include<iostream>
#include<fstream>
#include<iomanip>
double tim;
double last_rate,new_rate,last_time;
int method(double C,double F,double X)
{
	new_rate=last_rate+F;
	if( (C/last_rate + X/new_rate - last_time) <0)
	{
		//new_rate=last_rate+F;
			
		tim=tim-last_time+C/last_rate+X/new_rate;
		last_rate=new_rate;
		last_time=X/new_rate;
		return -1;
	}
	else 
	{
		return 0;
	}
}
		
using namespace std;
int main()
{
	int t;
	double C,F,X;
	ifstream fin ("b_.in");
	ofstream fout ("b_3.out");
	fin>>t;
	for(int cas=0;cas<t;cas++)
	{
		//scanf("%f",&C);
		//scanf("%f",&F);
		//scanf("%f",&X);
		fin>>C;
		fin>>F;
		fin>>X;	
		last_rate=2.0000000;
		tim=X/last_rate;
		last_time=X/2.0000000;
		while(1)
		{
			if(method(C,F,X)<0)
			{
				continue;
			}
			else
			{
				break;
			}
		}
		//printf("Case #%d: %f\n",cas+1,tim);
		fout<<"Case #"<<cas+1<<": "<<fixed<<setprecision(7)<<tim<<endl;
	}
	return 0;
}

