#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iostream>
#define mp make_pair
#define pb push_back

#define s second
#define f first

using namespace std;

vector < pair <char, int> > t[1000];
char s[1000][1000];

int foo ( int x, int y)
{
	if ( x * 1.0 / y - x / y >= 0.49999999)
		return x / y + 1;
	else
		return x / y;
}


int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int test;
	scanf("%d", &test);
 
    for ( int ii = 1; ii <= test; ii++)
    {
    	int n;
    	scanf("%d\n",&n);
    	for ( int i = 0; i < n; i++)
    	{	
    		gets(s[i]);
    		int len = strlen(s[i]);
    		t[i].clear();
    		for ( int j = 0; j < len; j++)
    		{
    			if ( j == 0 || s[i][j] != s[i][j - 1])
    				t[i].pb(mp(s[i][j], 1));
    			else
    				t[i][(int)t[i].size() - 1].s++;
    		}
    	}
    	int fl = 0;
    	long long res = 0;
    	for ( int i = 1; i < n; i++)
    		if ( t[0].size() != t[i].size())
    			fl = 1;
    	for ( int j = 0; j < (int)t[0].size(); j++)
    	{
    		int sr = 0;
    		for ( int i = 0; i < n; i++)
    		{
    			if ( t[0][j].f != t[i][j].f)
    				fl = 1;
    			sr += t[i][j].s;
    	   	}
    	   	sr = foo(sr, n);
    	    for ( int i = 0; i < n; i++)
    			res += abs(sr - t[i][j].s);
    	}
    	if ( fl == 1)
    		printf("Case #%d: Fegla Won\n", ii);
        else
        	
    		printf("Case #%d: %I64d\n", ii, res);
    	
    }




 

	return 0;
}