#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
    int times;
    int data[10010];
    freopen("A-large (1).in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> times;
    for (int t = 0; t < times; t++){
        int n,x;
        scanf("%d %d",&n,&x);
        for (int i = 0; i < n; i++)
        {
            scanf("%d",&data[i]);
        }
        sort(data,data+n);
        int ans = 0;
        int cnt = 0;
        int p = 0;
        int pp = n-1;
        while (cnt < n)
        {
            if (data[p] + data[pp] <= x){
                cnt += 2;
                p++;pp--;
            }
            else{
                cnt ++;
                pp--;
            }
            ans ++;
        }
        printf("Case #%d: %d\n",t+1,ans);
    }
}
