#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <bitset>
#include <map>
#include <time.h>
#include <string>
#include "math.h"
#include <functional>  
#include <stack>


using namespace std;

typedef long long ll;

#define _40l(index,limit) for(int index=0;index < limit;++index)
#define _40le(index,limit) for(int index=0;index <= limit;++index)
#define _41l(index,limit) for(int index=1;index < limit;++index)
#define _41le(index,limit) for(int index=1;index <= limit;++index)
#define _4ng0(index,start) for(int index=start;index > 0;--index)
#define _4nge0(index,start) for(int index=start;index >= 0;--index)
#define _4ng1(index,start) for(int index=start;index > 1;--index)
#define mp(x,y) make_pair(x,y)
#define mtp(x,y,z) mp(x,mp(y,z))
#define int_max 2147483647
#define ll_max 9223372036854775807

bool pairCompare(const std::pair<int, int>& firstElem, const std::pair<int, int>& secondElem) {
	return firstElem.second > secondElem.second;

}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		int parties;
		vector<pair<int, int>> pairs;
		cin >> parties;
		int sum = 0,temp;
		_40l(j, parties) {
			cin >> temp;
			sum += temp;
			pairs.push_back(mp(j, temp));
		}
		/*while (sum != 0) {
			
		}*/
		if (parties == 2) {
			_40l(k, sum / 2 - 1 ) {
				cout << "AB ";
			}
			cout <<"AB\n";
		}
		else {
			float mid;
			string out = "";
			while (sum > 0) {
				sort(pairs.begin(), pairs.end(), pairCompare);
				if (pairs[0].second <= (sum - 2) / 2.0 && pairs[0].second > 1) {
					out+= string(1, ('A' + pairs[0].first)) + string(1, ('A' + pairs[0].first))+ " ";
					sum -= 2;
					pairs[0].second -= 2;
					if (pairs[0].second == 0) pairs.erase(pairs.begin());
				}
				else if (pairs[0].second <= (sum - 1) / 2.0) {
					out += string(1, ('A' + pairs[0].first)) + " ";
					sum -= 1;
					pairs[0].second -= 1;
					if (pairs[0].second == 0) pairs.erase(pairs.begin());
				}
				else
				{
					out += string(1, ('A' + pairs[0].first)) + string(1, ('A' + pairs[1].first)) + " ";
					sum -= 2;
					pairs[0].second -= 1;
					pairs[1].second -= 1;
					if (pairs[1].second == 0) pairs.erase(pairs.begin()+1);
					if (pairs[0].second == 0) pairs.erase(pairs.begin());
				}
			}
			cout << out.substr(0, out.length() - 1);
			cout << '\n';
		}
	}
	return 0;
}