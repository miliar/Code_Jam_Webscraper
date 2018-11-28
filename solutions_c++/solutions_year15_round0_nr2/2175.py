//#define LOCAL
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int Cas;
int a[1005],b[1005];
int main(){
    #ifdef LOCAL
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    #endif
    int T,d,l,ans,cnt,pos;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            scanf("%d",&a[i]);
        }
        sort(a,a+d);
        l=a[d-1];
        ans=a[d-1];
        for(int t=1;t<=l;t++){
            cnt=t;
            for(int i=0;i<d;i++)
                b[i]=a[i];
            for(int i=d-1;i>=0;i--){
                pos=1;
                if(b[i]<t)break;
                cnt+=(b[i]/t-1);
                if(b[i]%t)cnt++;
            }
        //cout<<t<<" "<<cnt<<endl;
        ans=min(ans,cnt);
        }
        printf("Case #%d: ",++Cas);
        printf("%d\n",ans);
    }
    return 0;
}
