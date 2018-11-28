#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

const double PI = acos(-1.0);
const double e = 2.718281828459;
const double eps = 1e-8;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int Case;
    int num = 1;
    int n;
    cin>>Case;
    while(Case--)
    {
        string s;
        scanf("%d", &n);
        cin>>s;
        if(n == 0)
        {
            printf("Case #%d: 0\n", num++);
            continue;
        }
        int sum = 0;
        int extra = 0;
        for(int i = 0; i <= n; i++)
        {
            int t = s[i]-'0';
            if(sum >= i)
                sum += t;
            else
            {
                extra += (i-sum);
                sum += t+(i-sum);
            }
        }
        printf("Case #%d: %d\n", num++, extra);
    }
    return 0;
}

