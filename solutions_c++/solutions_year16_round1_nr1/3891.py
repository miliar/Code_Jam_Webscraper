#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <bitset>
#include <list>
#include <limits.h>
#include <iomanip>
#include <time.h>

using namespace std;

void testing (int position = 0){static clock_t clock_tStart;if (position==0){freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);clock_tStart = clock();}else {printf("\n\nTime taken: %fs\n\n", (double)(clock() - clock_tStart)/CLOCKS_PER_SEC);}}
void real_main();
int main ()
{
#ifdef WINDORO
testing(0);
#endif
    real_main();
#ifdef WINDORO
testing(1);
#endif
    return 0;
}
// --------------------------------- CODE HERE ------------------------------------------ 

#define ii pair<int,int>
#define iii pair<int,ii>
#define INF 2000000000
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef vector <ii> vii;
typedef vector <iii> viii;


void real_main()
{
    list <char> v;
    list <char>::iterator it;
    int t;
    cin >> t;
    int kasus = 1;
    while ( t-- )
    {
        string s;
        cin >> s;
        
        
        v.push_back( s[0] );
        
        for ( int i=1;i<s.size();i++ )
        {
            if ( s[i] >= v.front() )
            {
                v.push_front( s[i] );
            }
            else
            {
                v.push_back( s[i] );
            }
        }
        
        cout << "Case #" << kasus++ << ": ";
        for ( it = v.begin();it!=v.end();it++ )
        {
            cout << *it;
        }
        cout << endl;
        
        v.clear();
    }
    
}











