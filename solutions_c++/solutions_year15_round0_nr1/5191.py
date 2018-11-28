#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

int main()
{
    int T;
    freopen("codejam.ans", "w", stdout);
    cin >> T;
    int cas = 1;
    while(T --)
    {
        int Smax;
        string str;
        cin >> Smax >> str;
        int ans = 0;
        int cur = 0;
        for(int i=1; i<=Smax; i++)
        {
            cur += str[i-1] - '0';
            if(cur < i)
            {
                ans += i - cur;
                cur = i;
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
