#include <fstream>
#include <iomanip>
#include <ios>
using namespace std;

struct cases
{
	long double C;
	long double F;
	long double X;
	long double time;
};

void main()
{
	int noOfCases;
	long double smallest, temp;
	long double var;
	ifstream fin("B-small-attempt0.in");
	ofstream fout("CookieClicker.txt");
	fin>>noOfCases;
	cases *c=new cases[noOfCases];
	for(int i=0; i<noOfCases; i++)
	{
		fin>>c[i].C;
		fin>>c[i].F;
		fin>>c[i].X;
		smallest=c[i].X/2;
		bool flag=true;
		int counter=1;
		while(flag)
		{
			temp=c[i].C/2;
			for(int j=1; j<counter; j++)
				temp=temp+c[i].C/(2+c[i].F*j);

			temp=temp+c[i].X/(2+c[i].F*counter);
			
			counter++;
			if(temp<smallest)
			{
				smallest=temp;
				flag=true;
			}
			else
				flag=false;
		}
		fout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<smallest<<endl;

	}
	
}