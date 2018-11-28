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
ifstream cin("A-small-attempt4.in");
ofstream cout("out.txt");
int T,sum;
vector<int> digits;
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
	//	cout <<"ii : "<<ii<<endl;
		if((ii > clapping )& (S.at(ii)!='0'))
		{
	//		cout<< "-in loop- "<< ii-clapping<< "  ";
			Required = Required + (ii - clapping);
	//		cout <<" required:" <<Required;
			char temp = S.at(ii);
			int num = temp - '0';
	//		cout<< " num : " <<num;
			clapping += (num+Required);
	//		cout <<" clapping_now:"<<clapping<<endl;
		}
		else
		{
			char temp = S.at(ii);
			int num = temp - '0';
			clapping+=num;
		}
	
	}
	//cout<<"  required :"<<Required<<endl;
		cout <<"Case #"<<i+1<<": "<<Required<<endl;

}
}