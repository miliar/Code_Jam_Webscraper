#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
#include<set>
#define ll long long
using namespace std;
int a[1010];
int main(){
    int t,cas=1;
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        int n,ans=111100;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        for(int i=1;i<=2000;i++){
            int res=i;
            for(int j=0;j<n;j++) res+=(a[j]-1)/i;
            ans=min(ans,res);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
