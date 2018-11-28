#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

int howMany ( long a, long n, size_t c )
{
    int i = 0;
    while ( a <= n && i < c )
    {
        a += a - 1;
        ++i;
    }
    return i;
}

int main ()
{
    ofstream out;
    out.open ("a.out");

    int T;
    cin >> T;
    
    list< long > n;
    long t, a;
    int N, ans;
    
    for ( int i = 1; i <= T; ++i )
    {
        cin >> a >> N;
        
        ans = 0;
        n.clear();
        for ( int x = 0; x < N; ++x )
        {
            cin >> t;
            n.push_back(t);
        }
        
        n.sort();
        while (!n.empty())
        {
            if ( n.front() >= a && (a + a - 1) > n.front())
            {
                a += a - 1;
                ++ans;
            }
            else if ( n.front() >= a )
            {
                int o = howMany( a, n.front(), n.size() );
                if ( o < n.size() )
                {
                    while ( o > 0 )
                    {
                        a += (a - 1);
                        --o;
                        ++ans;
                    }
                }
                else
                {
                    n.pop_front();
                    ++ans;
                }
            }
            else
            {
                a += n.front(); n.pop_front();
            }
        }
        
        out << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
