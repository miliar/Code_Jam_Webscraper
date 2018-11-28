#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int a[105];
int ans[105];
int main()
{
    //freopen("C:\\codejam\\A-small-attempt1.in","r",stdin);
    //freopen("C:\\codejam\\a.out","w",stdout);
    int T,n,A;
    int out = 1;
    scanf("%d",&T);
    while(T--)
    {
        ans[0]=0;
        scanf("%d",&A);
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        sort(a+1,a+1+n);
        for(int i=1;i<=n;i++)
        {
            if(A>a[i]) {A+=a[i];ans[i]=ans[i-1];}
            else{
                ans[i]=ans[i-1];
                if(A==1) {ans[i]=1000;continue;}
                while(A<=a[i]){
                    A=A+A-1;
                    ans[i]++;
                }
                A+=a[i];
            }
        }
        int outans = 1000;
        for(int i=1;i<=n+1;i++){
            if(ans[i-1]+(n-(i-1))<outans) outans = ans[i-1]+(n-(i-1));
        }
        printf("Case #%d: %d\n",out++,outans);
    }
    return 0;
}
