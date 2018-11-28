/*
 * template.cpp
 *
 *  Created on: 10-Apr-2013
 *      Author: sandip
 */

#include <iostream>
#include <vector>
#include <unistd.h>
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

	string strPath = "/home/sandip/Downloads/";
	string strInput = strPath + "A-small-attempt1.in";
	string strOutput = strPath + "A-small-attempt1.out";

	ifstream in(strInput.c_str(),ifstream::in);
	ofstream out(strOutput.c_str(),ofstream::out);

	string strTestCase;
	getline(in,strTestCase);
	nTestCase = atoll(strTestCase.c_str());

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
	unsigned long long r ,t;
	in>>r;
	in>>t;
	unsigned long long tpaint =0;
	unsigned long long count = 0;
	unsigned long long radius = r+1;
	while(1)
	{
		unsigned long long temp = ((radius)*radius)-((radius-1)*(radius-1));
		if(t>=temp)
			count++;
		else
			break;

		tpaint+=temp;
		radius += 2;
		t=t-temp;
	}
	cout<<count<<endl;
	out<<count;
}




