#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <limits.h>
#include <memory>
#include <cstdio>
using namespace std;

int main() 
{
	int T; 
	string s;

	cin >> T; 
	for(int t = 1; t <= T; t++)
	{
		string result;
		cin >> s;
		result += s[0];

		for(int i = 1; i < s.length(); i++) 
		{
			if(s[i] >= result[0])
				result = s[i] + result;
			else 
				result += s[i];
		}

		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}
