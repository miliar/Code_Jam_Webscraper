/*
prob: A
id: amlan
lang: C++
date: Apr 11, 2015
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
typedef pair<int, int> PII;

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define ROF(i,a,b) for(i=a;i>=b;i--)
#define FR(i,n)	for(i=0;i<n;i++)
#define RF(i,n) for(i=n;i>0;i--)
#define CLR(a) memset ( a, 0, sizeof ( a ) )
#define RESET(a) memset ( a, -1, sizeof ( a ) )
#define PB(a)	push_back ( a )


int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

    int i, j, k, l, temp, t, n, m, ans, caseno = 0;
    string str;
    scanf ( "%d", &t );
    
    while ( t-- )	{
    	cin >> n >> str;
    	k = str[0]-'0';
    	ans = 0;
    	FOR ( i, 1, n )	{
    		if ( k < i )	{
    			ans+= i-k;
    			k = i;
    		}
    		k += str[i]-'0';
    	}
    	printf ( "Case #%d: %d\n", ++caseno, ans );
    }
    return 0;
}
