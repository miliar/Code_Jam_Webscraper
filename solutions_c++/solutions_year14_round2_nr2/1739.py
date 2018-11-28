#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
using namespace std;

#define STEP2

#ifdef STEP0
istream& fin = cin;
ostream& fout = cout;
#endif

#ifdef STEP1
ifstream fin ("B-sample.txt");
ostream& fout = cout;
#endif

#ifdef STEP2
ifstream fin ("B-small-attempt0.in");
ofstream fout ("B-small-attempt0.out");
#endif

#ifdef STEP3
ifstream fin ("B-large.in");
ofstream fout ("B-large.out");
#endif

int main()
{
	int T;
	
	fin >> T;
	for(int t=1; t<=T; t++)
	{
		int A, B, K;
		fin >> A >> B >> K;
		
		int rs = 0;
		for(int i=0; i<A; i++)
		{
			for(int j=0; j<B; j++)
			{
				int num = i & j;
				if(num < K)
				{
					rs++;
				}
			}
		}
		
		fout << "Case #" << t << ": ";
		fout << rs;
		fout << endl;
	}
	
	return 0;
}
