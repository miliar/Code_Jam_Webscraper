#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
using namespace std;
long long data[1000000];
map<long long,long long >mm;

bool iss(long long i)
{
    long long t=0,p=0;
    long long str[100];
    t=i;
    while(t!=0)
    {
        str[p++]=t%10;
        t/=10;
    }
    long long j;
    for(j=0;j<p/2;++j)
    {
        if(str[j]!=str[p-j-1])break;
    }
    if(p/2==j)return 1;
    else return 0;
}
int main()
{
	long long i,j,k,l,n,m,t,T,ii,c1,c2,c;
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.txt","w",stdout);
    scanf("%I64d",&T);
    mm[0]=0;
    for(i=1,j=0,c=0;i<=10000000;++i)
    {
        if(iss(i))
        {
            if(iss(i*i))
            {
                data[(int)j]=i*i;
                ++j;
            }
        }
    }
    for(ii=1;ii<=T;++ii)
    {
       scanf("%I64d%I64d",&n,&m);
        c=0;
       //printf("%d %d\n",n,m);
       for(i=0;i<j;++i)
       {
           if(data[i]<n)continue;
           else if(data[i]>m)break;
           else
           {
               c++;
           }
       }
       printf("Case #%I64d: %I64d\n",ii,c);
    }

    return 0;
}
