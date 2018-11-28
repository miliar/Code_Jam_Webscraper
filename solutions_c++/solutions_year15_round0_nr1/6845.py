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

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); ++k)

using namespace std;

int main() {
  	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

  	int tt; cin >> tt;
  	for (int qq=1; qq<=tt; qq++) {
    	printf("Case #%d: ", qq);
		
		int max; cin >> max;
		string data; cin >> data;
		
		unsigned long total_people = 0;
		unsigned long total_friends = 0;
		for(unsigned int shyness_factor=0; shyness_factor<data.length(); shyness_factor++) {
			unsigned int people = data[shyness_factor] - '0';
			unsigned long friends = 0;		
			
			if (people > 0 && shyness_factor > total_people) {  
				friends = shyness_factor - total_people;
			}
			total_people += people + friends;
			total_friends += friends;
		}

		cout << total_friends << endl; 
	}

	return 0;
}

