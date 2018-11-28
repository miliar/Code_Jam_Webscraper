#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip> 
using namespace std;

//istream& fin = cin;
//ifstream fin ("B-sample.txt");
//ifstream fin ("B-small-attempt0.in");
ifstream fin ("B-large.in");
//ofstream fout ("B-small-attempt0.out");
ofstream fout ("B-large.out");
//ostream& fout = cout;

int main()
{
	fout << fixed << setprecision(7);
	
	int N;
	double C, F, X;	

	fin >> N;
	for(int n=1; n<=N; n++)
	{
		fin >> C >> F >> X;
		
		double t = 0;
		double r = 2.0;		
		if(X <= C)
		{
			t = X / r;
		}
		else
		{
			while(true)
			{
				double t1 = X/r;
				double t2 = C/r + X/(r+F);
				if(t1 <= t2)
				{
					t += t1;
					break;
				}
				else
				{
					t += C/r;
					r += F;
				}
			}			
		}		
				
		fout << "Case #" << n << ": ";
		fout << t;
		fout << endl;
	}
	
	return 0;
}

