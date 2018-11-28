#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for( int tt=1; tt<=t; tt++ )
    {
        string stack;
        cin >> stack;
        
        char last = '0';
        int cnt = 0;
        for( string::iterator it=stack.begin(); it!=stack.end(); it++ )
        {
            if( *it != last )
            {
                last = *it;
                cnt++;
            }
        }
        if( *(stack.rbegin()) == '+' )
            cnt--;
        
        printf("Case #%d: %d\n", tt, cnt);
    }
    return 0;
}