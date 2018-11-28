#include<bits/stdc++.h>
#define sf scanf
#define pf printf

using namespace std;

char str[105];
void flip(int pos)
{
    for(int i = pos ; i >= 0 ; --i)
    {
        if(str[i] == '+') str[i]= '-';
        else str[i] = '+';
    }
}

int main()
{
    freopen("input.txt" , "r" , stdin);
    freopen("output.in" , "w" , stdout);
    int t , len , cnt , cc = 0;
    sf("%d" , &t);
    while(t--)
    {
        cnt = 0;
        sf("%s" , str);
        len = strlen(str);
        for(int i = len - 1  ; i >= 0 ; --i)
        {
            if(str[i] == '-')
            {
                flip(i);
                ++cnt;
            }
        }
        pf("Case #%d: %d\n" , ++cc , cnt);
    }
    return 0;
}
