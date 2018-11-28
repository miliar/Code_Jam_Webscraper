#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int T;
int n,l,r,mid,ans;
int a[1100];
int get(int p){
    int t=0;
    for (int i=1;i<=n;i++)
        t+=(a[i]-1)/p;
    return p+t;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (int tt=1;tt<=T;tt++){
        scanf("%d",&n);
        l=1001; r=-1;
        for (int i=1;i<=n;i++) {
            scanf("%d",&a[i]);
            l=min(a[i],l);
            r=max(a[i],r);
        }
        ans=1<<30;
        for (int i=1;i<=1000;i++)
            ans=min(ans,get(i));
        printf("Case #%d: %d\n",tt,ans);
    }
}

