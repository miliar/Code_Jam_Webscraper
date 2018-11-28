#include<stdio.h>
#include<iostream>
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
 
int main()
{
    int t,counter=1;
    SC(t);
    while(t--){
               int m,n;
               SC(n);SC(m);
               int a[n][m];
               FR(i,0,n){
                         FR(j,0,m)SC(a[i][j]);
                         }
               bool flag=true;
               FR(i,0,n){
                         FR(j,0,m){
                                   int x=0,y=0;
                                   FR(k,0,n)if(a[k][j]>a[i][j])x++;
                                   if(x>0)y++;
                                   x=0;
                                   FR(k,0,m)if(a[i][k]>a[i][j])x++;
                                   if(x>0)y++;
                                   if(y>1){
                                            flag=false;
                                            break;
                                            }
                                   }
                         if(!flag)break;
                         }
               printf("Case #%d: ",counter++);
               if(flag)printf("YES\n");
               if(!flag)printf("NO\n");
               }
        //system("pause");
     R 0;
}    
