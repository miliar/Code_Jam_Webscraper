#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <vector>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <iostream>  
#include <string>
#include <iomanip>
#include <ctime>
using namespace std;

#define EPS 1e-9
#define ABS(a) ( (a) < 0 ? -(a) : (a) )

const double PI = 4 * atan(1.0);
const int MAXN  = (int)(210);

typedef long long ll;
const ll INF = (int)1E9 + 10;
const int MOD = (int)(1001017);
const int P = 31;

#define mp make_pair 
#define FOR(i,s,f) for(int i=s; i<f; i++)

//  prime -> 1001017
//int dir[2][4] = {{ -1, 0, 1, 0 }, { 0, 1, 0, -1 }}; 
//************************************************

char str[110];

int main()
{
freopen("B-large.in", "rb", stdin); 
freopen("out.txt", "wt", stdout);
//unsigned int start_time =  clock();

int t; cin >> t;

for(int f=1; f<=t; f++)
{
	scanf("%s", str);

	bool pr = (str[0] == '+' ? 1: 0);
	int ans = 0;
	int len = strlen(str);

	for(int i=1; i<len; i++)
	{
		bool cur = (str[i] == '+' ? 1: 0);

		if(pr != cur)
		{
			ans ++; pr=cur;
		}

	}

	if( pr == 0 ) ans++;

	cout << "Case #" << f <<": " << ans << endl;
}

	return 0;
}

