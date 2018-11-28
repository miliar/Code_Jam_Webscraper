#include <iostream>
#include <string>
#include <stdio.h>
#include <conio.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <numeric>


using namespace std;
using std::vector;


int main()
{
ifstream cin("A-small-attempt0.in");
ofstream cout("out.txt");
int T,sum;
string S;
cin >> T;

for(int i = 0; i < T; i++)
{
	int Smax;
	vector<int> digits;
	cin >> Smax ;
	cin >> S;
	int Required = 0;
	char a = S.at(0);
	int clapping = a - '0';
	
	for ( int ii = 1; ii < S.size(); ii++)
	{
	
		if((ii > clapping )& (S.at(ii)!='0'))
		{
	
			Required = Required + (ii - clapping);
	
			char temp = S.at(ii);
			int num = temp - '0';
	
			clapping += (num+Required);

		}
		else
		{
			char temp = S.at(ii);
			int num = temp - '0';
			clapping+=num;
		}
	
	}

		cout <<"Case #"<<i+1<<": "<<Required<<endl;

}
}