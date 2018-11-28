#include<bits/stdc++.h>
using namespace std;

void solve(){
    double c,f,x,cur=0,ans=1e9,per_sec=2;
    scanf("%lf%lf%lf",&c,&f,&x);
    for(int i=0;i<2e5;i++){
        double to_end=x/per_sec,to_next;
        ans=min(ans,cur+to_end);
        to_next=c/per_sec;
        cur+=to_next;
        per_sec+=f;
    }
    printf("%lf",ans);
}

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("2.txt","w",stdout);

    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
        printf("\n");
    }

    return 0;
}
