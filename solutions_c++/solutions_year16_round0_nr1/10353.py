#include <stdio.h>
#include <string.h>
int Digit(int n);
int a[20];
int main()
{
    int t,n,i,j;
    freopen("A-large.in","r",stdin);
    freopen("CodejamAlarge.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",i);
        else{
        int max=Digit(n);
            printf("Case #%d: %d\n",i,max);
        }
        memset(a,0,sizeof(a));

    }
    return 0;

}
int Digit(int n){

    int i=2,j;
    int b=n;
    while(1){
        int num=b;
        while(num!=0){
            int x=num%10;
            num=num/10;
            a[x]=1;


        }
        int flag=0;
        for(j=0;j<10;j++)
        {
            if(a[j]!=1){
                flag=1;
                break;

            }
        }
        if(flag==0)
            break;

        b=n*i;
        i++;
    }
    return b;
}
