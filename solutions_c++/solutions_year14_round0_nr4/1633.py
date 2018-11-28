/*@author: c0d3_k1ra
 *
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>
#include <map>
#include <string>
#include <climits>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <ctime>
using namespace std;
typedef long int int64;
typedef long long int int64l;
typedef unsigned long long uint64l;
typedef unsigned long uint64;
inline void scanint(int *a)
{
    char c = 0;int sign=1;
    while(c<33)
       // c = fgetc_unlocked(stdin);
    c = getc(stdin);

    *a = 0;
    while(c>33)
    {
        if(c=='-'){ sign=-1;
        c = getc(stdin);
        //c = fgetc_unlocked(stdin);
        continue;}
        *a = *a*10 + c - '0';
       // c = fgetc_unlocked(stdin);
    c = getc(stdin);
    }
    *a=*a * sign;
    //printf("%d\n",*a);
}
char outputbuf[20];

inline void putint(int n)
{
	outputbuf[19]='\n';
    bool flag=false;int i=18,r;
    if(n<0){ flag=true; n*=-1;}
    while(n!=0)
    {
        r=n%10;
        outputbuf[i--]=r+'0';
        n/=10;
    }
    if(flag) outputbuf[i--]='-';
    i++;
    while(i<20)
    {
        //putchar_unlocked(outputbuf[i++]);
        putc(outputbuf[i++],stdout);
    }
}
using namespace std;
int main()
{
    int cases,n;
    pair<double,int> naomi[1000],ken[1000];
    pair<double,int> naomiCopy[1000],kencopy[1000];

    int i,j,k,falg;
    int cwar,cdwar;
 	scanf("%d",&cases);
 	for(i = 1; i <= cases; i++)
 	{
 		cwar = 0;
 		cdwar = 0;

 		scanf("%d",&n);


		for(j = 0; j < n; j++)
 		{
 		  scanf("%f",&naomi[j].first);
		  naomi[j].second = 0;
 		  naomiCopy[j].first = naomi[j].first;
		  naomiCopy[j].second = 0;
		}

 		for(j = 0; j < n; j++)
 		{
 		    scanf("%f",&ken[j].first);
		    ken[j].second = 0;
 			kencopy[j].first = ken[j].first;
			kencopy[j].second = 0;
		}
		 sort(naomi, naomi + n);
		 sort(ken, ken + n);
 		 for(j = 0; j < n; j++)
 		 {
 		 	falg = 0;
 		 	for(k = 0; k < n; k++)
 		 	{
 		 		if(naomi[j].first < ken[k].first && ken[k].second == 0)
 		 		{
 		 			falg = 1;
 		 			ken[k].second = 1;
 		 			break;
 		 		}
 		 	}
 		 	if(!falg) cwar++;
 		 }
 		 sort(naomiCopy, naomiCopy + n);
		 sort(kencopy, kencopy + n);
 		 for(j = 0; j < n; j++)
 		 {
 		 	falg = 0;
 		 	for(k = 0; k < n; k++)
 		 	{
 		 		if(naomiCopy[j].first > kencopy[k].first && kencopy[k].second == 0)
 		 		{
 		 			falg = 1;
 		 			kencopy[k].second = 1;
 		 			cdwar++;
 		 			break;
 		 		}
 		 	}
 		 }
 		 printf("Case #%d: %d %d\n",i,cdwar,cwar);
 	}
 	return 0;
 }
