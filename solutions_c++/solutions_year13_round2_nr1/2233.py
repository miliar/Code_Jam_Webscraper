#include<stdio.h>
#include<iostream>
#include<fstream>
#include <string.h>
#include<math.h>
#define R return
#define FR(i,a,b) for(int i=a;i<b;i++)
#define RFR(i,a,b) for(int i=a;i>=b;i--)
#define SC(x) scanf("%d",&x)
#define SSC(x) scanf("%s",x)
#include<sstream>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<utility>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#define IN(i,j) a[i][j]
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define FUN(x) x==true)?1:0
#define SWAP(x,y,z) {z=x;x=y;y=z;}
#define mod 1000000003
using namespace std;
 
int fun(int a[],int i,int k,int v,int n)
{
    if(i==n)return v;
    if(a[i]<k){
               k+=a[i];
               return(fun(a,i+1,k,v,n));
               }
    else{
         if(2*k-1>a[i])return(MIN(fun(a,i+1,2*k-1+a[i],v+1,n),fun(a,i+1,k,v+1,n)));
         else{
              if(k==2*k-1)return (fun(a,i+1,k,v+1,n));
              else return(MIN(fun(a,i,2*k-1,v+1,n),fun(a,i+1,k,v+1,n)));
              }
         }
}
 
int main()
{
    int t,h;
    SC(t);
    FR(h,0,t){
              int n,k;
              SC(k);SC(n);
              int a[n];
              FR(i,0,n)SC(a[i]);
              sort(a,a+n);
              printf("Case #%d: %d\n",h+1,fun(a,0,k,0,n));
              }
     R 0;
}
