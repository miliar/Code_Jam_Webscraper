// jam2013.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<math.h>
using namespace std;

string convert(int myLongDouble);
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in;
	ofstream out;
	int a,b;
	in.open("input.txt");
	out.open("output.txt");
	int t;
	in>>t;
	for(int i=1;i<=t;i++)
	{
		in>>a>>b;
		int count=0;
		for(int j=a;j<=b;j++)
		{
		  int ans=sqrt((float)j);
         string input=convert(j);
	     cout<<input<<endl;
	     if(input==string(input.rbegin(),input.rend()))
		 {
			 if((ans*ans)==j){
				 /*check if the sqrt is itself palindrome*/
				 string input=convert(ans);
				 if(input==string(input.rbegin(),input.rend()))
				     count++;
			 }
		 }
		}
		out<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}

string convert(int myLongDouble) {
    stringstream blah;
    blah << myLongDouble;

    return blah.str();
}

