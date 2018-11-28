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


using namespace std;

std::string OrderString(std::string Orig)
{
	std::string res = "";
	res  = res + Orig.at(0);
	for(int i = 1; i < Orig.size() ; ++i)
	{
		if(res[0] <= Orig[i])
			res = Orig[i] + res;
		else
			res = res + Orig[i];
	}
	return res;
}

const int N = 10000;

char g[N];
int main() {


	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;

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
			std::string res = OrderString(Orig);
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
