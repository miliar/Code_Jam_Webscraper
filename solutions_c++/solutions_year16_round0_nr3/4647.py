#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int T,Case=0,n,m;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",++Case);
        int N=n/2;
        long long a=(1LL<<N)|1;
        for(int i=0;i<1<<(N-2)&&i<m;i++){
            long long tmp = a|(a<<(N-1));
            for(int j=0;j<N-2;j++){
                if(i&(1LL<<j))tmp|=(a<<(j+1));
            }
            //printf("%lld\n",tmp);
            char ans[50];
            int top=0;
            while(tmp){
                ans[top++]=tmp%2+'0';
                tmp/=2;
            }
            for(int x=0,y=top-1;x<y;x++,y--)swap(ans[x],ans[y]);
            ans[top]='\0';
            printf("%s",ans);
            for(int j=2;j<=10;j++){
                long long rr=0;
                for(int k=0;k<top;k++)rr=rr*j+ans[k]-'0';
                for(long long k=2;k*k<=rr;k++){
                    if(rr%k==0){
                        printf(" %d",k);
                        break;
                    }
                }
            }
            puts("");
        }
    }
    return 0;
}
