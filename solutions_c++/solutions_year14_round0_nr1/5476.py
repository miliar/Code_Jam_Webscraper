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
#include<cassert>
#define read(x) scanf("%d",&x)
#define read2(x,y) scanf("%d%d",&x,&y)
#define read3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;
typedef pair<int,int> pr;

int main()
{
    
    int t,a,b,i,j,c,tt=1;
     //freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
     read(t);
     while(t--)
     {
               int freq[17]={0};
               read(a);
               for(i=0;i<4;i++)
               for(j=0;j<4;j++)
               {
                               read(c);
                               if(i==a-1)freq[c]++;
               }
               read(b);
               for(i=0;i<4;i++)
               for(j=0;j<4;j++)
               {
                               read(c);
                               if(i==b-1)freq[c]++;
               }
               
               j=-1;
               for(i=1;i<=16;i++)
               if(freq[i]==2)
               {
               if(j!=-1){
                         j=0;break;
                         }
               else j=i;
               }          
    
               printf("Case #%d: ",tt++);
               if(j==0)printf("Bad magician!\n");
               else if(j==-1)printf("Volunteer cheated!\n");
               else printf("%d\n",j);
    }
}
