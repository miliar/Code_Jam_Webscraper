#include<iostream>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<fstream>
using namespace std;

int T, i, j, k, tcase;
long double C, F, X, TOT, TEMP, RT;

ifstream in("B.in");
ofstream out("GCJ14QB.out");

int main()
{
	in>>T;
	for ( tcase = 1; tcase <= T; tcase++ )
	{
		in>>C>>F>>X;
		TOT = 0; RT = 2.0;
		while ( 1 )
		{
			if ( (C/RT) + (X/(RT+F)) < (X/RT) )
			{
				TOT += (C/RT);
				RT += F;
			}
			else
			{
				TOT += (X/RT);
				break;
			}
		}
		out<<"Case #"<<tcase<<": ";
		out<<fixed<<setprecision(7)<<TOT<<endl;
		
	}
	
	
	
	return 0;
}
