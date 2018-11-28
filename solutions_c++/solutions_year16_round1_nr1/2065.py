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
		string s;
		cin >> s;
		string result;
		for (int i = 0; i < s.length(); ++i){
			if (s[i] >= result[0]){
				result = s.substr(i, 1)+result;
			}
			else{
				result = result+s.substr(i, 1);

			}
		}
		cout << "Case #" << _t << ": " <<result<< endl;
		cerr << _t << endl;
	}

	return 0;
}
