#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<map>
#include<list>
#include<cmath>
#include<cstdlib>

using namespace std;

#define     PI      3.1428571
#define     UL      unsigned long int
#define     ULL      unsigned long long int

#define     GETI(k)      scanf("%d",&k)
#define     GETUL(k)    scanf("%lu",&k)
#define     GETULL(k)    scanf("%llu",&k)
#define     GETF(k)      scanf("%f",&k)
#define     GETC(k)     scanf("%c",&k)
#define     GETCP(k)   scanf("%s",&k) //char pointer
#define     GETS(k)     scanf("%s",k)  //string

#define     PUTI(k)     printf("%d",k)
#define     PUTUL(k)   printf("%lu",k)
#define     PUTULL(k)   printf("%llu",k)
#define     PUTF(k)     printf("%f",k)
#define     PUTC(k)     printf("%c",k)
#define     PUTS(k)     printf("%s",k)
#define     PUTK(k)     printf(k)           //hard coded string
#define     NL	printf("\n")

bool palindrome(int num)
{
    int n = num,rev=0,dig=0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if(n == rev)
        return  true;
    else
        return  false;
}

int main()
{
    int a,b,tc;
    GETI(tc);
    for(int t=1; t<=tc; t++)
    {
        int ans=0;
        GETI(a);
        GETI(b);
        double sqra = sqrt(a);
        int sqb = sqrt(b);
        int sqa = sqra;
        if(sqra-sqa)
            sqa++;

        for(int i=sqa; i<=sqb; i++)
            if(palindrome(i) && palindrome(i*i))
                ans++;

        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
