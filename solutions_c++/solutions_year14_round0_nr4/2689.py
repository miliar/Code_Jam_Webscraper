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
              int n;
              fscanf(ifile, "%d",&n); 
              double a[n],b[n];
              FR(i,0,n)
              fscanf(ifile, "%lf",&a[i]);
              FR(i,0,n)
              fscanf(ifile, "%lf",&b[i]);
              
              sort(a,a+n);sort(b,b+n);
              //FR(i,0,n)fprintf(ofile, "%lf ",a[i]);fprintf(ofile, "\n");
              //FR(i,0,n)fprintf(ofile, "%lf ",b[i]);fprintf(ofile, "\n");
              int i1=0,i2=0;
              while(1)
              {
                     if(b[i2]<a[i1])i2++;
                     else 
                     {
                          i2++;
                          i1++;
                     }
                     if(i2==n)break;
              }
                     
                       
              int st=0,cnt=0;
              while(st<n && a[st]<b[0])st++;
              if(st==n)
              fprintf(ofile, "Case #%d: 0 %d\n",h,n-i1);
              else
              {
               i2=0;
               while(1)
               {
                       if(a[st]>b[i2])
                       {
                           st++;
                           i2++;
                           cnt++;
                       }
                       else st++;
                       if(st==n)break;
               }
               fprintf(ofile, "Case #%d: %d %d\n",h,cnt,n-i1);
               }
    }
    fclose(ifile);
    fclose(ofile); 
    //system("pause");
     R 0;
}
