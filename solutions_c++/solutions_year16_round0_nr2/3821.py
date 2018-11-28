#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

//#define _DEBUG_
#ifdef _DEBUG_
#define fin cin
#define fout cout
#else
//ifstream fin("B-small-attempt1.in.txt");
//ofstream fout("B-small-attempt1.out.txt");
ifstream fin("B-large.in.txt");
ofstream fout("B-large.out.txt");
#endif

void flip(string& S, int n)
{
    int l = 0, h = n;
    while (l < h)
    {
	char tmp = S[h];
	S[h] = S[l] == '-' ? '+' : '-';
	S[l] = tmp == '-' ? '+' : '-';
	++l; --h;
    }
    if (l == h) S[h] = S[l] == '-' ? '+' : '-';
}

int main()
{
    int T;
    fin >> T;
    for (int c = 1; c <= T; ++c)
    {
	string S;
	fin >> S;
	fout << "Case #" << c << ": ";
	int cnt = 0;
	for (int i = S.size()-1; i >= 0; --i)
	{
	    // bottom cookie alr happy
	    if (S[i] == '+') continue;
	    // check top cookie
	    if (S[0] == '+')
	    {
		// find next cookie that happy, then flip
		for (int j = i-1; j >= 0; --j)
		{
		    if (S[j] == '+')
		    {
			flip(S, j);
			cnt++;
			break;
		    }
		}
	    }
	    flip(S, i);
	    cnt++;
	}
	fout << cnt << endl;
    }
}
