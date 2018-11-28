#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <vector>

using namespace std;

//#define _DEBUG_
#ifdef _DEBUG_
#define fin cin
#define fout cout
#else
ifstream fin("D-small-attempt0.in.txt");
ofstream fout("D-small-attempt0.out.txt");
//ifstream fin("B-large.in.txt");
//ofstream fout("B-large.out.txt");
#endif

typedef unsigned long long ULL;

int main()
{
    int T;
    fin >> T;
    for (int c = 1; c <= T; ++c)
    {
	int K, C, S;
	fin >> K >> C >> S;
	fout << "Case #" << c << ":";
	for (int i = 1; i <= K; ++i)
	{
	    fout << " " << i;
	}
	fout << endl;
    }
    return 0;
}
