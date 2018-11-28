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

float C, X, F;
int numT;
int i;
float ans=0.0;

void readfile()
{
	string line;
	getline(cin,line);
	stringstream tt;
	tt<<line;
	tt>>numT;
	//cout<<numT<<endl;
	tt.clear();
	for (int k=0; k<numT; k++)
	{
		getline(cin, line);
		tt<<line;
		tt>>C>>F>>X;
		tt.str("");
		tt.clear();
		//cout<<C<<" "<<F<<" "<<X<<endl;
		i= ceil((X/C)-(2/F)-1);
		if (i<0) i=0;
		if (i!=0)
		{
				for (int j=0; j<i; j++)
			{
				ans += (C/(2+j*F));
			}
		}
		ans += X/(2+i*F);
		cout<<"Case #"<<(k+1)<<": "<<ans<<endl;
		ans=0;
	}
}

int main()
{
	cout<<fixed;
	cout<<setprecision(8);
	//cout<<4.0/2.4;
	readfile();
	//cout<<4.01236<<endl;
	return 0;
}