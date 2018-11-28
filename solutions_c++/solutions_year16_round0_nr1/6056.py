// Bis-mil-lah

#include<bits/stdc++.h>

using namespace std;



int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int arr[13];

    int tc;
    cin>>tc;

    for(int cas=1;cas<=tc;cas++){
        int n;cin>>n;
        if( n==0 ) {
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }
        memset(arr,0,sizeof arr);
        int res = 0;
        for(int i=1;i<=30000;i++) {
            int m = n*i;
            while( m ) arr[ m%10 ] = 1 , m/=10;
            int cnt = 0;
            for(int dg=0;dg<=9;dg++) cnt+=arr[dg];
            if( cnt==10 ) {
                res = i*n;
                break;
            }
        }

        printf("Case #%d: %d\n",cas,res);
    }



    return 0;
}

