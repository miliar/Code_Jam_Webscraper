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
#include <stdlib.h>
#include <stdio.h>
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
		vector<char> count(3000);
		for (int i = 0; i < s.length(); ++i){
			count[s[i]]++;
		}

		vector<int> result(10);
		result[0] = count['Z'];
		result[2] = count['W'];
		result[6] = count['X'];
		result[8] = count['G'];

		result[3] = count['T'] - result[8] - result[2];
		result[4] = count['R'] - result[3] - result[0];
		result[5] = count['F'] - result[4];
		result[7] = count['V'] - result[5];

		result[1] = count['O'] - result[0] - result[2] -result[4];
		result[9] = count['I'] - result[5] - result[6] - result[8];
		string output;
		for (int i = 0; i < 10; ++i){
			for (int j = 0; j < result[i]; ++j){
				string s = " ";
				stringstream ss;
				ss << i;
				output += ss.str();
			}
		}

		cout << "Case #" << _t << ": " << output << endl;
		cerr << _t << endl;
	}

	return 0;
}
