#include<cstdio>
#include<cmath>
long long int palindrome(long long int x)
{
    long long int num,j,digit,rev=0;
    num=x;
 
    do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while(num!=0);
    if(x==rev)
    return 1;
    else
    return 0;
    }
int main()
{
    long long int a,b,test,i,j,k,palind,count=0,sq,g,fair=0,palind2;
    scanf("%lld",&test);
    g=1;
    while(test--)
    {
        scanf("%lld %lld",&a,&b);
        for(i=a;i<=b;i++)
        {
           palind=palindrome(i);
            sq=sqrt(i);
           k=sq;
           //printf("%lld\n",sq);
            sq=sq*sq;
            if(sq==i)
       {    
           
       palind2=palindrome(k);
       
       }
            
            if(palind==1&&palind2==1)
        { //  printf("%lld",i);
            count++;}
            palind=0;
            palind2=0;
            }
            printf("Case #%lld: ",g);
            printf("%lld\n",count);
            g++;
            count=0;
palind=0;
palind2=0;
        }
}
