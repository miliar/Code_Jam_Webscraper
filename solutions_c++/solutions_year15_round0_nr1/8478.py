// Problem A. Standing Ovation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int t,iterator,iterator2;
	char arr[1001];
	int before,count,size;
	ifstream ifile("sample.in");
    ofstream ofile("sample.out");

	ifile>>t;
//	scanf("%d",&t);
	iterator2=0;
	while(iterator2<t)
	{
		//scanf("%d",&size);
			ifile>>size;
			ifile>>arr;
		before=arr[0]-'0';
		count=0;
		for(iterator=1;iterator<=size;iterator++)
		{
			if((arr[iterator]-'0')!=0 && iterator > before)
			{
				count+=iterator-before;
				before+=iterator-before;
			}
			before+=(arr[iterator]-'0');
		}

		ofile<<"Case #"<<iterator2+1<<": "<<count<<endl;
		iterator2++;
	}
	    ifile.close();
    ofile.close();

	return 0;
}

