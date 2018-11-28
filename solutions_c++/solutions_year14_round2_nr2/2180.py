#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<stack>
#include<map>
#include<set>
#include<queue>
#include<vector>
#define pi (2*acos(0))
#define SF scanf
#define SFd1(a) scanf("%d",&a)
#define SFd2(a,b) scanf("%d%d",&a,&b)
#define SFd3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define PF printf
#define inf 99999999
#define eps 0.00000001
#define ll long long
#define ull long long unsigned
#define fr(i,n) for(i=0;i<n;i++)
#define dist(x1,y1,x2,y2) sqrt( ((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)) )
using namespace std;
//int rr[]={1,2,-1,-2,1,2,-1,-2};
//int cc[]={2,1,2,1,-2,-1,-2,-1};

ull i,j,res,t,l,k,p,a,b;

main()
{
    FILE *read,*write;
    read=fopen("new_lottery_game_in.txt","r");
    write=fopen("new_lottery_game_out.txt","w");
    fscanf(read," %llu",&t);
    for(p=1;p<=t;p++)
    {
        fscanf(read," %llu %llu %llu",&a,&b,&k);
        res=0LLU;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                    res++;
            }
        }
        fprintf(write,"Case #%llu: %llu\n",p,res);
    }
    fclose(read);
    fclose(write);
    return 0;
}

