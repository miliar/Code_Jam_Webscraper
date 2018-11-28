#include<stdio.h>
#include<iostream>
#include <string.h>
#include<math.h>
#define R return
#define FR(i,a,b) for(L i=a;i<b;i++)
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
    L a[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
    //FR(i,0,39)cout<<a[i]<<endl;
    int t,counter=1;
    SC(t);
    while(t--){
               L m,n;
               LSC(n);LSC(m);
               int c=0;
               FR(i,0,39){
                          if(a[i]>=n && a[i]<=m)c++;
                          }
               printf("Case #%d: ",counter++);
               printf("%d\n",c);
               }
        //system("pause");
     R 0;
}    
