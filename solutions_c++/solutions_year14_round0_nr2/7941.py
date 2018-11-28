#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<iomanip>
using namespace std;

double solve(double, double,double);
double calculate(double,double);
int main(int argc,char *argv[])
{

	//std::istream &is = std::cin;
	//std::ostream &os = std::cout;
	std::ifstream ifs;
	std::ofstream ofs;
	vector<double> vecDouble;
	if(argc ==2)
	  {
	   ifs.open(argv[1],ios::in);	
	   ofs.open("OutputFile",ios::out);
	   }
	else
		{
		 //is = new istream(std::cin,)
		 //os  =&cout;
		}
	int T;
	double C,F,X;
	ifs >>T;
	while ( T--)
	{
		ifs >>C>>F>>X;
		vecDouble.push_back(solve(C,F,X));
	}
	//cout.precision(10);
	ofs<<std::fixed;
	for( int i=0 ; i !=vecDouble.size();i++)
	{
		//printf("Case #%d: %4.7f \n",i+1,vecDouble[i]);
		
		ofs<<"Case #"<<i+1<<": "<<setprecision(7)<<vecDouble[i]<<endl;
	}
}	


double solve(double C, double F, double X)
{
	double totalSec =0.0,amt=0.0;
	double div =2.0;
	double val1,val2;	
	if(X <C)
		return X/div;
	else
	{	
		while( amt != X)
		{
			val1 =calculate(X,div);
			val2 = calculate(C,div)+calculate(X,div+F);
			if(val2 <val1)
				{
				//cout<<" "<<val1<<" "<<val2<<endl;
				//cout<<"val1 "<<calculate(C,div)<<endl;
				totalSec +=calculate(C,div);
				div +=F;
				}
			else
			{
				totalSec += calculate(X,div);
				amt +=X;
			
			}
		}
	}
	return totalSec;
}

double calculate(double X,double F)
{
	return X/F;
}

