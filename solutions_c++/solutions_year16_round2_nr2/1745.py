///////////////////
//  Shamim Ehsan //
//  SUST CSE 12  //
//  2012331035   //
///////////////////
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#define PI (2* acos(0))
#define push_back pb
using namespace std;
//int X[]= {0,0,1,-1};
//int Y[]= {-1,1,0,0};
//int X[]= {0,0,1,1,1,-1,-1,-1};
//int Y[]= {-1,1,0,1,-1,0,1,-1};
char one[15],two[15],a1[15],a2[15];
int cs;
int an1,an2,ab=1<<29;
bool check(int len)
{
    //` printf("%s %s %s %s\n",one,two,a1,a2);
    for(int i=0; i<len; i++)
    {
        if(one[i]=='?')continue;
        if(one[i]!=a2[i])return false;
    }
    for(int i=0; i<len; i++)
    {
        if(two[i]=='?')continue;
        if(two[i]!=a1[i])return false;
    }
    return true;
}
void f1()
{
   // puts("asfa");
    int an1,an2,ab=1<<29;
    for(int i=0; i<=9; i++)
        for(int j=0; j<=9; j++)
        {
            sprintf(a1,"%d",i);
            sprintf(a2,"%d",j);
            if(check(1))
            {
                if(abs(i-j)<ab)
                {
                    ab=abs(i-j);
                    an1=j;
                    an2=i;
                }
                //printf("Case #%d: %d %d\n",cs,j,i);
                //return;
            }
        }
    printf("Case #%d: %d %d\n",cs,an1,an2);

    return;
}
void f2()
{
    int an1,an2,ab=1<<29;
    for(int i=0; i<=99; i++)
    {
        //printf("%d \n",i);
        for(int j=0; j<=99; j++)
        {
            // printf("%d %d\n",i,j);
            // puts("asf");
            sprintf(a1,"%02d",i);
            sprintf(a2,"%02d",j);
            if(check(2))
            {
                if(abs(i-j)<ab)
                {
                    ab=abs(i-j);
                    an1=j;
                    an2=i;
                }
            }
        }

    }

    printf("Case #%d: %02d %02d\n",cs,an1,an2);

    return;
}
void f3()
{

    for(int i=0; i<=999; i++)
        for(int j=0; j<=999; j++)
        {
            sprintf(a1,"%03d",i);
            sprintf(a2,"%03d",j);
            if(check(3))
            {
                if(abs(i-j)<ab)
                {
                    ab=abs(i-j);
                    an1=j;
                    an2=i;
                }
            }
        }
    printf("Case #%d: %03d %03d\n",cs,an1,an2);
    return;
}
int main()
{

    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for( cs=1; cs<=t; cs++)
    {
        ab =1<<29;
        scanf("%s %s",one,two);
        if(strlen(one)==1)
            f1();
        if(strlen(one)==2)
            f2();
        if(strlen(one)==3)
            f3();
       // printf("Case #%d: %d %d",cs,an1,an2);
    }
    return 0;
}


