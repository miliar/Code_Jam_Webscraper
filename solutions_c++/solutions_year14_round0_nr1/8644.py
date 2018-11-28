#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#include <stack>
#include <list>
#include <numeric>
#define INT_MAX 2147483647
#define INT_MIN -2147483647 //2^31-1
#define pi acos(-1.0)
#define N 1000000
#define LL unsigned long long
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define SWAP(a,b) a= a^b, b=a^b, a=a^b
typedef  long long int ull;
using namespace std;

int main()
{
//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);

int k,t;cin>>t;

for(k=1;k<=t;k++){
          
          int arr1[10][10]={},arr2[10][10]={},a,b,i,j,c=0,d;
          cin>>a;a--;
          for(i=0;i<4;i++)for(j=0;j<4;j++)cin>>arr1[i][j];
          cin>>b;b--;
          for(i=0;i<4;i++)for(j=0;j<4;j++)cin>>arr2[i][j];
          
          for(i=0;i<4;i++)
          for(j=0;j<4;j++)
          if(arr1[a][i]==arr2[b][j]){c++;d=arr1[a][i];}
          
          if(c>1)cout<<"Case #"<<k<<": Bad magician!"<<endl;
          else if (c==1)cout<<"Case #"<<k<<": "<<d<<endl;
          else cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
          }
//system("pause");
return 0;
}
