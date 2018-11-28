#include <stdio.h>

int* func(int a[], int n)
{
    int i, temp,t, m0=0, m1=0;
    int pos0=-1, pos1=-1;
    for(i=0;i<n;i++){
        if(a[i]>=m0){
            m1=m0;
            pos1=pos0;
            m0=a[i];
            pos0=i;
        }
        else if(a[i]>m1){
            pos1=i;
            m1=a[i];
        }
    }
    int b[2];
    b[0]=pos0;
    b[1]=pos1;
    return b;
}

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,i;
    scanf("%d",&T);
    int *p;
    for(i=0;i<T;i++){
        int N,j,k;
        scanf("%d",&N);
        int P[N];
        int sum=0;
        for(j=0;j<N;j++){
            scanf("%d",&P[j]);
            sum+=P[j];
        }
        printf("Case #%d:",i+1);
        p=func(P,N);
        int pos0=*p;
        int pos1=*(p+1);
        if(P[pos0]==P[pos1]){
            for(j=0;j<N;j++){
                if(j!=pos0&&j!=pos1){
                    for(k=0;k<P[j];k++){
                        printf(" %c",j+'A');
                    }
                }
            }
            for(j=0;j<P[pos0];j++){
                printf(" %c%c",pos0+'A',pos1+'A');
            }
        }
        else{
            for(j=0;j<P[pos0]-P[pos1];j++){
                printf(" %c",pos0+'A');
            }
            for(j=0;j<N;j++){
                if(j!=pos0&&j!=pos1){
                    for(k=0;k<P[j];k++){
                        printf(" %c",j+'A');
                    }
                }
            }
            for(j=0;j<P[pos1];j++){
                printf(" %c%c",pos0+'A',pos1+'A');
            }
        }
        printf("\n");
    }
    return 0;
}
