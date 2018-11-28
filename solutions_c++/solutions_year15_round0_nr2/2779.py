#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int s[1005];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        int n;
        scanf("%d", &n);
        for (int i=0; i<n; i++) {
            scanf("%d",s+i);
        }
        int ans = 0,cnt=0;
        for(int i=1; i<=1000; i++) {
            int tmp = 0;
            for(int j=0;j<n;j++) {
                if(s[j]%i ==0) tmp += s[j]/i - 1;
                else tmp += s[j]/i;
            }
            tmp += i;
            if (i==1 || ans > tmp) ans = tmp;
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
