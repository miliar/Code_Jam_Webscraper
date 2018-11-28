#include<stdio.h>
int main(){
    freopen("C:\\Users\\WAhid\\Desktop\\Round 1A\\A-large (1).in","r",stdin);
    freopen("C:\\Users\\WAhid\\Desktop\\Round 1A\\output.txt","w",stdout);
long long i,t,cas=0,n,m[10005],y,z,d,max_d,a;
scanf("%lld",&t);
while(t--){
        y=z=max_d=0;
    scanf("%lld",&n);
    for(i=0;i<n;i++){
        scanf("%lld",&m[i]);
    }
    n--;
    for(i=0;i<n;i++){
        d=m[i]-m[i+1];
    if (max_d<d) max_d=d;
        if(d>0) y+=d;
    }

    for(i=0;i<n;i++){
        if(m[i]<max_d) z+=m[i];
        else z+=max_d;
    }
    printf("Case #%lld: %lld %lld\n",++cas,y,z);


}
}
