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
              int N;
              fscanf(ifile, "%d",&N);
              int arr[N];
              FR(i,0,N)fscanf(ifile, "%d",&arr[i]);
              int result=0;
              int start=0,end=N-1;
              for(int i=0;i<N;i++)
              {
                    int Mini=start;
                    for(int j=start;j<=end;j++)
                    {
                            if(arr[j]<arr[Mini])
                               Mini=j;
                    }
                    if((Mini-start) <= (end-Mini))
                    {
                          result+=(Mini-start);
                          for(int j=Mini-1;j>=start;j--)
                          {
                                  arr[j+1]=arr[j];
                          }
                          start++;
                    }
                    else
                    {
                        result+=(end-Mini);
                        for(int j=Mini;j<end;j++)
                        {
                                  arr[j]=arr[j+1];
                        }
                        end--;
                    }
            }
    fprintf(ofile, "Case #%d: %d\n",h,result);
    }
    fclose(ifile);
    fclose(ofile); 
    //system("pause");
     R 0;
}
