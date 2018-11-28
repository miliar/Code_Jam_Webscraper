#include<bits\stdc++.h>
using namespace std;
main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,c=0;
    scanf("%d",&t);
    while(t--){
        int a,b,k,cnt=0;
        scanf("%d%d%d",&a,&b,&k);
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                if((i&j)<k)cnt++;
            }
        }
        printf("Case #%d: %d\n",++c,cnt);
    }
}

