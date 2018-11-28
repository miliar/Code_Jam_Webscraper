#include<iostream>
#include<stdio.h>
using namespace std;

unsigned const int p[5]={1,4,9,121,484};

int main()
{
 int q, w, a, b, t, T;
 scanf("%d",&T);
 for(t=1;t<=T;++t)
 {
  scanf("%d %d",&a,&b);
  for(q=0;q<5;++q)  if(p[q]>=a)break;
  for(w=4;w>=0;--w) if(p[w]<=b)break;
  printf("Case #%d: %d\n",t,(w-q)+1);
 }
 return 0;   
}
