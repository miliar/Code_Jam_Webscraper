#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ao.txt","w",stdout);
    int t,in;
    scanf("%d",&t);
    for(in=1;in<=t;in++)
    {
        int n,i,ans1,ans2,md;
        int a[1005]={0};
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
        ans1 = ans2 = md = 0;

        for(i=1;i<n;i++)
            {

                if(a[i]<a[i-1]){
                    ans1+=a[i-1]-a[i];
                    if(a[i-1]-a[i]>md)md = a[i-1]-a[i];
                }
            }
            for(i=0;i<n-1;i++)
            {
                ans2+= (a[i]>md)?md:a[i];
            }
            printf("Case #%d: %d %d\n",in,ans1,ans2);
    }


}
