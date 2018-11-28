#include<iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream in ("D-small-attempt0.in");
	ofstream out ("output.txt");
	int n;
	in>>n;
	string line;
	for (int i = 1; i <= n; i++)
	{
		int K,C,S;
		in>>K>>C>>S;
		
		long long x = 1;
		for (int j = 0; j < C-1; j++)
		{
			x = x*K;
		}
		out<<"Case #"<<i<<": ";
		for (int j = 0; j < S; j++)
		{
			out<<j*x+1<<" ";
		}
		out<<'\n';
	}
	return 0;
}
//out<<"Case #"<<i<<": "<<number<<'\n';
