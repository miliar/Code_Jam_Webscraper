#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>
#include <deque>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define B 33
#define MAX 100010
#define eps 1e-7
#define pi 3.14159
#define ull unsigned long long
#define MOD 1000000009

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;

int t;
long double c,f,x;
long double curr;
long double tempo;

bool isBetter(long double c,long double f,long double x)
{
	return c/curr + x/(curr + f) <= x/curr;
}

int main(void)
{
	scanf("%d",&t);
	int cases = 0;
	while (t--)
	{
		scanf("%llf %llf %llf",&c,&f,&x);

		curr = 2.0;
		tempo = 0;

		while ( isBetter(c,f,x) )
		{
			tempo += c/curr;
			curr += f;
		}

		printf("Case #%d: %.7llf\n",++cases,tempo + x/curr);
	}
	return 0;
}