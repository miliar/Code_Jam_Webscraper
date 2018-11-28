#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <string>

using namespace std;

#define read(x) scanf("%d",&x)
#define dbg(x) cout<<#x<<" = "<<x<<endl
#define INF 1000000000

int T,n,q,c,ans,cased;
string str;

int main(){
    freopen("hello.in","r",stdin);
    freopen("hello.out","w",stdout);
    read(T);

    while(T--){cased++;q=0;ans=0;
      read(n);cin>>str;
      for(int k=0;k<=n;k++){
        c=str[k]-48;
        if(q>=k)q+=c;
        if(q<k){ans+=k-q;q+=c+k-q;}
      }
       cout<<"Case #"<<cased<<": "<<ans<<endl;
    }
   return 0;
}
