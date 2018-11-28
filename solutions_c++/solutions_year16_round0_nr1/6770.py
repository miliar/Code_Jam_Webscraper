// pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

typedef unsigned long USLONG;

inline void update(vector<bool>& b, USLONG ans)
{
	for(; ans > 0; ans/=10) { b[ans%10] = true; }
}

inline bool check(const vector<bool>& b)
{
	for(short i = 0; i < 10; i++)
	{
		if(!b[i]) { return true; }
	}
	return false;
}

//#define fin cin
//#define fout cout

//int main(int argc, char **argv)
int main()
{
	USLONG T = 0, N = 0, i = 0, ans = 0;
	vector<bool> b(10);
	#ifndef fin
	ifstream fin("Input.txt");
	ofstream fout("Output.txt");
	#endif
	
	fin >> T;
	for(USLONG j = 1 ; j <= T; j++)
	{
		fin >> N;
		if(N == 0)
		{
			fout << "Case #" << j << ": " << "INSOMNIA" << "\n";
			continue;
		}
		b.clear();
		b.resize(10);
		i = 1;
		do
		{
			ans = i*N;
			update(b, ans);
			i++;
			if(i == (USLONG)(-1))
			{
				fout << "Case #" << j << ": " << "INSOMNIA" << "\n";
				break;
			}
		}while(check(b));
	
		fout << "Case #" << j << ": " << ans << "\n";
	}
	return 0;
}
