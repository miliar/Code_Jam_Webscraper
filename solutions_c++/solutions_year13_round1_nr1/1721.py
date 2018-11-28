//Author : r20rock
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
#include<climits>
#include<iomanip>

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
#define 	NL	printf("\n")

int main()
{
    ULL tc,r,t;
    GETULL(tc);
    for(int i=1;i<=tc;i++)
    {
        ULL rt=0;
        GETULL(r);
        GETULL(t);
        rt=t;
        ULL n=1;
        while( (2*n*r) + (2*n*n - (n))<=rt)
        {
            n++;
        }

        PUTK("Case #");
        PUTI(i);
        PUTK(": ");
        PUTULL(n-1);
        NL;
    }
	return 0;
}
