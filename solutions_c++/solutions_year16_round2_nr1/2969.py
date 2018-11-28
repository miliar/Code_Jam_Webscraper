//============================================================================
// Name        : PractiseBeastX11.cpp
// Author      : neo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <climits>
#include <stdlib.h>

using namespace std;

std::string ConvertDigits(std::string s)
{
	std::map<char,int> mymap;

	for(int i = 0; i < s.length(); ++i)
	{
		std::map<char,int>::iterator it;
		it = mymap.find(s[i]);
		if (it == mymap.end())
		{
			mymap[s[i]] = 1;
		}
		else
			mymap[s[i]] = mymap[s[i]] +1;

	}
	int A[10];
	for(int i = 0; i < 10 ; ++i)
		A[i] = 0;
	// Remove 0
	while (mymap['Z'] != 0)
	{

		A[0]  = A[0] + 1;
		mymap['Z'] = mymap['Z'] - 1;
		mymap['E'] = mymap['E'] - 1;
		mymap['O'] = mymap['O'] - 1;
		mymap['R'] = mymap['R'] - 1;

	}

	// Remove 0
	while (mymap['Z'] != 0)
	{

		A[0]  = A[0] + 1;
		mymap['Z'] = mymap['Z'] - 1;
		mymap['E'] = mymap['E'] - 1;
		mymap['O'] = mymap['O'] - 1;
		mymap['R'] = mymap['R'] - 1;

	}

	// Remove 2
	while (mymap['W'] != 0)
	{

		A[2]  = A[2] + 1;
		mymap['T'] = mymap['T'] - 1;
		mymap['W'] = mymap['W'] - 1;
		mymap['O'] = mymap['O'] - 1;

	}
	// Remove 6
	while (mymap['X'] != 0)
	{

		A[6]  = A[6] + 1;
		mymap['S'] = mymap['S'] - 1;
		mymap['I'] = mymap['I'] - 1;
		mymap['X'] = mymap['X'] - 1;

	}

	// Remove 8
		while (mymap['G'] != 0)
		{

			A[8]  = A[8] + 1;
			mymap['E'] = mymap['E'] - 1;
			mymap['I'] = mymap['I'] - 1;
			mymap['G'] = mymap['G'] - 1;
			mymap['H'] = mymap['H'] - 1;
			mymap['T'] = mymap['T'] - 1;

		}

	// Remove 4
			while (mymap['U'] != 0)
			{

				A[4]  = A[4] + 1;
				mymap['F'] = mymap['F'] - 1;
				mymap['O'] = mymap['O'] - 1;
				mymap['U'] = mymap['U'] - 1;
				mymap['R'] = mymap['R'] - 1;
			}
	// Remove 5
				while (mymap['F'] != 0)
				{

					A[5]  = A[5] + 1;
					mymap['F'] = mymap['F'] - 1;
					mymap['I'] = mymap['I'] - 1;
					mymap['V'] = mymap['V'] - 1;
					mymap['E'] = mymap['E'] - 1;
				}

	// Remove 1
				while (mymap['O'] != 0)
				{

					A[1]  = A[1] + 1;
					mymap['O'] = mymap['O'] - 1;
					mymap['N'] = mymap['N'] - 1;
					mymap['E'] = mymap['E'] - 1;
				}
	// Remove 3
	while (mymap['H'] != 0)
		{

			A[3]  = A[3] + 1;
			mymap['T'] = mymap['T'] - 1;
			mymap['H'] = mymap['H'] - 1;
			mymap['R'] = mymap['R'] - 1;
			mymap['E'] = mymap['E'] - 1;
			mymap['E'] = mymap['E'] - 1;

		}


	while (mymap['I'] != 0)
					{

						A[9]  = A[9] + 1;
						mymap['N'] = mymap['N'] - 1;
						mymap['I'] = mymap['I'] - 1;
						mymap['N'] = mymap['N'] - 1;
						mymap['E'] = mymap['E'] - 1;
					}
	while (mymap['V'] != 0)
					{

						A[7]  = A[7] + 1;
						mymap['S'] = mymap['S'] - 1;
						mymap['E'] = mymap['E'] - 1;
						mymap['V'] = mymap['V'] - 1;
						mymap['E'] = mymap['E'] - 1;
						mymap['N'] = mymap['N'] - 1;
					}

std::string  res= "";
for(int i = 0 ; i < 10 ; ++i)
{
	for(int j = 0; j < A[i]; ++j)
	{
		std::string s;
		std::stringstream out;
		out << i;
		s = out.str();
		res = res + s;
	}
}
return res;
}

char g[3000];
int main() {


	freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

    int T;
    int N;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {

		scanf("%s", g);

				std::string Orig = "";
				for(int  j =0; g[j] != '\0' ; ++j)
				{
				    	Orig = Orig + g[j];

				}
		//        std::cout << Orig << std::endl;

				//else
				{
					std::string res = ConvertDigits(Orig);
			        printf("Case #%d: %s\n", Ti, &res[0]);
			        fflush(stdout);
				}


	}
	 fflush(stdout);
	//int x = 0;
	//x++;

	//justcheck(0);
	//std::cout << " max counter we "  <<  we << std::endl;
	//justcheck(1);
	//std::cout << " max counter we "  <<  we << std::endl;
	//justcheck(2);
	//std::cout << " max counter we "  <<  we << std::endl;
	//justcheck(11);
	//std::cout << " max counter we "  <<  we << std::endl;
	//justcheck(1692);
	//std::cout << " max counter we "  <<  we << std::endl;

	//for(long long i = 0 ; i <= 1000000 ; ++i )
	//	justcheck(i, &maxval, &we);
	//std::cout << " max counter val "  <<  maxval << std::endl;
	//std::cout << " max counter we "  <<  we << std::endl;
	/*
	 int xdim; int ydim;
	   std::cin >>  xdim;
	   std::cin >>  ydim;
	   //scanf("give  the x dimension %d", &xdim);
	   //scanf("give  the y dimension %d", &ydim);
	   int ** A = new int*[xdim];
	   for(int i = 0; i < xdim; ++i)
	   A[i] = new int[ydim];


	   for(int i = 0; i < xdim; ++i)
	   {
	       std::cout << std::endl;
	   for(int j = 0; j < ydim; ++j)
	   {
	   A[i][j] = i*j;
	   std::cout << A[i][j] << " " ;
	   }
	   std::cout << std::endl;
	   }
	   return 0;
	   */
}
