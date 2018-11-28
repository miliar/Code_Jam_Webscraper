#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,a,b[10],T,i,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>a;
        for(i=0;i<a;i++) cin>>b[i];
        sort(b,b+a);
        T=0;
        for(;b[a-1]>3;)
        {
            b[a-1]=b[a-1]/2+b[a-1]%2;
            sort(b,b+a);
            T+=1;
        }
        if(b[a-1]<=3) T+=b[a-1];
        printf("Case #%d: %d\n",j,T);
    }
    return 0;
}
