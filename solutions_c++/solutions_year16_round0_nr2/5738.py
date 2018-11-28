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



int MinMoves(vector<int>& list)
{
	int moves = 0;
	while(list.size() != 0)
	{
		while(list[list.size()-1] == 1)
			list.pop_back();

		if(list.size() == 0)
			return moves;

		if(list[0] == 0)
		{
			std::reverse(list.begin(),list.end());
			for(int i = 0 ; i < list.size() ; ++i)
			{
				if(list[i] == 0)
					list[i] = 1;
				else
					list[i] = 0;
			}
			moves++;
		}
		else
		{
			int endindex = 0;
			while(endindex < list.size() && list[endindex] == 1)
			{
	                    list[endindex] = 0;
						endindex++;
			}
			moves++;
			if(endindex == list.size())
				std::cout << "ERROR" << std::endl;

			std::reverse(list.begin(),list.end());
			for(int i = 0 ; i < list.size() ; ++i)
			{
				if(list[i] == 0)
					list[i] = 1;
				else
					list[i] = 0;
			}
			moves++;



		}


	}



}

const int MAXSIZE = 100000;

char g[MAXSIZE];
int main() {
      /*
	  int myints1[] = {0};
	  std::vector<int> test1 (myints1, myints1 + sizeof(myints1) / sizeof(int) );

	  std::cout << " The test value is "  << MinMoves(test1) << std::endl;


	  int myints2[] = {0,1};
	  std::vector<int> test2 (myints2, myints2 + sizeof(myints2) / sizeof(int) );

	  std::cout << " The test value is "  << MinMoves(test2) << std::endl;

	  int myints3[] = {1,0};
	  std::vector<int> test3 (myints3, myints3 + sizeof(myints3) / sizeof(int) );

	  std::cout << " The test value is "  << MinMoves(test3) << std::endl;


	  int myints4[] = {1,1,1};
	  std::vector<int> test4 (myints4, myints4 + sizeof(myints4) / sizeof(int) );

	  std::cout << " The test value is "  << MinMoves(test4) << std::endl;


	  int myints5[] = {0,0,1,0};
	  std::vector<int> test5 (myints5, myints5 + sizeof(myints5) / sizeof(int) );

	  std::cout << " The test value is "  << MinMoves(test5) << std::endl;
      */


	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

    int T;

	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {

		scanf("%s", g);
		vector<int> digits;
		for(int  j =0; j < MAXSIZE ; ++j)
		    {

		    	char temp = g[j];
		    	if(temp == '\0')
		    		break;
		    	if(temp == '+')
		    		digits.push_back(1);
		    	else
		    		digits.push_back(0);
		    }


		int res =  MinMoves(digits);

        printf("Case #%d: %d\n", Ti, res);
        fflush(stdout);


	}
	 fflush(stdout);




}
