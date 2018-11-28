#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++){
        int d;
        scanf("%d",&d);
        int p[d],lim=0;
        for(int i=0;i<d;i++){
            scanf("%d",&p[i]);
            lim=max(p[i],lim);
        }
        int ans=12345678;
        for(int i=1;i<=lim;i++){
            int sum=0,q=0;
            for(int j=0;j<d;j++){
                if(p[j]>i){
                    sum+=((p[j]+i-1)/i);
                    sum--;
                }
            }
            ans=min(ans,sum+i);
        }
        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
