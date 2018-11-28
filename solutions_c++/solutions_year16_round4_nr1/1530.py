#pragma	comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <list>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define pi acos(-1.0)
#define eps 1e-9

char a[100005];
char b[] = {'P', 'S', 'R'};

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		string res = "Z";
		int n, r, p, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		for(int i = 0; i < 3; i++)
		{
			a[1] = b[i];
			for(int j = 1; j < (1 << n); j++)
			{
				if(a[j] == 'P')
				{
					a[2*j] = 'P';
					a[2*j+1] = 'R';
				}
				if(a[j] == 'R')
				{
					if(2*j >= (1 << n))
					{
						a[2*j] = 'R';
						a[2*j+1] = 'S';
					}
					else
					{
						a[2*j] = 'S';
						a[2*j+1] = 'R';
					}
				}
				if(a[j] == 'S')
				{
					if(4*j >= (1 << n))
					{
						a[2*j] = 'P';
						a[2*j+1] = 'S';
					}
					else
					{
						a[2*j] = 'S';
						a[2*j+1] = 'P';
					}
				}
			}
			int cntr = 0, cnts = 0, cntp = 0;
			for(int j = (1 << n); j < 2 * (1 << n); j++)
			{
				if(a[j] == 'R')
					cntr++;
				else
					if(a[j] == 'S')
						cnts++;
					else
						cntp++;
			}
			if(r == cntr && p == cntp && s == cnts)
			{
				a[2 * (1 << n)] = 0;
				res = min(res, string(a + (1 << n)));
			}
		}
		if(res == "Z")
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %s\n", t, res.c_str());
	}
	return 0;
}