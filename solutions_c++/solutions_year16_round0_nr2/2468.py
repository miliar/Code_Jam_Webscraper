#include <bits/stdc++.h>

using namespace std;

int T,S;

int main()
{
    scanf("%d",&T);
    getchar();
    int count = 0;
    for(int i = 1; i<=T; ++i)
    {
        bool b = false; 
        char c = getchar();
        while( c != '\n' )
        {
            while( cin.peek() == c )
            {
                getchar();
            }
            if( c == '+' ) b = true;
            else b = false;
            c = getchar();
            ++count;
        }
        if( b ) --count;
        printf("Case #%d: %d\n",i,count);
        count = 0;
    }
}
