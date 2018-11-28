#include<cstdio>
#include<iostream>
#include<cmath>
#include<stdlib.h>
#include<string>
#include<time.h>
#include<vector>
#include<cstdint>
#include<set>

using namespace std;

set<string> used_string;

uint64_t find_div(uint64_t n) {
	for (uint64_t i = 2; i <= ceil(sqrt(n)); i++) {
		if (n%i == 0) {
			return i;
		}
	}
	return 0;
}

int check(string s) {
	vector<uint64_t> leg;
	for (int i = 2; i <= 10; i++) {
		uint64_t cur_number = 0;
		for (int j = 0; j < s.size(); j++) {
			cur_number = cur_number*i + (s[j] - '0');
		} 
		uint64_t div = find_div(cur_number);
//		cerr << "number in base " << i << " : " << cur_number << " div: " << div << endl;
		if (div == 0) {
			return 0;
		} else {
			leg.push_back(div);
		}
	}
	cout << s;
	for (int i = 0; i < leg.size(); i++) {
		cout << " " << leg[i];
	}
	cout << endl;
	return 1;
}

int main()
{
	freopen("c.txt", "r", stdin);
	freopen("c.out", "w", stdout);
	
	srand(time(0));
	cout << "Case #1:" << endl;
	int j;
	int n;
	cin >> n >> n >> j;
	int result = 0;
	while (1) {
		string s = "1";
		for (int i = 1; i < n - 1; i++) {
			s += ('0' + rand()%2);
		}
		s += "1";
		if (!(used_string.count(s) == 0)) continue;
//		cerr << s << endl;
		used_string.insert(s);
		result += check(s);
//		cerr << " " << result << endl;	
		if (result >= j) break;
	}
	
	return 0;
}

