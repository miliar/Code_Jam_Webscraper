#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <sstream>

using namespace std;

typedef long long llong;


int main()
{
   // ios_base::sync_with_stdio(false);
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    
    int TC;
    cin>>TC;

    for(int j = 1; j <= TC; j++)
    {
        llong a, b, c;
        cin>>a>>b>>c;
        llong cnt = 0;

        for(llong k = 0; k < a; k++)
        {
            for(llong i = 0; i < b; i++)
            {
                llong ans = (k&i);
    
                if(ans < c)
                    cnt++;
                
            }
        }

        printf("Case #%d: %lld\n", j, cnt);
    }

    return 0;
}