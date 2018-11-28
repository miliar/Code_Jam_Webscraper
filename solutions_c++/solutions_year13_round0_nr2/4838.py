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
int t,tc=1;cin>>t;

while(t--){
           int m,n,i,j,f=1;
           int a[105][105]={{0}};
           int row[105]={0},col[105]={0};
           cin>>m>>n;
           for(i=0;i<m;i++)
           for(j=0;j<n;j++){
                            read(a[i][j]);
                            row[i]=max(row[i],a[i][j]);
                            col[j]=max(col[j],a[i][j]);
                            }
           
            for(i=0;i<m;i++){if(!f)break;
           for(j=0;j<n;j++)if(a[i][j]!=row[i] && a[i][j]!=col[j]){f=0;break;}}
           
           if(!f)printf("Case #%d: NO\n",tc++);
           else printf("Case #%d: YES\n",tc++);
           }


//system("pause");
return 0;
}

