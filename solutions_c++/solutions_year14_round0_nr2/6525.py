/*
GOOGLE CODEJAM 2014
Qualification Round
prob: B.cpp
id: i.amlansaha@gmail.com
lang: C++
date: Apr 12, 2014
algo: 
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef map<int, int> MAPII;
typedef map<string,int> MAPSI;

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define ROF(i,a,b) for(i=a;i>=b;i--)
#define FR(i,n)	for(i=0;i<n;i++)
#define RF(i,n) for(i=n;i>0;i--)
#define CLR(a) memset ( a, 0, sizeof ( a ) )
#define RESET(a) memset ( a, -1, sizeof ( a ) )
#define PB(a)	push_back ( a )


int main ()
{
//	freopen("B-small.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-output.out", "w", stdout);

    int i, j, k, l, temp, t, n, ans, caseno = 0;
    double r, c, f, x, total, temp1, temp2;
    scanf ( "%d", &t );
    
    while ( t-- )	{
    	scanf ( "%lf %lf %lf", &c, &f, &x );
    	r = 2;
    	total = 0;
    	while (1)	{
    		temp1 = x/r;
    		temp2 = c/r + x/(r+f);
    		if ( temp1 <= temp2 )	{
    			total+= temp1;
    			break;
    		}
    		else	{
    			total+= c/r;
    			r+= f;
    		}
    	}
    	printf ( "Case #%d: %.7lf\n", ++caseno, total+1e-10 );
    }
    return 0;
}
