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




void readMatrix(istream & fin, vector<vector<int> >& A, int N)
{
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < N; j++)
		{
			fin >> A[i][j];
		}
	}
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
		int N, M;
		
		vector<vector<int> > A(4, vector<int>(4, 0));
		vector<vector<int> > B(4, vector<int>(4, 0));

		fin >> N;
		readMatrix(fin, A, 4);
		fin >> M;
		readMatrix(fin, B, 4);

		N--;
		M--;

		vector<int> row1 = A[N];
		vector<int> row2 = B[M];
		int lValue = -1;
		int count = 0;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(row1[i] == row2[j])
				{
					count++;
					lValue = row1[i];
				}
			}
		}

		fout << "Case #" << t + 1 << ": ";
		if(count == 1)
		{
			fout << lValue;
		}
		else if(count == 0)
		{
			fout << "Volunteer cheated!";
		}
		else
		{
			fout << "Bad magician!";
		}
		fout << "\n";
	}

#ifdef ONLINE_JUDGE
#else
    fout.close();
	fin.close();
#endif
}
