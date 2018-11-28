#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <cctype>
using namespace std;
typedef long long llong;
typedef unsigned long long ullong;
typedef unsigned int uint;

int GCD(int u, int v)
{
    int tmp;
 
    while(v)
    {
        tmp = u%v;
        u = v;
        v = tmp;
    }
    return u;
}

int LCM(int u, int v)
{
	return u*v / GCD(u, v);
}

int main(void)
{
	int numTests;
	cin >> numTests;
	for(int caseNum=1; caseNum<=numTests; caseNum++) {

		llong p, q;
		char ch;
		cin >> p >> ch >> q;

		bool possible = false;
		int answer = 1;
		if(q % 2 == 0) {
			possible = true;

			int m = 2;
			while( (double)p/q < (double)1/m ) {
				m *= 2;
				answer++;
			}

			while(q % 2 == 0)
				q = q / 2;
			if(q != 1)
				possible = false;
		}
		
		cout << "Case #" << caseNum << ": ";
		if(possible)
			cout << answer << endl;
		else
			cout << "impossible" << endl;
		

	}
	return 0;
}