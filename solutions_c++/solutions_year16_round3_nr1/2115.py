/*
* @Author: doody
* @Date:   2016-05-08 14:39:43
* @Last Modified by:   doody
* @Last Modified time: 2016-05-08 15:19:15
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

template <typename T1, typename T2>
struct less_second {
    typedef pair<T1, T2> type;
    bool operator ()(type const& a, type const& b) const {
        return a.second > b.second;
    }
};

int main(){
	int T(0), N(0), P(0), sum(0);
	vector<pair<char, int> > hashMap;
	char ch = 'A';

	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		ch = 'A';
		sum = 0;
		cin >> N;
		for (int j = 0; j < N; ++j)
		{
			cin >> P;
			sum += P;
			hashMap.push_back(make_pair(ch, P));
			ch++;
		}

		sort(hashMap.begin(), hashMap.end(), less_second<char, int>());
		
		cout << "Case #" << i << ":";
		while (hashMap.front().second != 0)
		{
			// cout << sum;
			if (hashMap[2].second <= (sum-2)/2 and hashMap[1].second > 0)
			{
				cout << ' ' << hashMap[0].first << hashMap[1].first;
				--hashMap[0].second;--hashMap[1].second;
				sum -= 2;
			}
			else
			{
				cout << ' ' << hashMap[0].first;
				--hashMap[0].second;
				sum -= 1;
			}
			sort(hashMap.begin(), hashMap.end(), less_second<char, int>());
		}
		cout << '\n';
	}

    return 0;
}