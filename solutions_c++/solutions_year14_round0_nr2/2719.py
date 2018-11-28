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


double minCost(double c, double start, double f, double x) { 
	double curr = x / start; 
	double next = c / start +  x / (start + f);
#ifdef DEBUG 
	cout << " c = " << c << " start = "<<start << " f = "<< f << " x = " << x <<endl; 
	cout << "  curr = "<<curr << " next = " << next << endl; 
#endif 
	if (next < curr) 
		return c/start + minCost(c, start + f, f, x); 
	return curr;
} 

int main(int argc, const char* argv[]) { 

	int ntest = 0; 
	cin >> ntest; 
	int testcase = 1; 
	std::cout.precision(7);
	cout << std::fixed; 
	while (ntest--) { 
		double c, f, x; 
		cin>> c >> f >> x; 
		//cout << "\n c = " << c << " f = " << f <<" x = " << x <<endl;

		cout << "Case #"<<testcase<<": "<<minCost(c,2, f, x) <<endl; 

		testcase++; 
	}
	return 0; 
}
