#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;
//#define DEBUG

template<class T>
bool pairCompare(const T & x, const T & y)
{
  return x.second < y.second;
}

template<class T>
typename T::const_iterator map_max_element(const T &A)
{
    typedef typename T::value_type pair_type;
    return max_element(A.begin(), A.end(), pairCompare<typename T::value_type>);
}


bool verify(int p, int q) { 
	while (p < q) { 
		if (q % 2 != 0) 
			return false; 
		q /= 2;
	}
	if (p == q) 
		return true; 
	else 
		return verify(p-q, q);
}

int gen(int p, int q) { 
	int count = 0; 
	while (p < q) { 
		if (q % 2 != 0) 
			return -1; 
		q /= 2;
	   	count++; 
	}
	if (p == q || verify(p-q, q)) {
		return count ;
	}
	return -1; 
}	

int main(int argc, const char* argv[]) { 

	int ntest = 0; 
	cin >> ntest; 
	int testcase = 1; 
	//std::cout.precision(7);
	// cout << std::fixed; 
	while (ntest--) { 
		int p, q; 
		char s; 
		cin>> p >> s >> q; 

		int res = gen(p, q); 
		if (res == -1) 
			cout << "Case #"<<testcase<<": "<<  "impossible" <<endl; 
		else 
			cout << "Case #"<<testcase<<": "<< res  <<endl; 

		testcase++; 
	}
	return 0; 
}
