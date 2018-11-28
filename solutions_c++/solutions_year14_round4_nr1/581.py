#include<stdio.h>

int cnt[1001]={0};
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n,x;
    int t,t2;
    int i,temp,ans=0;
    scanf("%d",&t2);
    for(t=1;t<=t2;t++){
        ans = 0;
        if(t==68){
            t ++;
            t--;
        }
        scanf("%d%d",&n,&x);
        for(i=1;i<=x;i++) cnt[i] = 0;
        for(i=0;i<n;i++){
            scanf("%d",&temp);
            cnt[temp]++;
        }
        ans += cnt[x];
        if(x>1){
            for(i=x-1;i>x/2;i--){
                if(cnt[i] >= cnt[x-i]){
                    ans += cnt[i];
                    cnt[x-i] = cnt[i] = 0;
                }
                else{
                    ans += cnt[i];
                    temp = cnt[x-i] - cnt[i];
                    cnt[x-i] = cnt[i] = 0;
                    cnt[x-i+1] += temp;
                }
            }
            if(cnt[x-x/2]%2 == 1) ans++;
            ans += cnt[x-x/2]/2;
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
