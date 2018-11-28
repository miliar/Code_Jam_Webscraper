#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int is_palindrome(long long int a)
{
    char tmp[100];
    int l,flag = 0,i,j;
    sprintf(tmp, "%lld", a);
    l = strlen(tmp);
    //printf("%d\n",l);
    for(i=0,j=l-1;i<j;i++,j--)
    {
        if(tmp[i] != tmp[j])
        {
            flag = 1;
            break;
        }
    }
    if(flag == 1)
    return 0;
    return 1;

}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("Q3out.txt","w",stdout);
    long long int n , m ,t ,tmp ,i,mrt,nrt,count;
    scanf("%lld",&t);
    tmp = 0;
    while(tmp != t)
        {
            count = 0;
            scanf("%lld",&n);
            scanf("%lld",&m);
            nrt = (long long int) pow((long double)n,0.5);
            mrt = (long long int) pow((long double)m,0.5);
            if(nrt*nrt != n)
            nrt++;
            for(i=nrt; i<=mrt;i++)
            {
                if(is_palindrome(i) && is_palindrome(i*i))
                {
                count++;
                }
            }
            //printf("%lld root of n ... %lld root of m\n Count is %lld\n",nrt,mrt,count);
            printf("Case #%lld: %lld\n",tmp+1,count);
            tmp++;
        }
    return 0 ;
}
