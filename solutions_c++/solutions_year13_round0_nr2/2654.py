#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
 
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define S(a) scanf("%d",&(a))
#define P(a) printf("%d",(a))
#define min(a,b) ((a)<(b)?(a):(b))
#define NL printf("\n")
#define sqr(a) ((a)*(a))
#define SL(a) scanf("%lld",&(a))
#define PL(a) printf("%lld",(a))
#define lli long long int
#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define inarrd(arr,n) for(int i=0;i<n;i++)S(arr[i]);
#define outarrd(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PF(" ");}NL;
#define outarrN(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PFN;}

int main()
{   freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test,count=0;
    cin>>test;
    while(test--)
    {       
              count++;
              int no,mm,result=1;
              cin>>no>>mm;
              int arr[no][mm];
              for(int i=0;i<no;i++)
              {for(int j=0;j<mm;j++){cin>>arr[i][j];}}
              for(int i=0;i<no;i++)
              {for(int j=0;j<mm;j++){if(arr[i][j]==1){
                      int flag=1;for(int y=0;y<mm;y++){if(arr[i][y]!=arr[i][j]){flag=0;break;}}
                                            if(flag==0)
                                            {flag=1;for(int y=0;y<no;y++){if(arr[y][j]!=arr[i][j]){flag=0;break;}}}
        
                                            if(flag==0)
                                            {result=0;break;}}}
                              
                      
                      if(result==0)break;
                      
              }
              cout<<"Case #"<<count<<": ";
              if(result==0)
                cout<<"NO"<<endl;
              else
                cout<<"YES"<<endl;
    }
    return 0;
}
 
