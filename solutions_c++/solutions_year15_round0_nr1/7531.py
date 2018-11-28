#include<bits/stdc++.h>
using namespace std;
#define MAX 1100
int shy[MAX];
int main()
{
    ios_base ::sync_with_stdio(false);
    cin.tie(0);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tcase, t;
    cin >> tcase;
    string str;
    int ans, smax, sum;
    for(t = 1; t <= tcase; t++)
    {
        cin >> smax;
        cin >> str;
        for(int i = 0; i <= smax; i++) shy[i] = (str[i] - '0');
        ans = 0;
        sum = shy[0];
        for(int i = 1; i<=smax; i++)
        {
            if(i > sum)
            {
                ans += i - sum;
                sum += i - sum + shy[i];
            }
            else
            {
                sum += shy[i];
            }

        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
