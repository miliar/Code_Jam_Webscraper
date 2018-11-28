#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

char str[105];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int ti = 1; ti <= t; ti++)
    {
        cin >> str;
        int len = strlen(str);
        int sum = 0;
        for(int i = 1; i < len; i++)
        {
            if(str[i - 1] != str[i])
                sum++;
        }
        if(str[len - 1] == '-')
            sum++;
        printf("Case #%d: %d\n", ti, sum);
    }
    return 0;
}
