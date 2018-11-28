#include<cstdio>

int main(){
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T,N;
    scanf("%d",&T);
    int expectcnt=(1<<10)-1;
    for(int t=0;t<T;t++){
        scanf("%d",&N);
        int mul=0;
        int cnt=0,tmp;
        while(mul<=2000000000 && N>0){
            mul+=N;
            tmp=mul;
            while(tmp>0){
                cnt=cnt|(1<<(tmp%10));
                tmp=tmp/10;
            }
            //if(result<20) printf("%d, %d\n",cnt,mul);
            if(cnt==expectcnt) break;
        }
        if(cnt==expectcnt) printf("Case #%d: %d\n",t+1,mul);
        else printf("Case #%d: INSOMNIA\n",t+1);
    }
    return 0;
}
