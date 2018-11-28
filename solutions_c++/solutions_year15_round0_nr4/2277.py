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
 
int main() {
	int t,x,r,c,i;
	    FILE *fin  = fopen ("D-small-attempt0.in", "r");
    FILE *fout = fopen ("D-small.out", "w");
	fscanf(fin,"%d",&t);
	for(i=1;i<=t;i++)
	{
	    fscanf(fin,"%d%d%d",&x,&r,&c);
		if(x==1)
		{
		 fprintf(fout,"Case #%d: GABRIEL\n",i);
		}
		else if(x==2)
		{
		 if(r==1&&c==1||r==1&&c==3||r==3&&c==3||r==3&&c==1)
	        fprintf(fout,"Case #%d: RICHARD\n",i);
	       else
            fprintf(fout,"Case #%d: GABRIEL\n",i);
		}
		else if(x==3)
	    {
		if(r==1||c==1)
	        fprintf(fout,"Case #%d: RICHARD\n",i);
	      else if(r==3||c==3)
       fprintf(fout,"Case #%d: GABRIEL\n",i);
	     else
            fprintf(fout,"Case #%d: RICHARD\n",i);
		}

		else
		{
		if(r==4&&c==4||r==4&&c==3||r==3&&c==4)
         fprintf(fout,"Case #%d: GABRIEL\n",i);
	    else 
          fprintf(fout,"Case #%d: RICHARD\n",i);
		}
	    
	}
	return 0;
}

