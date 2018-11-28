#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>
using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");
int main()
{
	int N;
	fin>>N;
	int T = 0;
	fout.precision(7);
	while(T < N)
	{
		long double C,F,X;
		fin>>C>>F>>X;
		long double fF = 2.0;
		
		long double sum = 0.0;
		while(1)
		{
			long double t = X/fF;
			long double tB = C/fF;
		
			if(t > tB+(X/(fF+F)))
			{
					
				sum += C/fF;
				fF += F;
				//cout<<std::fixed<<tt[i]<<" ";
				//i++;
			}
			else
			{
				sum += t;
				break;
			}
			
		}
		fout<<"Case #"<<T+1<<": "<<std::fixed<<sum<<endl;
		T++;
	}
}
