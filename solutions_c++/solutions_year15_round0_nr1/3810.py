/** Libr@ries **/
//#include "bits/stdc++.h"
#include "stdio.h"
#include "string.h"
#include "cmath"
#include "iostream"
#include "algorithm"
#include "map"
#include "set"
#include "vector"

/** System **/
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

/** System_Win_32 **/
#if ( WIN32 || __WIN32_ )
   #define lld I64d
#endif

/** Utilities **/
#define forit(i,v  )  for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define fori( i,a,b)  for (int i = (int)(a); i < (int)(b); i++)
#define forn( i, n )  fori( i, 0, n )
#define zeros( a )    memset(a, 0,sizeof(a))
#define null( a )     memset(a,-1,sizeof(a))
#define all( a )      (a).begin() , (a).end()
#define sqr( a )      ( (a)*(a) )
#define sz( a )       (a).size()
#define pb            push_back
#define mp            make_pair
#define F             first
#define S             second
#define PI            2*acos(0.0)
using namespace std;
typedef long long LL;


int main(int argc, char const *argv[])
{
    int tc;
    cin >> tc;
    int n;
    string buff;


    for (int caso = 0; caso < tc; ++caso)
    {
    	
    	int ans = 0;
    	int acom = 0;
    	cin >> n >> buff;

    	for (int i = 0; i < (int)buff.size(); ++i)
    	{
    		if ( i )
    		{
    			if ( acom < i )
    			{
    				int add = i - acom;
    				ans += add;
    				acom += add;
    			}

    			acom += buff[ i ] - '0';
    		}
    		else 
    		{
    			if ( buff[i] > '0' ){
    				acom += buff[ i ] - '0' ;
    			}
    		}
    	}

    	cout << "Case #" << caso+1 << ": " << ans << endl;
    }
    return 0;
}
