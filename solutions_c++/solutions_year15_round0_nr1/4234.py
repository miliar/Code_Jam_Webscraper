#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    freopen("standing_ovation.txt", "r", stdin);
    freopen("Question_1.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++)
    {
        int n;
        scanf("%d", &n);
        char arr[n + 2];
        cin >> arr;
        long long sum = 0, ans = 0;
        for(int i = 0; i <= n; i++)
        {
            if((arr[i] - '0') != 0)
            {
                if(i > sum)
                {
                    ans += i - sum;
                    sum += ans;
                }
                sum += arr[i] - '0';
            }
        }
        printf("Case #%d: %d\n", k, ans);
    }
    return 0;
}
