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
        int freq[20]={0};
        int a;
        int m[20][20];
        fscanf(fpi,"%d",&a);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            fscanf(fpi,"%d",&m[i][j]);
        }
        for(int i=1;i<=4;i++)
        freq[m[a][i]]++;
        
        fscanf(fpi,"%d",&a);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            fscanf(fpi,"%d",&m[i][j]);
        }
        int flag=0,ans;
        for(int i=1;i<=4;i++)
        {
            if(flag==0&&freq[m[a][i]]!=0)
            {
               flag=1;
               ans=m[a][i];
            }
            else if(flag==1&&freq[m[a][i]]!=0)
            {
                flag=2;
            }
        }
        if(flag==0)
        fprintf(fpo,"Case #%d: Volunteer cheated!\n",z);
        else if(flag==1)
        fprintf(fpo,"Case #%d: %d\n",z,ans);
        else
        fprintf(fpo,"Case #%d: Bad magician!\n",z);
    }


getch();
return 0;
/*checklist
1)getch() and conio.h removed.*/
}
