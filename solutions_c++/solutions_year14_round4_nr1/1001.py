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
#define LSC(x) scanf("%lld",&x)
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
typedef long long int L;
int main()
{
    int t;
    FILE *ifile  = fopen("input.txt", "r");
    FILE *ofile = fopen("output.txt", "w");
    fscanf(ifile,"%d",&t); 
    //SC(t);
    FR(h,1,t+1)
    {
              int n,k;
              fscanf(ifile, "%d",&n); 
              fscanf(ifile, "%d",&k);
              int a[n];
              FR(i,0,n)fscanf(ifile, "%d",&a[i]);
              sort(a,a+n);
              int cnt=0;
              FR(i,0,n)
              {
                       if(a[i]!=-1){
                       RFR(j,n-1,i+1)
                       {
                                     if(a[j]!=-1 && a[i]+a[j]<=k)
                                     {
                                                 cnt++;
                                                 a[j]=-1;
                                                 a[i]=-1;
                                                 break;
                                     }
                       }
                       if(a[i]!=-1)cnt++;
                       }
              }
    fprintf(ofile, "Case #%d: %d\n",h,cnt);
    }
    fclose(ifile);
    fclose(ofile); 
    //system("pause");
     R 0;
}
