#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <set>
#include <queue>

using namespace std;

typedef long long int LL;
typedef pair<int,int> pii;

#define F first
#define S second
#define pb push_back
#define mp make_pair

bool palindrom(int x)
{
	char z[10];
	sprintf(z, "%d", x);
	int sz = strlen(z);

	for(int i = 0; i < sz/2; ++i)
		if(z[i] != z[sz-1-i]) return false;
	return true;
}

int main (void)
{
	int T;
	cin >> T;

	for(int c = 1; c <= T; ++c)
	{
		int a, b;
		cin >> a >> b;

		int res = 0;
		for(int i = 1; i <= b; ++i) {
			if( palindrom(i) && palindrom(i*i) && i*i <= b && i*i >= a) res++;

		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
