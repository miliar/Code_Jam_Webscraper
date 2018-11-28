#include<string.h>
#include<fstream>
#include<iomanip>
using namespace std;

void main()
{
	long double f , c, x , testCases, totaltime=0.0 , caseCount=0.0, produced=2.0 , check, init_time ;
	ifstream fin("B-large.in");
	ofstream fout("outputfile.txt");
	fin>>testCases;

	while(testCases>0)
	{
		caseCount++;
		fin>>c;
		fin>>f;
		fin>>x;

		init_time= x/2;
		int check1=init_time;

		
check_again:totaltime = totaltime + c/produced;
		if(check1<totaltime)
		{
			fout<<"Case #"<<caseCount<<": "<<setprecision(9)<<init_time<<endl;
		}
		else
		{

			produced = produced+f;
			
			check=x/produced;
			check=check + totaltime;
			if(check<init_time)
			{
				init_time = check;
				goto check_again;
			}	
				fout<<"Case #"<<caseCount<<": "<<setprecision(9)<<init_time<<endl;
		}
				totaltime=0;
				produced = 2;

				testCases--;
			
	}
}