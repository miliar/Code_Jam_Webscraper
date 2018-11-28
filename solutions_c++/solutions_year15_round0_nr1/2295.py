#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

int t, k, add, sum;
string s;

int main()
{
	ifstream infile("A-large.in");
    ofstream outfile;
    outfile.open("out.txt");
	infile >> t;
	for (int i = 1; i <= t; i++)
	{
		infile >> k >> s;
		sum = s[0]-'0'; add = 0;
		for (int j = 1; j <= k; j++)
		{
			if(s[j]-'0'> 0 && sum < j) {add+=j-sum; sum=j+s[j]-'0';}
			else sum+=s[j]-'0';
		}
		outfile << "Case #" << i << ": " << add << endl;
	}
}