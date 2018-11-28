#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
using namespace std;

template <class T, class U> T lexical_cast(U from) {
	stringstream ss;
	T to;
	ss << from;
	ss >> to;
	return to;
}

bool is_palindrome(const string& str) {
	string rev(str);
	reverse(rev.begin(), rev.end());
	return rev == str;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	set<long long> s;
	for(long long i = 1; i <= 10000000; ++i) {
		if(is_palindrome(lexical_cast<string>(i))
		   && is_palindrome(lexical_cast<string>(i * i)))
			s.insert(i * i);
	}

	int t;
	cin >> t;

	for(int test = 1; test <= t; ++test) {
		long long a, b;
		cin >> a >> b;
		set<long long>::const_iterator it = s.lower_bound(a), en = s.upper_bound(b);
		int cnt = 0;
		while(it != en) {
			++cnt;
			++it;
		}

		cout << "Case #" << test << ": " << cnt << endl;
	}

	return EXIT_SUCCESS;
}
