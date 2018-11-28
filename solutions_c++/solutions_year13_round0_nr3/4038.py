#include <iostream>
#include <algorithm>
#include <sstream>
#include <ctime>
#include <set>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)


bool is_pal(long long n) {
	stringstream ss;
	ss << n;
	string s;
	ss >> s;
	string t;
	t = s;
	reverse(t.begin(), t.end());
	return s==t;
}

int main () {
#ifdef __ASD__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	vector<long long> pals;
	for(int i=1;i<=10000000;++i) {
		if (!is_pal(i))continue;
		long long n = i;
		n*=n;
		if (is_pal(n)) {
			pals.push_back(n);
		}
	}

	int t;
	cin >> t;
	for(int tc=1;tc<=t;++tc) {
		long long l, r;
		cin >> l >> r;
		int res=0;
		forn(i, pals.size()) {
			if (pals[i]>=l && pals[i]<=r)++res;
		}
		cout<<"Case #"<<tc<<": "<<res<<endl;
	}
	return 0;
}