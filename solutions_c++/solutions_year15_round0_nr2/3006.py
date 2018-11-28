#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string>

using namespace std;

#define read(x) scanf("%d",&x)
#define dbg(x) cout<<#x<<" = "<<x<<endl
#define INF 1000000000

int T,n,q,c,ans,cased,x,test;
int a[2000];
int b[2000];

int main(){
    freopen("hello.in","r",stdin);
    freopen("hello.out","w",stdout);

    read(T);
    while(T--){ans=INF;test++;
        read(n);
        for(int k=1;k<=n;k++){
            read(x);a[x]++;
            b[k]=x;
        }
        for(int k=1000;k>=1;k--){q=0;
            for(int k2=1;k2<=n;k2++)q+=(b[k2]-1)/k;
            q+=k;
            ans=min(ans,q);
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
   return 0;
}
