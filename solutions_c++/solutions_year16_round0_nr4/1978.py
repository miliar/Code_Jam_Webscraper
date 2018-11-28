#include<bits/stdc++.h>
using namespace std;
int T,n,k,c,s
;
int use[123456];
int main(){
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    scanf("%d",&T);
    for(int ti=1;ti<=T;ti++){
        printf("Case #%d: ",ti);
        scanf("%d%d%d",&k,&c,&s);
        if(c*s<k){
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(int i=0;i<k;i++) use[i]=0;
        int need=k;
        long long x;
        while(need){
            x=0;
            for(int i=0;i<c;i++){
                for(int j=0;j<k;j++)if(!use[j]){
                        use[j]=1;
                        x=x*k+j;
                        need--;
                        break;
                }
                if(need==0)break;
            }
            if(need==0)break;
            cout<<x+1<<" ";
        }
        cout<<x+1<<endl;
    }
}

