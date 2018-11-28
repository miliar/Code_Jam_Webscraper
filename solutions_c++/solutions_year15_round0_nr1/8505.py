#include <iostream>
#include <algorithm>
#include <cstring>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <time.h>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main ( void )
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;
    
    for ( int i = 0; i < n; i++ )
    {
        int k;
        string str;
        cin >> k >> str;
        
        int ans = 0, cur = 0;
        
        for ( int j = 0; j <= k; j++ )
        {
            if ( cur < j )
            {
                ans += j - cur;
                cur = j;
            }
            
            cur += str[j] - '0';
        }
        
        printf ( "Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}

