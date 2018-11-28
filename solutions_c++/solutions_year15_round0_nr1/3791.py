#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <list>
#include <sstream>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>

#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << (_z))
#define rep(__z,__Z) for(int __z = 0; __z < __Z ; __z++ )
#define all(__z) __z.begin(),__z.end()

#define par pair<int, int>
#define p1 first
#define p2 second

#define eps = 1e-6

using namespace std;

int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};

int t, S;
char str[20100];

int main()
{
	cin >> t;
	int caze = 0;
	while (t --)
	{
		caze ++;
		int ans = 0;
		
		cin >> S;
		cin >> str;
		
		for (int i = 0, tot = 0; i <= S; i ++)
		{
			ans = max(ans, i - tot);
			tot += str[i]-'0';
		}
		cout << "Case #" << caze << ": " << ans << endl;
	}
		
	return 0;
}


