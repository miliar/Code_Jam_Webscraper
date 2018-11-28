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
	cin >> T; 
	
	for(int t = 1; t <= T; t++)
	{
		string s;
		int i, c = 0;

		cin >> s;

		int l = s.length();
		while(1) {
			i = 0;

			if(s[i] == '+') {
				while(s[i] == '+' && i < l)
					i++;

				if(i >= l) {
					break;
				} else {
					for(int j = 0; j <= i; j++)
						s[j] = '-';
					c++;
				}
			} else if(s[i] == '-') {
				while(s[i] == '-' && i < l)
					i++;

				if(i >= l) {
					c++;
					break;
				} else {
					for(int j = 0; j <= i; j++)
						s[j] = '+';
					c++;
				}
 
			}
		}

		cout << "case #" << t << ": " << c << endl;
	}
	
	return 0;
}
