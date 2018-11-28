//DER.......
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>
#include<iostream>
#include<sstream>
using namespace std;

// #defines
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define LPI(i,n) for(int i=0;i<(n);i++)
#define LPI1(i,a,b) for(int i=(a);i<=(b);i++)
#define LPIL(i,x) for(int i=0;x[i];i++)
#define LPD(i,n) for(int i=(n)-1;i>=0;i--)
#define LPD1(i,a,b) for(int i=(a);i>=(b);i--)
#define I(x) scanf("%d",&x)
#define RI(x) int x;I(x)
#define II(x,y) scanf("%d%d",&x,&y)
#define RII(x,y) int x,y;II(x,y)
#define III(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define RIII(x,y,z) int x,y,z;III(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define F first
#define S second
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
string convertInt(long number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}
int main(){

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

   map<string,int>m;
   char A[1000009];
   char ch[200];
   long i,c,p1,n,l,k,q;
   long long co;
   LPI(j,200)
   {
       ch[j]=1;
   }
   ch['a']=0;ch['e']=0;ch['i']=0;ch['o']=0;ch['u']=0;
   string str="";
   RI(t);
   LPI(j,t)
   {
       scanf("%s%ld",A,&n);
       l=strlen(A);
       co=0;c=0;
       m.clear();
       p1=0;
       for(i=0;i<l;i++)
       {
           if(ch[A[i]]==0)
           {
               c=0;
               p1=i+1;
           }
           else
           {
               if(c<n)
               c++;
               else
               p1=p1+1;
           }
           if(c==n)
           {
               //cout<<i<<endl;
               for(q=0;q<=p1;q++)
               {

                for(k=i;k<l;k++)
               {
                   str=convertInt(q)+","+convertInt(k);
                   if(m[str]<1)
                   {
                       co++;
                       m[str]=1;
                      // cout<<str<<endl;
                   }
               }
               }
           }
       }

       printf("Case #%ld: %lld\n",j+1,co);

   }
    return 0;
}


