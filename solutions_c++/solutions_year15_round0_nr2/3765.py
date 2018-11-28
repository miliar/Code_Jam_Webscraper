#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
const int N=1010;
int d[N];

int main(){
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int T,n;
   cin >> T;
   for(int t=1;t<=T;t++){
        cin >> n;
        memset(d,0,sizeof(d));
        int ans=0,w=0;
        for(int i=0;i<n;i++) {
            cin >> d[i];
            w=max(w,d[i]);
        }
        ans=w;
        //cout << ans;
        for(int i=1;i<=w;i++){
            int c=0;
            for(int j=0;j<n;j++){
                c+=(d[j]-1)/i;
            }
            ans=min(c+i,ans);
        }

        printf("Case #%d: %d\n",t,ans);

   }
    return 0;
}
