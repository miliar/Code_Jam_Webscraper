#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<map>
#include<climits>
#include<stack>
#include<vector>
#include<algorithm>
#define gc getchar//_unlocked
#define pc putchar//_unlocked
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define KEY_NOT_FOUND -1
typedef long long int LL;
typedef unsigned long long int ULL;
using namespace std;
inline int readInt();
inline void writeInt(int a);
long long readLongLong();
void writeLongLong(long long res);
LL power(LL base,LL exp,LL x);
LL mulmod(LL a,LL b,LL c);

int main()
{

    int a[4][4],b[4][4],i,j,x,y,t,T,ans,flag1,flag[17];
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        for(i=0;i<17;i++)flag[i]=0;
        flag1=0;
        scanf("%d",&x);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)scanf("%d",&a[i][j]);
        for(i=0;i<4;i++)flag[a[x-1][i]]++;
        scanf("%d",&y);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)scanf("%d",&b[i][j]);
        for(i=0;i<4;i++)flag[b[y-1][i]]++;
        for(i=0;i<17;i++)
        {
            if(flag[i]>1)
            {
                if(flag1==0)
                {
                    flag1=1;
                    ans=i;
                }
                else
                {
                    ans=90; // Bad magician
                    break;
                }
            }

        }
        if(flag1==1 && ans!=90 )
        {
            printf("Case #%d: %d\n",t,ans);
        }
        else if(flag1==1 && ans==90)printf("Case #%d: Bad Magician!\n",t);
        else printf("Case #%d: Volunteer Cheated!\n",t);
    }
    return 0;
}
void writeInt(int a)
{
    char s[11];
    register int t = -1;
    do
    {
        s[++t] = a % 10 + '0';
        a /= 10;
    }while(a > 0);
    while(t >= 0)pc(s[t--]);
    //pc('\n');
}
int readInt()
{
    char c=gc();
    int ans=0;
    while(c<'0'||c>'9')c=gc();
    while(c>='0'&& c<='9')
    {
        ans=ans*10+c-'0';
        c=gc();
    }
    return ans;
}
long long readLongLong()
{
   long long res=0;
   char ch;
   ch=gc();
   while(ch<'0' || ch>'9')
       ch=gc();
   while(ch>='0' && ch<='9')
   {
       res=(res*10)+ch-48;
       ch=gc();
   }
   return res;
}
void writeLongLong(long long res)
{
   long long rev,count=0,n;
   rev=res;
   if(res==0)
   {
       pc('0');
       pc('\n');
       return;
   }
   while(rev%10==0)
   {
       rev=rev/10;
       count++;
   }
   rev=0;
   n=res;
   while(n)
   {
       rev=(rev*10)+(n%10);
       n=n/10;
   }
   while(rev)
   {
       pc((rev%10)+48);
       rev=rev/10;
   }
   while(count--)
   pc('0');
   //pc('\n');
}
LL power(LL base,LL exp,LL x)
{
         long long ans=0;
         if(exp==0)
                   return 1;
         ans=power(base,exp>>1,x);
         ans=(ans*ans)%x;
         if(exp & 1)
                ans=(ans*base)%x;
         return ans;
}

LL mulmod(LL a,LL b,LL c){
    LL x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}


