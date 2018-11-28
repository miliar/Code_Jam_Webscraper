#include <bits/stdc++.h>
using namespace std;
int d[1010];
int main(){
    int t;
    scanf("%d",&t);
    int ii=1;
    while(t--){
        int ans;
        int n;
        scanf("%d",&n);
        int i,j;
        int num=0;
        for(i=0;i<n;i++){
            scanf("%d",&d[i]);
            num=max(d[i],num);
        }
        ans=num;
        for(i=1;i<=num;i++){
            int temp=i;
            for(j=0;j<n;j++){
                if(d[j]>i){
                    temp+=d[j]/i;
                    if(d[j]%i==0)
                        temp--;
                }
            }
            ans=min(ans,temp);
        }
        printf("Case #%d: %d\n",ii++,ans);
    }
}