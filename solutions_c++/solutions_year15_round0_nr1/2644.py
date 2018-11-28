#include<stdio.h>

int T;
int N;
int Sum;
int Count;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&T);

    int i,j;

    char a;

    for(i=1;i<=T;i++){
        scanf("%d",&N);

        Sum=0;
        Count=0;

        for(j=1;j<=N+1;j++){
            scanf(" %c",&a);
            Sum+=(a-'0');

            if(j>Sum){
                Count++;
                Sum++;
            }
        }

        printf("Case #%d: %d\n",i,Count);
    }
}
