/*
*************************************************************************
* $ Author : honeyslawyer   $
* $ Name   : shashank gupta $
*************************************************************************
*
* Copyright 2014 @ honeyslawyer and shashank gupta
*
************************************************************************/
#include<cstdio>
#include<iostream>
#include<cmath>
#include<conio.h>
#include<cstring>
#include<ctype.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<string>
#include<climits>

#define mod 1000000007
#define ll long long

using namespace std;
ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m)
 {ll ans=1;
  b%=m;
  while(exp)
   {if(exp&1)
     ans=(ans*b)%m;
    exp>>=1;
	b=(b*b)%m;
   }
  return ans;
 }

int main()
{
  FILE *fpi,*fpo;
  int t;
  fpi=fopen("input.in","r");
  fpo=fopen("output.txt","w");
  fscanf(fpi,"%d",&t);
  for(int z=1;z<=t;z++)
  {
        double c,f,x;
        fscanf(fpi,"%lf %lf %lf",&c,&f,&x);
        double ans1=0.00;
        double ans2=0.00;
        double rate=2.0;
        double time1=x/rate;
        double time2=c/rate+x/(rate+f);
        while(1)
        {
            if(time1<time2)
            {
                fprintf(fpo,"Case #%d: %0.7lf\n",z,time1);
                break;
            }
            rate=rate+f;
            time1=time2;
            time2=time2-x/rate+c/rate+x/(rate+f);
        }
    }


getch();
return 0;
/*checklist
1)getch() and conio.h removed.*/
}
