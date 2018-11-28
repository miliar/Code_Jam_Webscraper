#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <complex>
using namespace std;

#define ABS(a)		((a) < 0 ? (a) * (-1) : (a))
#define MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAX(a, b)	((a) > (b) ? (a) : (b))


int main(void)
{
	int t;
	cin>> t;
	for(int _case = 0; _case < t; _case++) {
		int s_max;
		cin>> s_max;

		int sum = 0;
		int answer = 0;
		for(int level = 0; level <= s_max; level++) {
			char temp;
			cin>> temp;
			//cout<< level << " " << sum << endl;
			if(sum < level) {
				int less = (level - sum);
				answer += less;
				sum += less;
			}
			sum += (int)(temp - '0');
		}
		cout << "Case #" << _case + 1 << ": " << answer << endl;
	}

	return 0;
}
