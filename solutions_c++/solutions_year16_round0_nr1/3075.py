#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <list>
#include <climits>
#include <assert.h>
#include <functional>     // std::greater
#ifdef _WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif

using namespace std;
#define ll long long
int main()
{
	ll T = 0;
	cin >> T;
	for (int _t = 1; _t <= T; ++_t){
		ll N;
		cin >> N;
		vector<bool> taken(10);
		ll val = N;
		ll i = 0;
		for (i = 0; i < 1000000;++i){
			ll tmp = val;
			while (tmp){
				taken[tmp % 10] = true;
				tmp /= 10;
			}

			bool ok = true;
			for (int j = 0; j < 10; ++j){
				if (taken[j] == false)ok = false;
			}
			if (ok)break;
			val += N;
		}

		if (i < 1000000){
			cout << "Case #" << _t << ": " << val << endl;
		}
		else{
			cout << "Case #" << _t << ": " << "INSOMNIA" << endl;

		}
		cerr << _t << endl;
	}

	return 0;
}
