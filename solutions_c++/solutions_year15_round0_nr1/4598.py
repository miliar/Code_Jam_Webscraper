
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
char str[1010];
int main () {
    FILE *fin  = fopen ("A-large.in", "r");
    FILE *fout = fopen ("A-large.out", "w");
   int n,k,t,i,sum,j;
   //scanf("%d",&t);
   fscanf(fin,"%d",&t);
   for(j=1;j<=t;j++)
   {   //scanf("%d",&n);
	   fscanf(fin,"%d",&n);
  // scanf("%s",str);
   fscanf(fin,"%s",str);
   k=0;
sum=0;
for(i=0;i<strlen(str);i++)
{
if(sum<i)
{
k+=(i-sum);
sum+=((i-sum)+(str[i]-'0'));
}
else
{
sum+=(str[i]-'0');
}

}
fprintf(fout,"Case #%d: %d\n",j,k);
//printf("Case #%d: %d\n",j,k);


   }

    
return (0);
}
