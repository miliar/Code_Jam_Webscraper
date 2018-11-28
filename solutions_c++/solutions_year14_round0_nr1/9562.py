#include <cstdio>
#include <string>
#include <iostream>
#include <errno.h>
#include <string.h>
#include <cstdlib>
#include <locale>
#include <functional>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <math.h>
#include <sstream>

using namespace std;

int first, second;
int array1[4];
int array2[4];
int numT;
int x=0, y;

int searcharrays()
{
	for (int i=0; i<4; i++)
	{
		for (int j=0; j<4; j++)
		{
			if (array1[i]==array2[j])
			{
				x++;
				y= array1[i];
			}
		}
	}
	return x;
}

void readfile()
{
	string line;
	getline(cin,line);
	stringstream tt;
	tt<<line;
	tt>>numT;
	tt.clear();
	for (int i=0; i<numT; i++)
	{
		getline(cin, line);
		tt<<line;
		tt>>first;
		tt.str("");
		tt.clear();
		for (int j=0; j<first; j++)
			{getline(cin, line);}
		tt<<line;
		tt>>array1[0]>>array1[1]>>array1[2]>>array1[3];
		tt.str("");
		tt.clear();
		for (int j=0; j<(4-first); j++)
			{getline(cin, line);}

		getline(cin, line);
		tt<<line;
		tt>>second;
		tt.str("");
		tt.clear();
		for (int j=0; j<second; j++)
			{getline(cin, line);}
		tt<<line;
		tt>>array2[0]>>array2[1]>>array2[2]>>array2[3];
		tt.clear();
		tt.str("");
		for (int j=0; j<(4-second); j++)
			{getline(cin, line);}

		if (searcharrays()==1)
			{cout<<"Case #"<<(i+1)<<": "<<y<<endl;}
		else if (searcharrays()==0)
			{cout<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;}
		else if (searcharrays()>1)
			{cout<<"Case #"<<(i+1)<<": Bad magician!"<<endl;}

		x=0;
	}
}

int main()
{
	readfile();
	return 0;
}