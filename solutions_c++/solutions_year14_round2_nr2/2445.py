#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");

// convert from string to integer
int toInteger (string MyString)
{
	istringstream converter(MyString);
	int result;
	converter >> result;
	return result;
}

// convert from integer to string
string toString (int Number)
{
	ostringstream converter;
	converter << Number;
	return converter.str();
}

// ----------------------------------------

int lottery(int A, int B, int K)
{
	int n=0;
	for (int a=0; a<A; a++)
		for (int b=0; b<B; b++)
			for (int k=0; k<K; k++)
				if ((a&b)==k)
					n+=1;
	return n;
}

// ----------------------------------------

int main()
{
	int T=0;
	fin >> T;
	for (int t=1; t<=T; t++)
	{
		int A=0, B=0, K=0;
		fin >> A >> B >> K;
		fout << "Case #" << t << ": ";
		fout << lottery(A, B, K) << "\n";
	}

	system("PAUSE");
	return 0;
}