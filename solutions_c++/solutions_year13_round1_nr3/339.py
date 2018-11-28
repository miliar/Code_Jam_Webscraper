#include <stdio.h>
#include <stdlib.h>

int r=100,n=3,m=5,k=7;
int table[100];

int possible(int a,int b,int c, int pro){
    if(pro==1){
        return 1;
    }
    if(pro==a || pro==b || pro==c){
        return 1;
    }
    if(pro==a*b || pro==b*c || pro==c*a){
        return 1;
    }
    if(pro==a*b*c){
        return 1;
    }
    return 0;
}

int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int i,j;
    int tt,zz;
    scanf("%d",&tt);
    scanf("%d%d%d%d",&r,&n,&m,&k);
    printf("Case #1:\n");
    for(i=1;i<=r;i++){
        for(j=1;j<=k;j++){
            scanf("%d",&table[j]);
        }
        for(int p=2;p<=m;p++){
            for(int q=2;q<=m;q++){
                for(int r=2;r<=m;r++){
                    for(j=1;j<=k;j++){
                        if(!possible(p,q,r,table[j])){
                            break;
                        }
                    }
                    if(j==k+1){
                        printf("%d%d%d\n",p,q,r);
                        p=m+1;
                        q=m+1;
                        r=m+1;
                    }
                }
            }
        }
    }
	return 0;
}
