#include<stdio.h>
#include<stdlib.h>
int n,a[102];
int com(const void*a,const void*b){
    return *(int*)a-*(int*)b;
}
int mainx(int g)
{
    int op,x;
    scanf("%d%d",&x,&n);
    op = n;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    qsort(a,n,sizeof(int),com);
    for(int i=0;i<n;i++)
    {
        int A = x, o = i;
        for(int j=0;j<n-i;j++)
        {
            if(A==1 && A<=a[j]){
                o=100000;
                break;
            }
            while( A <= a[j]){ A+=A-1; o++; }
            A += a[j];
        }
        if(o<op)op=o;
    }
    printf("Case #%d: %d\n",g,op);
}
int main(){
    freopen("mote2.in","r",stdin);
    freopen("mote2.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        mainx(i+1);
    }
}
