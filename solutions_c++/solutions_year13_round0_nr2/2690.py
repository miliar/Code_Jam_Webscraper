#include<vector>
#include<utility>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
#define pb push_back
typedef pair < int, int >  pii;
#define SORT(a,n) qsort(a,n,sizeof(int),intcmp)
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%I64d",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define fill(a,v)                   memset(a, v, sizeof(a))
int intcmp(const void *f,const void *s)
{
   return (*(int *)f -*(int *)s);
}
int gcd(int a,int b){ return ((b==0)?a:gcd(b,a%b));}

#define MAX 20
#define MODBY 1000000007

typedef long long int lld;
typedef long double Lf;
int preprocess()
{
   return 0;
}

int main()
{
   int cases;
   int i,j;
   preprocess();
   int casectr=1;
   int a[MAX][MAX];
   for(scanf("%d",&cases);casectr<=cases;++casectr){
      printf("Case #%d: ",casectr);
      int n,m;
      scanf("%d",&n);
      scanf("%d",&m);
      for(i=0;i<n;++i)
         for(j=0;j<m;++j)
            scanf("%d",&a[i][j]);
      
      int tot=m+n;
      int bit;
      int row[MAX],col[MAX];
      for(bit=(1<<tot)-1;bit>=0;--bit){//lowest n bits are columns
         int wrong=0;//selected ones are twos, rest ones
         for(i=0;i<n;++i) row[i]=1+(             ((bit&(1<<i))      !=0));
         for(j=0;j<m;++j) col[j]=1+(             (bit&(1<<(j+n)))    !=0);
         for(i=0;i<n;++i)
            for(j=0;j<m;++j)
               wrong|=(min(row[i],col[j])!=a[i][j]);
         if(!wrong)
            break;
      }
      if(bit>=0) printf("YES\n");
      else printf("NO\n");
   }
   return 0;
}
