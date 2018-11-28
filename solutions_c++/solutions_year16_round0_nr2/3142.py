#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
using namespace std;

typedef long long ll;

int main()
{
	ll T = 0;
	cin >> T;
	for (int _t = 1; _t <= T; ++_t){
		string s;
		cin >> s;
		int index = s.length() - 1;
		int result = 0;
		while (index >= 0 && s[index] == '+')index--;
		while (index >= 0){
			for (int i = 0; i <= index; ++i){
				s[i] = s[i] == '+' ? '-' : '+';
			}
			++result;
			while (index>=0&&s[index] == '+')index--;
		}


		cout << "Case #" << _t << ": " << result << endl;
		cerr << "Case #" << _t << ": " << result << endl;
		
	}
}