#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<map>
#include<deque>
using namespace std;
unsigned long long int powerarr[60];
int main()
{
    freopen("sampleinput.txt","r",stdin);
    freopen("sampleout2.txt","w",stdout);
    int tnum,numtc;
    scanf("%d",&numtc);
    powerarr[0]=1;
    unsigned long long int two=2;
    int i;
    for(i=1;i<=60;i++)
       powerarr[i]=powerarr[i-1]*two;
    for(tnum=1;tnum<=numtc;tnum++)
    {
        unsigned long long int n,p;
        scanf("%llu%llu",&n,&p);
        unsigned long long int ans1,ans2;
        unsigned long long int temp1=powerarr[n],temp2,sub=1;
        temp2=temp1;
        if(p==temp1)
           ans2=temp1;
        else
        {
            while(1)
            {
                temp1/=2;
                temp2-=sub;
                if(temp1==0)
                   break;
                if(p>=temp1)
                {
                    ans2=temp2;
                    break;
                }
                sub*=2;
            }
        }

        temp1=powerarr[n];
        temp2=n+1;
        sub=1;
        if(p==temp1)
          ans1=temp1;
        else
        {
            while(1)
            {
                 temp2--;
                 temp1-=sub;
                 sub*=2;
                 if(temp1<=0)
                    break;
                 if(p>=temp1)
                 {
                     ans1=powerarr[temp2]-1;
                     break;
                 }
            }
        }
        ans1--;
        ans2--;

        printf("Case #%d: %llu %llu\n",tnum,ans1,ans2);
    }
    return 0;
}

