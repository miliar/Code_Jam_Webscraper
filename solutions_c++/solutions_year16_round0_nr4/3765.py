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


	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

    int T;

	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {

		int K;
		int Kdup;
		int C;
		scanf("%d %d %d", &K, &C, &Kdup);
        std::cout << "Case #"<< Ti << ": ";
        for(int i = 0; i < K; ++i)
        	std::cout << i+1 << " " ;
        std::cout << std::endl;
        //printf("Case #%d: %d\n", Ti, res);
        fflush(stdout);


	}
	 fflush(stdout);




}
