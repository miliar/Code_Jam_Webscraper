#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <stdio.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin( "c:\\B-large.in" );
	//ofstream fout( "c:\\output.txt" , ios_base::out | ios_base::trunc);
	FILE * pFile;
	pFile = fopen ("c:\\output.txt","w");
	string temp1, temp2;
	istringstream stream1;
	string temp;
	fin>>temp;
	stream1.str(temp);
	int times;
	stream1>>times;
	string stc;
	getline(fin, stc);
	stream1.clear();
	for(int i=0; i<times; ++i)
	{
		getline(fin, stc);
		stream1.clear();
		stream1.str(stc);
		double c, f, x;
		double speed=2.0;
		stream1>>c>>f>>x;

		double clickToEnd = x/speed;
		double buyFarm = c/speed;
		double buySpendTime = buyFarm;
		speed+=f;
		double newClickToEnd = x/speed;
		double afterBuyToEnd = newClickToEnd+buyFarm;
		while(clickToEnd > afterBuyToEnd)
		{
			clickToEnd = buySpendTime+x/speed;
			buyFarm = c/speed;		
			buySpendTime+=buyFarm;
			speed+=f;
			newClickToEnd = x/speed;
			afterBuyToEnd=buySpendTime+newClickToEnd;			
			//printf("case %d :%.7f %.7f\n", i, clickToEnd, afterBuyToEnd);
		}
		//printf("case %d :%.7f %.7f\n", i, clickToEnd, afterBuyToEnd);
		//fout.precision(7);
		//fout.setf( std::ios::fixed, std:: ios::floatfield );
		//fout<<"Case #"<<i+1<<": "<<clickToEnd<<endl;
		fprintf (pFile, "Case #%d: %.7f\n",i+1, clickToEnd);
	}
	//system("pause");
	return 0;
}

