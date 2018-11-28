#include<stdio.h>
#include<iostream>
using namespace std;

#include<math.h>
#include<algorithm>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<string>
#include<queue>

#define repA(p,q,i)  for( int (i)=(p); (i)!=(q); ++(i) )
#define repAE(p,q,i)  for( int (i)=(p); (i)<=(q); ++(i) )
#define repD(p,q,i)  for( int (i)=(p); (i)!=(q); --(i) )
#define repDE(p,q,i)  for( int (i)=(p); (i)>=(q); --(i) )

#define range 10010

void MAIN();

double mp1[range];
double mp2[range];

bool cmp(double a, double b);
int TianJi(double *a, double *b, int n);


int main()
{
    freopen("0000.in", "r", stdin);
    freopen("0000.out", "w", stdout);
    MAIN();
    fclose(stdout);
    
    return 0;
}



void MAIN()
{
     int test;  scanf("%d", &test);
     int n;
     repAE(1,test,rd)
     {
          scanf("%d", &n);
          repA(0,n,i)  scanf("%lf", &mp1[i]);
          repA(0,n,i)  scanf("%lf", &mp2[i]);
          
          sort(mp1, mp1+n, cmp);
          sort(mp2, mp2+n, cmp);
          
          int rst1 = TianJi(mp1, mp2, n);
          int rst2 = TianJi(mp2, mp1, n);
          
          printf("Case #%d: %d %d\n",rd, rst1, n-rst2);
                          
     }
     return;
}

int TianJi(double *a, double *b, int n)
{
     int rst = 0;
     int cp = n;
     int ap,aq,bp,bq;
     ap=bp=0;  aq=bq=n-1;
     while(cp--)
     {
         if(a[aq] > b[bq])
         {  --aq; --bq; ++rst; }
         else if(a[ap] > b[bp])
         {  ++ap; ++bp; ++rst; }
         else
         {  ++ap; --bq; }
         
     }   
     
     return rst;
}

bool cmp(double a, double b)
{
     return a < b;     
}
