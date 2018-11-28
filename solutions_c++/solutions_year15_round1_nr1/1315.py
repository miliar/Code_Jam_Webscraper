#include<bits/stdc++.h>
using namespace std;
int a[1005];
int main()
{
    int T,it,N,i;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for(it=1; it<=T; it++)
    {
        scanf("%d",&N);
        for(i=0; i<N; i++)  scanf("%d",&a[i]);
        int y,z;
        y=0,z=0;
        for(i=1; i<N; i++)
        {
            if(a[i-1]>a[i])  y+=a[i-1]-a[i];
        }
        int mx=0;
        for(i=1; i<N; i++)
        {
            if(a[i-1]>a[i]) mx=max(mx,a[i-1]-a[i]);
        }
        for(i=0; i<N-1; i++)
        {
            if(a[i]>mx)  z+=mx;
            else z+=a[i];
        }
        printf("Case #%d: %d %d\n",it,y,z);
    }
    return 0;
}
