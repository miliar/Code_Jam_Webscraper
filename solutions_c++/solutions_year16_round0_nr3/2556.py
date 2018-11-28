#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;

int n,m,A[50];
LL num[11];

void init()
{
     scanf("%d %d",&n,&m);
}

bool prime(LL x,int p) 
{
     for(LL i=2;i*i<=x;i++)
         if(x%i==0) {num[p]=i; return false;}
     return true;
}

bool check(LL x)
{
     for(int p=0;x;x>>=1) A[++p]=x&1;
     for(int p=2;p<=10;p++)
     {
         LL sum=0;
         for(int i=n;i>=1;i--) sum=sum*p+A[i];
         if(prime(sum,p)) return false;
     }
     return true;
}

void work()
{
     LL P=1; P=(P<<(n-2))-1; int cnt=0;
     for(LL i=0;i<=P && cnt<m;i++)
     {
         LL x=1; x=(x<<(n-1))+(i<<1)+1;
         if(check(x))
         {
            cnt++;
            for(int j=n;j>=1;j--) printf("%d",A[j]);
            printf(" ");
            for(int j=2;j<10;j++) cout<<num[j]<<' ';
            cout<<num[10]<<endl;
         }
     }
}

int main()
{
    int TT;
    scanf("%d",&TT);
    for(int i=1;i<=TT;i++)
    {
        printf("Case #%d:\n",i);
        init();
        work();
    }
    return 0;
}

