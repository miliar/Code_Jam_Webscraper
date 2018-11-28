#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,w,n,m,r,c;
    freopen("A-large.in","r",stdin);
    freopen("A_large.txt","w",stdout);
    cin>>T;
    for( int ks=1;ks<=T;ks++ )
    {
        cin>>r>>c>>w;
        int ans=(c/w)*r+(w-1);
        if( c%w!=0 )ans++;
        printf("Case #%d: %d\n",ks,ans);

    }
    return 0;
}
