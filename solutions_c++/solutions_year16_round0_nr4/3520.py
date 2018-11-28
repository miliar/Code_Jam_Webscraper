#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test , k , c , s;
    cin >> test ;
    for(int i = 1 ; i <= test ;i++)
    {
        cin >> k >> c >> s ;
        printf("Case #%d:",i);
        if(s < k)
            cout << " IMPOSSIBLE" << endl ;
        else
        {
        for(int i = 1 ; i <= s ; i++)
            cout << " " << i;
        cout << endl ;
        }
    }
    return 0;
}
