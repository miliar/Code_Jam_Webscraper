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
main()
{
	int cases;
	scanint(&cases);
	for(int t=1;t<=cases;t++)
    {
        int a,b,k,cnt=0;
        scanint(&a);
        scanint(&b);
        scanint(&k);
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
                if((i&j)<k)
                    cnt++;
        printf("Case #%d: %d\n",t,cnt);
	}
}
