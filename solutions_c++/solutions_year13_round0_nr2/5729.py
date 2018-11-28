#include<stdio.h>
#include<stdlib.h>
#define max(a,b) a>b? a:b
#define min(a,b) a<b? a:b
int w,h,a[102][102],b[102][102],V[102],H[102];
int cut(int x)
{
    int r=x;
    for(int i=0;i<h&&r>0;i++){
        if(r%2==1){
            for(int j=0;j<w;j++)
            {
                b[i][j]=1;
            }
        }
        r/=2;
    }
    for(int i=0;i<w&&r>0;i++){
        if(r%2==1){
            for(int j=0;j<h;j++)
            {
                b[j][i]=1;
            }
        }
        r/=2;
    }
}
int comp(int r){

    /*for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            printf("%d ",b[i][j]);
        }
        printf("\n");
    }*/

    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            if(a[i][j]!=b[i][j])return 0;
        }
    }
    return 1;
}
int calc(){
    scanf("%d%d",&h,&w);
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            scanf("%d",&a[i][j]);
            H[i]=max(H[i],a[i][j]);
            V[j]=max(V[j],a[i][j]);
            b[i][j]=100;
        }
    }
    for(int i=100;i>0;i--){
        for(int j=0;j<h;j++)
        {
            if(H[j]==i)
            {
                for(int k=0;k<w;k++)
                {
                    b[j][k]=i;
                }
            }
        }
        for(int j=0;j<w;j++){
            if(V[j]==i)
            {
                for(int k=0;k<h;k++)
                {
                    b[k][j]=i;
                }
            }
        }
    }
    return comp(0);
}
int main(){
    freopen("in22.in","r",stdin);
    freopen("out22.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int result=-1;
        result = calc();
        if(result==0)printf("Case #%d: NO\n",i+1);
        if(result==1)printf("Case #%d: YES\n",i+1);
        for(int i=0;i<100;i++){
            V[i]=-1;
            H[i]=-1;
        }
    }
}
