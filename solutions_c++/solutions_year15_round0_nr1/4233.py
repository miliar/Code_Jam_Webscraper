// do.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
using namespace std;

//output stuff
int casesol[101];
int ncase;
void output()
{
	for(int i=1;i<=ncase;i++)
	{
	printf("Case #%d: %d\n",i,casesol[i]);
	}
}

void main()
{
		freopen("file.in", "r", stdin);
		freopen("file.out", "w", stdout);
		scanf("%d",&ncase);
		int max;
		int standing,fren,val;
		char shy[1500];
		for(int j=1;j<=ncase;j++)
		{
			fren=0;
			scanf("%d %s",&max,&shy);
			/*for(int i=0;i<=max;i++){
				shy[i]=ppl/(10^(max-i));
			}*/
			standing=shy[0]-'0';
			for(int i=1;i<=max;i++){
			val=shy[i]-'0';
				if(standing>i)
					standing+=val;
				else
				{
					fren+=i-standing;
					standing+=val+(i-standing);
				}
			}
			casesol[j]=fren;
		}
output();
}


