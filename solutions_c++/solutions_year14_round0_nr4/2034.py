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
        double a[10010],b[10010];
        int n;
        fscanf(fpi,"%d",&n);
        for(int i=0;i<n;i++)
        fscanf(fpi,"%lf",&a[i]);
        
        for(int i=0;i<n;i++)
        fscanf(fpi,"%lf",&b[i]);
        
        sort(a,a+n);
        sort(b,b+n);
        /*for(int i=0;i<n;i++)
        fprintf(fpo,"%lf ",a[i]);
        fprintf(fpo,"\n");
        for(int i=0;i<n;i++)
        fprintf(fpo,"%lf ",b[i]);
        fprintf(fpo,"\n");*/
        int selected[10010]={0},ken[10010];
        for(int i=n-1;i>=0;i--)
        {
            int flag=0;
            for(int j=i;j<n;j++)
            {
                if(selected[j]==0&&a[i]<b[j])
                {
                   ken[i]=j;
                   selected[j]=1;
                   flag=1;
                   break;
                }
            }
            if(flag==0)
            {
                for(int j=0;j<n;j++)
                {
                  if(selected[j]==0)
                  {
                        ken[i]=j;
                        selected[j]=1;
                        break;
                    }
                }
                
            }
        }
        int ans2=0;
        int ken2[100010],selected2[100010]={0};
        for(int i=0;i<n;i++)
        {
            if(a[i]>b[ken[i]])
            {
            ans2++;
            }
        }
        int ans1=0;
        for(int i=n-1;i>=0;i--)
        {
            int flag=0;
            ken2[i]=-1;
            for(int j=n-1;j>=0;j--)
            {
            if(selected2[j]==0&&a[i]>b[j])
            {
              ken2[i]=j;
              selected2[j]=1;
              flag=1;
              break;
            }
            }

        }
        for(int i=n-1;i>=0;i--)
        {
            if(ken2[i]==-1)
            {
              for(int j=n-1;j>=0;j--)
            {
            if(selected2[j]==0)
            {
              ken2[i]=j;
              selected2[j]=1;
              break;
            }

            }
        }
    }
        for(int i=0;i<n;i++)
        {
            if(a[i]>b[ken2[i]])
            ans1++;
        }
        fprintf(fpo,"Case #%d: %d %d\n",z,ans1,ans2);
        
        
    }



getch();
return 0;
/*checklist
1)getch() and conio.h removed.*/
}
