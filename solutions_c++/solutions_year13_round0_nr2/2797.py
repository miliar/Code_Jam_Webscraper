using namespace std;
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
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;


int mat[105][105]={{0}};


int main()
{
//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
int t,tt=1;
int m,n,i,j,flag;
read(t);
while(t--){
           int row[100]={0},col[100]={0};
           read(m);read(n);
           for(i=0;i<m;i++)
           for(j=0;j<n;j++){
                            read(mat[i][j]);
                            row[i]=max(row[i],mat[i][j]);
                            col[j]=max(col[j],mat[i][j]);
                            }
           flag=1;
           for(i=0;i<m && flag;i++)
           for(j=0;j<n;j++)if(mat[i][j]!=row[i] && mat[i][j]!=col[j]){flag=0;break;}
           if(!flag)printf("Case #%d: NO\n",tt++);
           else printf("Case #%d: YES\n",tt++);
           }

return 0;
}
