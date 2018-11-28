#include<stdio.h>
#include<cstdlib>
long a,b,mat[10][10],t,i,j,k,p[10],p2[10];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    scanf("%ld",&t);
    for(int w=1;w<=t;w++){
        b=0;
        scanf("%ld",&a);
        for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%ld",&mat[i][j]);
        for(j=0;j<4;j++) p[j]=mat[a-1][j];
        scanf("%ld",&a);
        for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%ld",&mat[i][j]);
        for(j=0;j<4;j++) p2[j]=mat[a-1][j];
        for(i=0;i<4;i++)            for(j=0;j<4;j++){
            if(p[i]==p2[j]){
                b++;
                k=p[i];
            }
        }
        if(b==1) printf("Case #%d: %ld\n",w,k);
        else if(b>1) printf("Case #%d: Bad magician!\n",w);
        else if(b==0) printf("Case #%d: Volunteer cheated!\n",w);
    }
}
