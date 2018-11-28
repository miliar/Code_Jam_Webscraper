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
    ifstream fp_in("input.txt");
    ofstream fp_out("output.txt");
    //SC(t);
    fp_in>>t;
    FR(h,1,t+1)
    {
              int n,a[4][4],b[4][4],m;
              bool f[17]={false},f1[17]={false},f2[17]={false};
              //SC(n);
              fp_in>>n;
              FR(i,0,4)
              FR(j,0,4)fp_in>>a[i][j];//SC(a[i][j]);
              fp_in>>m;//SC(m);
              FR(i,0,4)
              FR(j,0,4)fp_in>>b[i][j];//SC(b[i][j]);
              
              FR(i,0,4)
              {
                       f[a[n-1][i]]=true;
                       f1[a[n-1][i]]=true;
              }
              FR(i,0,4)
              {
                       f[b[m-1][i]]=true;
                       f2[b[m-1][i]]=true;
              }
              int cnt=0;
              FR(i,0,17)
              {
                        if(f[i])cnt++;
              }
              
              if(cnt<7)fp_out<<"Case #"<<h<<": Bad magician!\n";
              else if(cnt==7)
              {
                   int ans;
                   FR(i,0,17)
                   {
                             if(f[i] && f1[i] && f2[i])
                             {
                                     ans=i;
                                     break;
                             }
                   }
                   fp_out<<"Case #"<<h<<": "<<ans<<"\n";
              }
              else fp_out<<"Case #"<<h<<": Volunteer cheated!\n";
    }
    fp_in.close();
    fp_out.close(); 
     R 0;
}
