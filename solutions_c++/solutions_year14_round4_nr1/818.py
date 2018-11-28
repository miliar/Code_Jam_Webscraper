#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int s[20000];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T, n, X;
    scanf("%d", &T);
    for(int cas = 1 ; cas <= T ; cas++)
    {
        scanf("%d%d", &n, &X);
        for(int i = 0 ; i < n ; i++)
            scanf("%d", &s[i]);
        sort(s, s + n);
        int i = 0, j = n - 1, ans = 0;
        while(i <= j)
        {
            ans++;
            if(i == j)break;
            if(s[i] + s[j] > X)j--;
            else               {i++;j--;}
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
