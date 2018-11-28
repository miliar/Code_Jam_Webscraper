/*
 * A.CPP
 *
 *  Created on: 13-Apr-2013
 *      Author: sandip
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <iomanip>


using namespace std;
void solution(ifstream &in ,ofstream &out);

int main()
{
	long long nTestCase = 0;

	ifstream in("C:\\Users\\Sandip\\Downloads\\B-large.in",ifstream::in);
	ofstream out("C:\\Users\\Sandip\\Downloads\\B-large.out",ofstream::out);

	string strTestCase;
	getline(in,strTestCase);
	nTestCase = atol(strTestCase.c_str());
	out.precision(10);
	for(int i=0; i< nTestCase; i++)
	{
		out<<"Case #"<<i+1<<": ";
		solution(in, out);
		out<<endl;
	}

	in.close();
	out.close();
	return 0;
}

void solution(ifstream &in, ofstream &out)
{
	double seconds=0;
	double C,X,F;
	in>>C;
	in>>F;
	in>>X;

	if(X<C)
		seconds = X/2;
	else
	{
		int numberoffarms=0;
		double farmSeconds = C/2;
		double tempSeconds = X/2;
		double dCookieRate = 2.0;
		double seconds1=0;
		while(1)
		{
			numberoffarms++;
			seconds1 += farmSeconds;
			dCookieRate += F;
			double totalseconds = X/dCookieRate;
			if((seconds1 + totalseconds) > tempSeconds)
			{
				break;
			}
			else
			{
				tempSeconds = seconds1 + totalseconds;
				farmSeconds = C/dCookieRate;
			}
		}
		seconds = tempSeconds;
	}
	out << seconds;

}
