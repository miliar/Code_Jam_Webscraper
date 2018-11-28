#include<bits/stdc++.h>
using namespace std;
int cnt[1000+10];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,Case=0,d,p,ans,mp;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&d);
        memset(cnt,0,sizeof(cnt));
        mp=0;
        for(int i=0;i<d;i++){
            scanf("%d",&p);
            cnt[p]++;
            if(p>mp)mp=p;
        }
        ans=mp;
        for(int i=1;i<=mp;i++){
            int cc=i;
            int tcnt[1000+10]={};
            for(int j=0;j<=mp;j++)tcnt[j]=cnt[j];

            for(int j=mp;j>i;j--){
                if(tcnt[j]){
                    cc+=tcnt[j];
                    tcnt[i]+=tcnt[j];
                    tcnt[j-i]+=tcnt[j];
                    tcnt[j]=0;
                }
            }
            if(ans>cc)ans=cc;
        }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
