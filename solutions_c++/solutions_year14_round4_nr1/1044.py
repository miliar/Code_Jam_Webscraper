#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <utility>
#include <functional>
#include <iterator>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cmath>
#include <cstdlib>
//#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
//using namespace boost::multiprecision;

void comp(int tc){
	int N, X;
	cin >> N >> X;
	multiset<int> m;
	for (int i = 0; i < N; ++i){
		int tmp;
		cin >> tmp;
		m.insert(tmp);
	}

	int count = 0;
	while (!m.empty()){
		++count;
		auto it = m.end();
		--it;
		int first = *it;
		m.erase(it);
		if (!m.empty()){
			int rem = X - first;
			it = m.lower_bound(rem);
			if (it == m.end()){
				--it;
			}
			if (*it > rem){
				if (it == m.begin())
					continue;
				--it;
			}
			m.erase(it);
		}
	}

	cout << "Case #" << tc << ": " << count << endl;
}

int main(){
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		comp(tc);
	}
}