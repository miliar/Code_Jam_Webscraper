#include<stdio.h>
#include<math.h>
//long long
int main()
{
    long long i,test,t,r,paint,j,c,ttl,temp,count;
    freopen("C://Users//Sheemul//Downloads//A-small-attempt0.in","r",stdin);
    freopen("E://Anamul Kabir//output.txt","a",stdout);
    scanf("%lld",&test);
    for(t=1;t<=test;t++)
    {
        scanf("%lld %lld",&r,&paint);
        ttl=0;
        //int flg=2;
        c=r-1;
        count=0;
        while(1)
        {
            c+=2;
            temp=(c*c)-((c-1)*(c-1));
            if(ttl+temp>paint) break;
            ttl+=temp;
            count++;
        }
        printf("Case #%lld: %lld\n",t,count);
    }
    return 0;
}
