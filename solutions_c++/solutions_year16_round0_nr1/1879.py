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
 
using namespace std;

int main() {
	int total_num;
	cin >> total_num;
	for(int m = 1; m <= total_num; m++) {
		long long num;
		cin >> num;
		int max = 1000000;
		vector<int> store(10, 0);

		bool yes = false;

		long long cpy = 0;
		for(int i = 1; i < max; i++) {
			cpy += num;
			long long tmp = cpy;

			// cout << tmp << endl;
			while(tmp) {
				int d = tmp % 10; 
				store[d]++;
				tmp = tmp/10;
			}

			bool got = true;
			for(int k = 0; k < store.size(); k++) {
				if(store[k] == 0) {
					got = false;
				}
			}

			if(got) {
				cout << "Case #" << m << ": " << cpy << endl;
				yes = true;
				break;
			} 
		}

		if(!yes) {
			cout << "Case #" << m << ": INSOMNIA" << endl;
		}
	}
}