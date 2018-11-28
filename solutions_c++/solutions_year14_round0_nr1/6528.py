/*
prob: A.cpp
id: amlansaha
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
	freopen("A-small.in", "r", stdin);
//	freopen("A-large.in", "r", stdin);
	freopen("A-output.out", "w", stdout);

    int i, j, k, l, temp, t, n, ans, caseno = 0, choice;
    int row1[4], row2[4];
    scanf ( "%d", &t );
    
    while ( t-- )	{
    	scanf ( "%d", &choice );
    	choice--;
    	FR (i,4)	{
    		FR ( j, 4)	{
    			scanf ( "%d", &temp );
    			if ( i == choice )	row1[j] = temp;
    		}
    	}

		scanf("%d", &choice);
		choice--;
		FR (i,4)	{
			FR ( j, 4)	{
				scanf("%d", &temp);
				if (i == choice)	row2[j] = temp;
			}
		}
		k = 0, ans = 0;
		FR ( i, 4)	{
			FR ( j, 4 )	{
				if ( row1[i] == row2[j] )	{
					k++;
					ans = i;
				}
			}
		}

    	printf ( "Case #%d: ", ++caseno );
    	if ( k == 0 )	printf ( "Volunteer cheated!\n" );
    	else if ( k == 1 )	printf ( "%d\n", row1[ans] );
    	else	printf ( "Bad magician!\n" );
    }
    return 0;
}
