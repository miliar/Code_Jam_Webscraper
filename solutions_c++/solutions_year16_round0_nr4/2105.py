#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#include<string.h>
#include<queue>
using namespace std;
#define ll long long
const int N=110;
ll ans[N];
int main()
{
#ifdef gh546
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
#endif // gh546
    int TAT; scanf("%d",&TAT);
    for(int cas=1;cas<=TAT;cas++){
        int k,c,s; scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",cas);
        if(s==k){
            for(int i=1;i<=s;i++) printf(" %d",i); printf("\n");
            continue;
        }
        if(c==1){
            if(s<k) printf(" IMPOSSIBLE\n");
            else{
                for(int i=1;i<=k;i++) printf(" %d",i); printf("\n");
            }
        }
        else{
            int flag=0,cnt=0,num=1; ll pos=0; int id=2;
            for(int i=k;i>0;i-=2){
                ans[cnt++]=pos+id; id+=2; num++;
                if(id>k) id=k;
                pos=pos+k*(id-1);
                if(num==c){
                    if(s-cnt<k-id) {flag=1;}
                    else{
                        for(int i=id;i<=k;i++) ans[cnt++]=pos+i;
                    }
                    break;
                }
            }
            if(flag){printf(" IMPOSSIBLE\n");}
            else{
                for(int i=0;i<cnt;i++) printf(" %d",ans[i]); printf("\n");
            }
        }
    }
    return 0;
}
