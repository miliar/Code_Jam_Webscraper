#include <iostream>
#include<stdio.h>
using namespace std;

int func(int i,int R,int C)
{
    int answer = 0;
    for (int r = 0; r < R; r++)
    {
        for (int c = 0; c < C; c++)
        {
            if (c > 0 and (i & (1 << (r * C + c))) and (i & (1 << (r * C+ c - 1))))
                answer++;
            if (r > 0 and (i & (1 << (r * C + c))) and (i & (1 << (r * C + c - C))))
                answer++;
        }
    }
    return answer;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int arr[1 << 20];
    int t;
    cin >> t;
    for (int k = 1; k<= t; k++)
    {
        int r,c,n;
        scanf("%d %d %d",&r,&c,&n);
        int pos=r*c;
        int ans=r*c*n*100;
        for (int i = 1; i < (1 << pos); i++)
        {
            arr[i] = arr[i - (i & -i)] + 1;
            if (arr[i] == n) ans = min(ans, func(i,r,c));
        }
        printf("Case #%d: %d\n", k, ans);
    }
}
