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
              double c,f,x;
              fscanf(ifile, "%lf %lf %lf", &c, &f, &x); 
              //fp_in>>c>>f>>x;
              //cout<<c<<" "<<f<<" "<<x<<"\n";
              double prodr=2.0,tmpanst,rt,anst,stt=0.0;
              anst=x/prodr;
              while(1)
              {
                      rt=c/prodr;
                      prodr+=f;
                      tmpanst=x/prodr;
                      tmpanst+=rt;
                      if(tmpanst+stt>anst)break;
                      anst=tmpanst+stt;//cout<<tmpanst<<" "<<anst<<" "<<rt<<" "<<stt<<" "<<prodr;
                      //cin>>t;
                      stt+=rt;
                      
              }
              fprintf(ofile, "Case #%d: %.7lf\n",h,anst);
    }
    fclose(ifile);
    fclose(ofile);
     R 0;
}
