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
        int smax;
        cin >> smax;
        string shyness;
        cin >> shyness;
        
        int addition=0, cur=0;
        for( int i=0; i<=smax; i++ )
        {
            if( cur < i )
            {
                addition += i-cur;
                cur = i;
            }
            cur += shyness[i]-'0';
        }
        
        printf("Case #%d: %d\n", tt, addition);
    }
}