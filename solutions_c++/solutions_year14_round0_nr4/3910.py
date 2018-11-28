#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iterator>
#include <random>
#include <assert.h>
using namespace std;

const string file = "file";

const string infile = file + ".in";
const string outfile = file + ".out";

const int INF = 0x3f3f3f3f; 

//#define ONLINE_JUDGE

void readM(istream& fin, deque<double>& A, int N)
{
	for(int i = 0; i < N; i++)
	{
		fin >> A[i];
	}
	sort(A.begin(), A.end());
}

int main()
{
#ifdef ONLINE_JUDGE
	ostream &fout = cout;
	istream &fin = cin;
#else
	fstream fin(infile.c_str(), ios::in);
	fstream fout(outfile.c_str(), ios::out);
#endif	

	int T;
	fin >> T;
	for(int t = 0; t < T; t++)
	{
		int N;
		fin >> N;
		deque<double> A(N);
		deque<double> B(N);
		readM(fin, A, N);
		readM(fin, B, N);


		deque<double> C = A;
		deque<double> D = B;

		int scoreA = 0;
		int scoreB = 0;

		for(int i = 0; i < N; i++)
		{
			if(A.front() < B.front())
			{
				A.pop_front();
				B.pop_back();
				
			}
			else
			{
				A.pop_front();
				B.pop_front();
				scoreA++;
			}

			if(C.back() < D.back())
			{
				C.pop_back();
				D.pop_back();
			}
			else
			{
				C.pop_back();
				D.pop_front();
				scoreB++;
			}

		}


		fout << "Case #" << t + 1 << ": "
			 << scoreA << " " << scoreB
			 << "\n";
		
	}

#ifdef ONLINE_JUDGE
#else
    fout.close();
	fin.close();
#endif
}
