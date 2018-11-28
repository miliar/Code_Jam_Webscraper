#include<stdio.h>
#define ll long long
using namespace std;

int main(){
    ll tt;
    scanf("%lld",&tt);
    for(ll lv=1;lv<=tt;lv++){
		printf("Case #%lld: ",lv);
        ll n;
        scanf("%lld",&n);
        ll arr[n];
        ll max=-1;
        for( ll lv1=1;lv1<=n;lv1++){
            scanf("%lld",&arr[lv1-1]);
        }
        ll ans=0;
        ll maxd=-1;
        ll ans2=0;
        for( ll lv1=1;lv1<=n-1;lv1++){
            if(arr[lv1]<arr[lv1-1]){
                ans=ans+arr[lv1-1]-arr[lv1];
                if(maxd<arr[lv1-1]-arr[lv1]){
                    maxd=arr[lv1-1]-arr[lv1];
                }
            }
        }
        if(maxd>0){
        for(ll lv1=1;lv1<=n-1;lv1++){
            if(arr[lv1-1]>=maxd){
                ans2=ans2+maxd;
            }
            else{
                ans2=ans2+arr[lv1-1];
            }
        }}
        printf("%lld %lld\n",ans,ans2);
    }
    return 0;
}
