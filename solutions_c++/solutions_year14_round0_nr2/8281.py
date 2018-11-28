#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

double myAlgo(double c, double f, double x)
{
	double time_spent=0;
	double rate=2;
	double time_1,time_2;

	//we have to calculate two time intervals
	for( ; ;)
	{
		time_1 = time_spent+x/rate;
		time_2 = time_spent+ c/rate + x/(rate+f);

		if(time_2 < time_1)
		{
			time_spent+=c/rate;
			rate+=f;
		}
		else 
		{
			time_spent=time_1;
			return time_spent;
		}
	}
	return -1;
}


double akash(double c,double f, double x)
{
	double prev_ans=0,ans=0;
	double k=2;
	while(prev_ans >= ans)
	{
		
		prev_ans=ans;
		k+=2;
		ans=x/k+c/k;
		
	}
	return k;
}
		

int main()
{
	ofstream outfile("output.txt");
	ifstream infile("input.txt");
	if(!infile)
		{
			cout<<"Could not open file for input...";
			return -1;
	}
	int n_cases;
	infile>>n_cases;

	double c,f,x;
	for(int n=1; n<=n_cases; n++)
	{
		infile>>c>>f>>x;
		outfile<<setprecision(9)<<"Case #"<<n<<": "<<myAlgo(c,f,x)<<endl;
		//break;
	}
	return 1;
}
