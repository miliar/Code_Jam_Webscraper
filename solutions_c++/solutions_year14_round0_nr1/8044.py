#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long int int64;
/*#define gc getchar_unlocked
inline void scanint(int64 &x)
{
   register int64 c = gc();
   x = 0;
   for(;(c<48 || c>57);c = gc());
   for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}*/
int64 a[10][10],b[10][10],ab[10],ba[10];
int main()
{
          freopen("in.txt","r",stdin);
          freopen("out.txt","w",stdout);
          int64 i,j,k,m,n,t,ans,c=0;
          scanf("%lld",&t);
          while(t--)
                    {
                    int64 count = 0;
                    c++;
                     scanf("%lld",&n);
                     for(i=0;i<4;i++){
                                      for(j=0;j<4;j++){scanf("%lld",&a[i][j]);if(i==n-1)ab[j]=a[i][j];}}
                     sort(ab,ab+4);
                     scanf("%lld",&m);
                     for(i=0;i<4;i++){
                                      for(j=0;j<4;j++){scanf("%lld",&b[i][j]);if(i==m-1)ba[j]=b[i][j];}}
                    
                     sort(ba,ba+4);
                    for(i=0,j=0;i<4&&j<4;)
                                           {
                                           if(ab[i]==ba[j]){count++;ans=ab[i];i++;j++;}
                                           else if(ab[i]<ba[j])i++;
                                           else j++;                                   
                                           }
                     if(count==0)
                     printf("Case #%lld: Volunteer cheated!\n",c);
                     else if(count==1)
                      printf("Case #%lld: %lld\n",c,ans);
                      else
                       printf("Case #%lld: Bad magician!\n",c);
                     }
                 
 //system("pause");
}
