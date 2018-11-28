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



using namespace std;



long long justcheck(long long N)
{


	bool* A  = new bool[10];
	for(int i =0; i <10 ; ++i)
		A[i]= false;
	long long counter = 1;
	long long val = N;
    int iter  = 1000;
	while(iter != 0)
	{
		long long t = val;
		while(t != 0)
		{
			 int d = t%10;
			 A[d] = true;
			 t = t/10;
		}
		bool checkover = true;
		for(int i =0; i <10 ; ++i)
				if(A[i] == false)
					checkover = false;

		if(checkover == true)
		{
			return val;
//			std::cout << "the counter is " << counter << std::endl;
//			std::cout << "the val is " << val << std::endl;
//			break;
		}

		val = (counter+1)*N;
		counter++;
		iter--;
	}
	return 0;
}

int main() {


	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;

	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		long long N;
		scanf("%lld", &N);


		if (N == 0)
		{
			    printf("Case #%d: %s\n", Ti, "INSOMNIA");
			    fflush(stdout);

		}
		else
		{
			long long res = justcheck(N);
	        printf("Case #%d: %lld\n", Ti, res);
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
