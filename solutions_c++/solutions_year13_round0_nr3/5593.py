#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define frup(FRUP_I,FROM,TO) for(long long FRUP_I=FROM;FRUP_I<=TO;FRUP_I++)
#define frdn(FRDN_I,FROM,TO) for(long long FRDN_I=FROM;FRDN_I<TO;FRDN_I++)

#define pb(VALUE) push_back(VALUE)
#define pob() pop_back()
#define mp(FST,SEC) make_pair(FST,SEC)
#define len(STR) STR.length()
#define F first
#define S second

#define refresh(ARRAY,TARGET,VALUE) frdn(DEFINED_I,0,TARGET)ARRAY[DEFINED_I]=VALUE
#define watch(VALUE) {cout<<#VALUE;printf("=");cout<<VALUE;printf("\n");}
#define stop exit(0)

using namespace std;

int n,t,k,l,r;

bool chek(long long d)
{
     string s="";
     while (d) 
     {
       s+=(char)(d%10+48);
       d/=10;
     }     
     for(int i=0;i<len(s);i++)
      if (s[i]!=s[len(s)-1-i]) return 0;
     return 1;
}

int z[10000000];
int l1,r1;

int main()
{ 
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   
     for(int i=1;i<=10000000;i++)
             {
              if (chek(i)&&chek(1ll*i*i)) 
                 {
                  z[i]=z[i-1]+1;
                 } 
                   else z[i]=z[i-1];
             }
     scanf("%d",&t);     
     for (int p=0;p<t;p++)
      {
         cin >> l >> r;
         l1=(int) sqrt(l);
         r1=(int) sqrt(r);
         if (l1*l1>=l)
         cout << "Case #" << p+1 << ": " << z[r1]-z[l1-1] << endl; else
         cout << "Case #" << p+1 << ": " << z[r1]-z[l1] << endl; 
         
      }
return 0;
}
