/*
ID: anubhav6
PROG: packrec
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;
ifstream fin ("C-small-attempt1.in");
ofstream fout ("C-small-attempt1.out");


bool palindrome(string num)
{
	for(int i=0;i<num.size()/2;i++)
	{
		if(num[i]!=num[num.size()-i-1])
			return false;
	}
	return true;
}
int main()
{
	int T;
	fin>>T;
	double A,B;
	double root=0;
	stringstream convert;
	for(int i=0;i<T;i++)
	{
		fin>>A>>B;
		int count = 0;
		long root = (long)pow(A*1.0,0.5);
		double num = pow(root*1.0,2);
		while(num<=B)
		{
			
			convert.str("");
			convert<<root;
			if(palindrome(convert.str()))
			{
				if(num<A)
				{
					root++;
					num = pow(root*1.0,2);
					continue;
				}
				
				convert.str("");
				convert<<num;
				if(palindrome(convert.str()))
				{
					count++;
				}
			}
			//fout<<" "<< convert.str()<<endl;
			
			//fout<<root<<" "<<num <<" "<<convert.str()<<endl;
			root++;
			num = pow(root*1.0,2);
		}

		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}

}