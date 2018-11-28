#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<time.h>
#include<stdlib.h>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#define LL long long
using namespace std;
int main()
{
    //freopen("in.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int cse = 1;
    while(T--)
    {
        int smax;
        string s;
        scanf("%d", &smax);
        cin >> s;
        int ans = 0;
        int sum = 0;
        int len = s.size();
        for(int i = 0; i < len; i++)
        {
            if(sum < i)
            {
                sum++;
                ans++;
            }
            sum += s[i] - '0';
        }
        printf("Case #%d: %d\n", cse++, ans);
    }
    return 0;
}
