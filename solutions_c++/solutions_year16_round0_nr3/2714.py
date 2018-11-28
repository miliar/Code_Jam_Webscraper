#include<stdio.h>
#include<vector>
#include<math.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();it++)
#define p(a) printf("%lld y",a)
using namespace std;
long long comp[10000000];
bool bin[100];
long long powe[1001][1001];
vector<long long> f;
long long power(long long n,long long r)
{
    if(powe[n][r]) return powe[n][r];
    if(r==0)
    {
        powe[n][r]=1;
        return powe[n][r];
    }
    if(r%2==0)
    {
        long long y=power(n,r/2);
        powe[n][r]=y*y;
        return powe[n][r];
    }
    powe[n][r]=n*power(n,r-1);
    return powe[n][r];
}
void primesieve()
{
    int i,j;
    for(i=2;i<10000000;i++)
    {
         if(!comp[i])
        {
            for(j=2;j*i<10000000;j++)
            {
                if(!comp[j*i])
                    comp[j*i]=i;
            }
        }
    }
}
long long checkcomp(long long n)
{
    if(n<10000000) return comp[n];
    long long i;
    for(i=2;i<=sqrt(n)+1;i++)
    {
        if(n%i==0)
        {
            return i;
        }
    }
    return 0;
}
long long ctb(long long n, int b)
{
    long long ans=0,i=0;
    while(n)
    {
        if(n%2)
        {
            long long k=power(b,i);
            ans=ans+k;
        }
        n/=2;
        i++;
    }
    return ans;
}
int main()
{
    primesieve();
 //  freopen("input2.in","r",stdin);
   //freopen("output5.txt","w",stdout);
 //   for(int i=0;i<10;i++) printf("%lld ",power(2,i));
    int t;
    scanf("%d",&t);
    while(t--)
    {   printf("Case #1:\n");
        long long n,j;
        long long i,k,c=0;
        scanf("%lld%lld",&n,&k);
        int flag=1;
        long long st=power(2,n-1)+1;
        for(i=st;c<k;i++)
        {   flag=1;
            f.clear();
            long long che=ctb(i,10);
            if(che%10==0) continue;
            if(checkcomp(i))
            {
                f.push_back(checkcomp(i));
                for(j=3;j<=10;j++)
                {
                    long long tm=ctb(i,j);
                    long long fc=checkcomp(tm);
                    if(fc>0) f.push_back(fc);
                    else
                    {
                        flag=0;
                        break;
                    }
                }

            }
            else flag=0;
            if(flag==1)
            {   c++;
                printf("%lld ",ctb(i,10));
                tr(f,it1)
                {
                    printf("%lld ",*it1);
                }
                printf("\n");
            }
        }
        //scanf(" %s",s);
    }
    return 0;
}
