#include<bits/stdc++.h>
#define sf scanf
#define pf printf

using namespace std;

int main()
{
    freopen("input.txt" , "r" , stdin);
    freopen("output.in" , "w" , stdout);
    int t , cc = 0 , k , c , s;
    sf("%d" , &t);
    while(t--)
    {
        sf("%d %d %d" , &k , &c , &s);
        pf("Case #%d:" , ++cc);
        if(c == 1)
        {
            if(k == s)
            {
                for(int i = 1 ; i <= k ; ++i) pf(" %d" , i);
            }
            else pf(" IMPOSSIBLE");
        }
        else
        {
            if(s == k)
            {
                for(int i = 1 ; i <= s ; ++i) pf(" %d" , i);
            }
            else if(s == k - 1)
            {
                for(int i = 1 ; i <= s ; ++i) pf(" %d" , i + 1);
            }
            else pf(" IMPOSSIBLE");
        }
        pf("\n");
    }
    return 0;
}
