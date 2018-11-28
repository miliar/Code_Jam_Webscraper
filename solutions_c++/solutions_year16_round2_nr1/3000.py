#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


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

bool pairCompare(const std::pair<string, int>& firstElem, const std::pair<string, int>& secondElem) {
	return firstElem.first < secondElem.first;

}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	string in;
	for (int i = 1; i <= n; ++i) {
		cin >> in;
		int alpha[26];
		_40l(k, 26) alpha[k] = 0;
		for (int j = 0; j < in.length(); ++j) {
			alpha[in[j] - 'A']++;
		}
		vector<int> nums;
		_40l(k, alpha[25]) nums.push_back(0);
		alpha['E' - 'A'] -= alpha['Z' - 'A'];
		alpha['O' - 'A'] -= alpha['Z' - 'A'];
		alpha['R' - 'A'] -= alpha['Z' - 'A'];
		alpha['Z' - 'A'] -= alpha['Z' - 'A'];
		_40l(k, alpha['W' - 'A']) nums.push_back(2);
		alpha['T' - 'A'] -= alpha['W' - 'A'];
		alpha['O' - 'A'] -= alpha['W' - 'A'];
		alpha['W' - 'A'] -= alpha['W' - 'A'];
		_40l(k, alpha['U' - 'A']) nums.push_back(4);
		alpha['F' - 'A'] -= alpha['U' - 'A'];
		alpha['O' - 'A'] -= alpha['U' - 'A'];
		alpha['R' - 'A'] -= alpha['U' - 'A'];
		alpha['U' - 'A'] -= alpha['U' - 'A'];
		_40l(k, alpha['X' - 'A']) nums.push_back(6);
		alpha['I' - 'A'] -= alpha['X' - 'A'];
		alpha['S' - 'A'] -= alpha['X' - 'A'];
		alpha['X' - 'A'] -= alpha['X' - 'A'];
		_40l(k, alpha['G' - 'A']) nums.push_back(8);
		alpha['I' - 'A'] -= alpha['G' - 'A'];
		alpha['H' - 'A'] -= alpha['G' - 'A'];
		alpha['E' - 'A'] -= alpha['G' - 'A'];
		alpha['T' - 'A'] -= alpha['G' - 'A'];
		alpha['G' - 'A'] -= alpha['G' - 'A'];
		_40l(k, alpha['H' - 'A']) nums.push_back(3);
		alpha['T' - 'A'] -= alpha['H' - 'A'];
		alpha['R' - 'A'] -= alpha['H' - 'A'];
		alpha['E' - 'A'] -= 2*alpha['H' - 'A'];
		alpha['H' - 'A'] -= alpha['H' - 'A'];
		_40l(k, alpha['F' - 'A']) nums.push_back(5);
		alpha['I' - 'A'] -= alpha['F' - 'A'];
		alpha['V' - 'A'] -= alpha['F' - 'A'];
		alpha['E' - 'A'] -= alpha['F' - 'A'];
		alpha['F' - 'A'] -= alpha['F' - 'A'];
		_40l(k, alpha['I' - 'A']) nums.push_back(9);
		alpha['N' - 'A'] -= 2 * alpha['I' - 'A'];
		alpha['E' - 'A'] -= alpha['I' - 'A'];
		alpha['I' - 'A'] -= alpha['I' - 'A'];
		_40l(k, alpha['V' - 'A']) nums.push_back(7);
		alpha['S' - 'A'] -= alpha['V' - 'A'];
		alpha['E' - 'A'] -= 2 * alpha['V' - 'A'];
		alpha['N' - 'A'] -= alpha['V' - 'A'];
		alpha['V' - 'A'] -= alpha['V' - 'A'];
		_40l(k, alpha['N' - 'A']) nums.push_back(1);
		sort(nums.begin(), nums.end());
		cout << "Case #" << i << ": ";
		for (std::vector<int>::iterator it = nums.begin(); it != nums.end(); ++it)
			std::cout << *it;
		std::cout << '\n';
	}


	return 0;
}