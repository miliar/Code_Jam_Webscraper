/*
Shamim Ehsan
SUST CSE 12
*/
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
#include<sstream>
#define PI (2* acos(0))
#define pb push_back
#define ll long long
using namespace std;
//int X[]= {0,0,1,-1};
//int Y[]= {-1,1,0,0};
//int X[]= {0,0,1,1,1,-1,-1,-1};
//int Y[]= {-1,1,0,1,-1,0,1,-1};
int main()
{

    int t,n,r,c;
    freopen("D-small-attempt8.in","r",stdin);
    freopen("outpu.txt","w",stdout);

    scanf("%d",&t);
    for(int cs=1; cs<=t; cs++)
    {
        scanf("%d %d %d",&n,&r,&c);
        if(r>c)
        swap(r,c);
//        if(r*c==n)
//        {
//                    printf("Case #%d: RICHARD\n",cs);
//                continue;
//        }
        if(n==4)
        {
            if(r==1)
                printf("Case #%d: RICHARD\n",cs);
            if(r==2)
            {
                printf("Case #%d: RICHARD\n",cs);


            }
            if(r==3)
            {
                if(c==3)
                    printf("Case #%d: RICHARD\n",cs);
                else
                    printf("Case #%d: GABRIEL\n",cs);

            }
            if(r==4)
                printf("Case #%d: GABRIEL\n",cs);

        }
        else if(n==1)
        {
            printf("Case #%d: GABRIEL\n",cs);
        }
        else if(n==2)
        {
            if((r*c)%2==0)
                printf("Case #%d: GABRIEL\n",cs);
            else
                printf("Case #%d: RICHARD\n",cs);

        }
        else if(n==3)
        {
            if(r==1)
            {
                printf("Case #%d: RICHARD\n",cs);
                continue;
            }
            if(r==2)
            {
                if(c%3!=0)
                    printf("Case #%d: RICHARD\n",cs);
                else
                    printf("Case #%d: GABRIEL\n",cs);
                continue;
            }
            if(r==3)
            printf("Case #%d: GABRIEL\n",cs);
            if(r==4)
            printf("Case #%d: RICHARD\n",cs);

        }
    }
    return 0;
}


