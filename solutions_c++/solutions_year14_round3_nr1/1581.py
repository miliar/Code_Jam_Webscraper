#include<stdio.h>
#include<math.h>
//#include<conio.h>
long long gcd(long long,long long);
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1_out.txt","w",stdout);
    long long p=0,q=0,test,i,j,n,k,x;
    double f;
    char str[30];
    scanf("%lld",&test);
    for(i=0;i<test;i++)
    {
        scanf("%s",str);
        p=0;q=0;
        //printf("\nstr=%s\n",str);
        for(j=0;str[j]!='\/';j++)
        {
            //printf("\nstr[%d]=%c\n",j,str[j]);
            p=10*p+(str[j]-'0');
        }
        j++;
        for(;str[j]!='\0';j++)
        {
            q=10*q+(str[j]-'0');
        }
        //printf("\np=%d q=%d\n",p,q);
        //getch();
        if(p==0||q==0)
        {
            printf("Case #%lld: impossible\n",i+1);
            continue;
        }
        k=gcd(p,q);
        q=q/k;
        p=p/k;
        //printf("there\n");
        //getch();
        if((!(q&(q-1)))==0)
        {
            printf("Case #%lld: impossible\n",i+1);
            continue;
        }
        x=((long long)log2(q))-((long long)log2(p));
        printf("Case #%lld: %d\n",i+1,x);
    }
    return 0;
}
long long gcd(long long a,long long b)
{
    //printf("\na=%d b=%d",a,b);
    long long r,c;
    if(b>a)
    {
        c=b;
        b=a;
        a=c;
    }
    while ( a != 0 )
    {
     c = a;
     a = b%a;
     b = c;
    }
    //printf("\ngcd=%d",b);
    return b;
}
