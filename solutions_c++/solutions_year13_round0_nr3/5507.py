// FairAndSquare.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

bool IsPol(int num)
{
	string str,rev;
	stringstream stream;
	stream << num;
	str = stream.str();
	rev.insert(rev.begin(),str.rbegin(),str.rend());
	return (str==rev)?true:false;	
}

int _tmain(int argc, _TCHAR* argv[])
{
	int qnt(0);
	//string qnt;
	ifstream myReadFile;
	myReadFile.open("D:/Downloads/C-small-attempt0.in");
	//myReadFile.open("D:/Sources/GoogleCodeJam/qualification/FairAndSquare/input.txt");
	ofstream fout;
	fout.open("D:/Sources/GoogleCodeJam/qualification/FairAndSquare/output.txt");

	if (myReadFile.is_open()) {		
		myReadFile >> qnt;
		for(int i=0;i<qnt;i++)
		{				
			int b,e,res(0);
			myReadFile >> b;
			myReadFile >> e;
			for(int j=b;j<=e;j++)
			{
				if(IsPol(j))
				{
					int sqrt_j(static_cast<int>(sqrt((float)j)));
					if(sqrt_j*sqrt_j!=j)
					{
						continue;
					}
					if(IsPol(sqrt_j))
					{
						res++;
					}
				}
			}
			fout << "Case #"<< i+1 <<": "<< res << endl;
		}
	}
	return 0;
}

