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
int main()
{
    int t,k;
    double c,f,x,tottime,d,tot;
    scanint(&t);
    for(k=1;k<=t;++k)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        d=x-c;
        tot=2;
        tottime=c/tot;
        while((d/tot) > (x/(f+tot)))
        {
            tot+=f;
            tottime+= (c/tot);
        }
        tottime+=(d/tot);
        printf("Case #%d: %.7lf\n",k,tottime);
    }
    return 0;
}
