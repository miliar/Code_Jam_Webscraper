#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;

using namespace std;

int n, x;
multiset< int > s;

void solve()
{
    s.clear();
    cin >> n >> x;
    for ( int i = 0; i < n; i++ )
    {
        int a; cin >> a;
        s.insert( a );
    }
    int answer = 0;
    while ( s.size() )
    {
        answer++;
        multiset< int >::iterator it = s.end();
        it--;
        int cur = *it;
        //cout << cur << " ";
        s.erase( it );
        it = s.upper_bound( x - cur );
        if ( it == s.begin() || s.size() == 0 ) 
        {
            //cout << "\n";
            continue;
        }
        it--;
        //cout << *it << "\n";
        s.erase( it ); 
    }
    cout << answer;
}

int main (int argc, const char * argv[])
{
    int testcases; cin >> testcases;
    for ( int i = 1; i <= testcases; i++ )
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}