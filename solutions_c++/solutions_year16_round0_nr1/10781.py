#include<stdio.h>
#include<cstring>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,N,cc,an,i,ii;
    bool ud[12],yes;
    scanf("%d",&T);
    for(cc=1;cc<=T;cc++){
        scanf("%d",&N);
        an=1;
        memset(ud,0,sizeof(ud));
        yes=false;
        for(ii=1;ii<=1000;ii++){
            int x=N*ii;
            do{    
                ud[x%10]=true;
                x/=10;
            }while(x!=0);
            
            for(i=0;i<=9;i++){
                if(!ud[i])break;
            }
            if(i>9){
                yes=true;
                printf("Case #%d: %d\n",cc,N*ii);
                break;
            }
        }
        if(!yes)printf("Case #%d: INSOMNIA\n",cc);
        
    }
    return 0;
}
