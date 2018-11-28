#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;

void main()
{
	int testCases; long double C, F, X, T, TT, R, Res, FinRes;
	ifstream infile; ofstream ofile;
	ofile.open("B_Large.txt");
	ofile.precision(8);
	infile.precision(8);
	infile.open("B-large.in");
	infile>>testCases;
	for(int i=0;i<testCases;i++)
	{
		R=2.0;
		infile>>C;
		infile>>F;
		infile>>X;
		T=X/R;
		TT=C/R;
		R=R+F;
		Res=TT+(X/R);
		FinRes=Res;
		if(Res>T)
		{	
			Res=T;
			FinRes=Res;
		}
		else
		while(Res<T)
		{
			if(FinRes>Res)
				FinRes=Res;
			T=Res;
		TT=TT+(C/R);
		R=R+F;
		Res=TT+(X/R);
		}
		ofile<<"Case #"<<i+1<<": "<<FinRes<<endl;
	}
	infile.close();
	ofile.close();
}