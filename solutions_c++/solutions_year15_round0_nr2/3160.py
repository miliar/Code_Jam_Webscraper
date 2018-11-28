#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
#include<set>
#define ll long long
using namespace std;
int a[10010];
int t,cas=1;
int main(){
    freopen("B-large1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        int n,ans=100000,k;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        for(int i=1;i<=1000;i++){
            k=i; 
            for(int j=0;j<n;j++) k+=(a[j]-1)/i;
            ans=min(ans,k);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
