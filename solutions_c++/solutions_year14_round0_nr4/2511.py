#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <list>
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

template<class TYPE>
vector<TYPE> & split(const std::string &s, char delim, std::vector<TYPE> &elems) {
	std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
		int value; 
		if (! (istringstream(item) >> value))
			value = 0; 
    	elems.push_back(value);
    }
    return elems;
}

template<class TYPE> 
void print(list<TYPE>& vec) { 
	cout<<"["; 
	for (typename list<TYPE>::iterator it = vec.begin() ; it != vec.end(); ++it) { 
		cout << *it <<", ";
	}
	cout<< "]"<<endl;
}


int deceitWar(list<double> l1, list<double> l2) { 
	int count = 0; 
	while (! l1.empty()) { 
		double e1 = l1.front(); 
		double e2 = l2.front(); 
		if (e1 > e2) { 
			count++; 
			l1.pop_front(); 
			l2.pop_front(); 
		} else { 
			l1.pop_front(); 
			l2.pop_back(); 
		}
	}
	return count; 
}

int optimalWar(list<double> l1, list<double> l2) { 
	int count = l1.size(); 
	while (! l1.empty()) { 
		double e1 = l1.front(); 
		list<double>::iterator it; 
		for (it = l2.begin(); it != l2.end(); ++it) { 
			double e2 = *it;
			if (e2 > e1) { 
				count--; 
				l2.erase(it); 
				l1.pop_front(); 
				//cout << " e1 = " << e1 << " e2 = " <<e2 << endl;
				break; 
			}
		}
		if (it == l2.end()) { 
			l1.pop_front(); 
			l2.pop_front();
		}
	}
	return count; 
}


int main(int argc, const char* argv[]) { 

	int ntest = 0; 
	cin >> ntest; 
	int testcase = 1; 
	while (ntest--) { 
		double n, nval;
		cin>> n; 
		nval = n;
		std::list<double> naomi; 
		std::list<double> ken; 
		double value; 

		while (n--) { 
			cin >> value; 
			naomi.push_back(value); 
		}

		while (nval--) { 
			cin >> value; 
			ken.push_back(value); 
		}

		naomi.sort(); 
		ken.sort(); 
		//print(naomi); 
		//print(ken);
		cout<< "Case #"<<testcase<<": "<<deceitWar(naomi, ken)<< " " << optimalWar(naomi, ken)<<endl;

		testcase++; 
	}
	return 0; 
}
