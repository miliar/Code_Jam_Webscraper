#include<stdio.h>
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
    int allt,nowtest=0;
    scanf("%d",&allt);
    while(++nowtest <= allt){
        bool digit[11] = {};
        long long startn;
        int i=0,cnt=0;
        scanf("%d",&startn);
        //printf("%lld\n",startn);
        if(startn == 0){
            printf("Case #%d: INSOMNIA\n",nowtest,nowtest);
            continue;
        }
        while(++i){
            int idx=1;
            long long nown=startn*i;
            while(idx<=nown){

                long long nowdigit = (nown/idx)%10;
                if(digit[nowdigit] == false){
                    //printf(" %d ",nown);
                    digit[ nowdigit ] = true;
                    cnt++;
                }
                if(cnt==10){
                    break;
                }
                idx*=10;
            }
            if(cnt==10){
                printf("Case #%d: %lld\n",nowtest,nown);
                break;
            }
        }
    }
    return 0;
}
