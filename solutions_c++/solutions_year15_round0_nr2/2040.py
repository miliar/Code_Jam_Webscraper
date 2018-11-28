#include<cstdio>
#include<algorithm>

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int t,n,pancake[1000],i,j,k,temp,ans;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d",&n);
        for(j=0;j<n;j++){
            scanf("%d",&pancake[j]);
        }
        std::sort(pancake,pancake+n);
        ans=2147483647;
        for(j=1000;j>=1;j--){
            temp=0;
            for(k=n-1;k>=0;k--){
                temp+=((pancake[k]-1)/j);
            }
            if(temp+j<ans){
                ans=temp+j;
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}

