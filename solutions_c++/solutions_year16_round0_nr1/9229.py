#include<stdio.h>



int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

    int a,b,c,i,j,k,sum;
    int numb[10];
    int TC,N;
    while(scanf("%d",&N)!=EOF)
    {


for(TC=1;TC<=N;TC++)
{
    scanf("%d",&a);
    if(a==0){printf("Case #%d: INSOMNIA\n",TC);continue;}
    for(i=0;i<10;i++)
    {
        numb[i]=0;
    }
    for(i=1;;i++)
    {
        b=i*a;
        while(b>0)
        {
            numb[b%10]=1;
            b=b/10;
        }

        sum=0;

        for(j=0;j<10;j++)
        {
            sum=sum+numb[j];
        }

  //      printf("%d\n",i*a);
        if(sum==10){printf("Case #%d: %d\n",TC,i*a);break;}
    }

}    }
return 0;
}
