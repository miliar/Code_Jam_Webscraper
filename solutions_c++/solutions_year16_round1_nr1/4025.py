#include <iostream>
#include <cstdio>
#include <climits>
#include <cstring>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <list>
#include <cmath>
#include <numeric>
#include <utility>
#include <algorithm>
using namespace std;

#define BUF 1001
#define LEN 400
#define MOD 1000000007
#define PI 3.1415926535
#define lu unsigned long long int
#define ll long long int
#define pp pair<long long int, long long int>
#define vp vector< pp >
#define vl vector< ll >
#define vi vector< long int >
#define vvi vector< vi >
#define qi queue< int >
#define st stack< long int >
#define bt bitset<100>
#define pb(n) push_back(n)
#define setl set<long int>

bool sortfunc(long long int i, long long int j)
{
	return (fabs(i)<fabs(j));
}

lu look[10][30];

int main(int argc, char const *argv[])
{
	int t,c;
	scanf("%d", &t);
	for(c=0;c<t;c++)
	{
		char s[BUF],pref[BUF],suf[BUF],out[BUF];
		scanf("%s", s);
		int len = strlen(s),k=0,k1=0,k2=0;

		pref[0] = s[0];
		k1=1;
		for (int i = 1; i < len; ++i)
		{
			// al[s[i] - 'A']++;
			if((int)s[i] >= (int)pref[k1-1])
				pref[k1++] = s[i];
			else
				suf[k2++] = s[i];
		}

		for (int i = k1-1; i >= 0; --i)
			out[k++] = pref[i];

		for (int i = 0; i < k2; ++i)
			out[k++] = suf[i];

		out[k] = '\0';
		printf("Case #%d: %s\n", c+1, out);
	}
	return 0;
}