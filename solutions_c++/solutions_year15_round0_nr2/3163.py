#include <cstdio>
#include <iostream>
using namespace std;

int x[10000];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,d;
    int cas = 1;
    cin>>t;
    while(t--){
        cin>>d;
        for(int i=0;i<d;i++){
            scanf("%d",&x[i]);
        }
        int ans = 0x3f3f3f3f;
        for(int i=1;i<=1000;i++){
            int tmp = 0;
            for(int j=0;j<d;j++){
                if(x[j]<=i)continue;
                int tt = x[j]-i;
                while(tt>0){
                    tmp ++;
                    tt -= i;
                }
            }
            ans = min(ans, tmp+i);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
