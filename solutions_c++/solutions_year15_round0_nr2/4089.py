
/*
ID: pktyagi1
LANG: C++
TASK: preface
*/

//#include "stdafx.h"
#include<cstdio>

#include<stdio.h>
#include<cstring>
#include<vector>
#include<iostream>
#include<math.h>
#include<map>
#include<algorithm>
#include<set>
#include<string>
#define s(n) scanf("%d",&n)
#define p(n) printf("%d\n",n)
#include <iostream>
#include <fstream>
#define fs(n) fscanf(fin,"%d",&n)
#define fp(n) fprintf(fout,"%d\n",n)
using namespace std;
typedef long long ll; 
int a[1010],c[1010];
int sol(int i)
{if(i==0)
return 0;
else
	if(c[i]==0)
	return sol(i-1);
	else if(i<=3)
   return i;
	else
{
	int time=i;
for(int val=i/2;val>0;val--)
{
c[val]+=c[i];
c[i-val]+=c[i];
time=min(time,c[i]+sol(i-1));
c[val]-=c[i];
c[i-val]-=c[i];

}
return time;
}

}
int main () {
    FILE *fin  = fopen ("B-small-attempt3.in", "r");
    FILE *fout = fopen ("B-small.out", "w");
   int n,k,t,i,sum,j,time,mini;
   //scanf("%d",&t);
   fscanf(fin,"%d",&t);
   for(j=1;j<=t;j++)

   {   

	   //scanf("%d",&n);
	   fscanf(fin,"%d",&n);
	   for(i=0;i<=1000;i++)
		   c[i]=0;
for(i=0;i<n;i++)
   {   //scanf("%d",&a[i]);
	   fscanf(fin,"%d",&a[i]);
	   c[a[i]]++;

}




fprintf(fout,"Case #%d: %d\n",j,sol(*max_element(a,a+n)));
//printf("Case #%d: %d\n",j,time);


   }

    
return (0);
}
