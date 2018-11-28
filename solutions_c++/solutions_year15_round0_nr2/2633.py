#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <queue>
using namespace std;
const int N = 1050;

int a[N];
int n;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int x=1; x<=t; x++)
    {
        scanf("%d", &n);
        int ans = 0;
        for(int i=0; i<n; i++)
        {
            scanf("%d", &a[i]);
            ans = max(a[i], ans);
        }
        for(int i=ans; i>=1; i--)
        {
            int temp = i;
            for(int j=0; j<n; j++)
            {
                if(a[j] > i)
                {
                    temp += a[j]/i+(a[j]%i==0?0:1)-1;
                }
            }
            ans = min(temp, ans);
        }
        printf("Case #%d: %d\n", x, ans);
    }
    return 0;
}
