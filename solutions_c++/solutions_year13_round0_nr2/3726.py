// GCJ13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
using namespace std;

inline char charToInt( char ch ) {
  return (ch - '0');
}

int main()
{
	  ifstream in("B-large.in" );      // A-tiny-practice.in    // A-small-practice.in    // A-large-practice.in
	  ofstream outfile("B-large.out");
	  string line;
	  int tc; 
	  cin >> tc;
	  for(int tci = 0; tci < tc; tci++)
	  {
		char rows[100] = {0};
		char cols[100] = {0};
		char lawn[100][100];
		int n = 0;
		int m = 0;
		int dump = 0;
		cin >> n;
		cin >> m;		
		for(int ri = 0; ri < n; ri++)
		{
			
			for(int ci = 0; ci < m; ci++)
			{
				int h = 0;
				cin >> h;
				lawn[ri][ci] = h;
				if(rows[ri] < h) rows[ri] = h;
				if(cols[ci] < h) cols[ci] = h;
			}
		}		

		//analyze
		bool isPatternOK = true;
		for(int ri = 0; ri < n; ri++)
		{
			for(int ci = 0; ci < m; ci++)
			{
				int h = lawn[ri][ci];
				if(rows[ri] > h && cols[ci] > h)
				{
					cout<<"Case #"<<tci+1<<": NO"<<endl;
					ri=n;
					ci=m;
					isPatternOK = false;
				}
			}
		}
		if(isPatternOK)
			cout<<"Case #"<<tci+1<<": YES"<<endl;	
  }
}

