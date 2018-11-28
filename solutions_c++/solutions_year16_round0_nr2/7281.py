#include <iostream>
#include <cstdio>

using namespace std;

void solve()
{
    string s, k;
    char zap = '#';
    cin >> s;
    for(int i = 0 ; i < (int)s.size() ; i++)
    {
        if(s[i] != zap)
        {
            zap = s[i];
            k.push_back(zap);
        }
    }
    int roz = (int)k.size();
    if(roz % 2 == 0)
    {
        if(k[0] == '+')
            printf("%d\n", roz);
        else
            printf("%d\n", roz-1);
    }
    else
    {
        if(k[0] == '+')
            printf("%d\n", roz-1);
        else
            printf("%d\n", roz);
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 1 ; i <= t ; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
}
