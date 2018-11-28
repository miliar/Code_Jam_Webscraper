#include<bits/stdc++.h>
#define gc getchar//_unlocked
#define pc putchar//_unlocked
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define MAX 200006
#define ll long long
#define infinity 10000000
using namespace std;
inline void inp(ll *n )
{
*n=0;
ll ch=gc();int sign=1;
while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=gc();}
while( ch >= '0' && ch <= '9' )
*n = (*n<<3)+(*n<<1) + ch-'0', ch=gc();
*n=*n*sign;
}
inline void fastp(ll a)
{
    register char c;
    char snum[20];
    int i=0;
    do
    {
     snum[i++]=a%10+48;
     a=a/10;
    }while(a!=0);
    i=i-1;
    while(i>=0)
    pc(snum[i--]);
    pc('\n');
}

int main()
{
    srand(time(NULL));
    ll t,n,m,i,j,l,r,k,x,y,ans,sum;
    char s[1003];
    freopen("A-large.in","r",stdin);
    FILE *fp=fopen("A-large.out","w+");
    inp(&t);
    for(k=1;k<=t;k++)
    {
        inp(&n); scanf("%s",&s); ans=sum=0;
        for(i=0;i<=n;i++)
        {
            if(sum+s[i]-'0'<i+1)
            {
                ans=ans+i-sum+s[i]-'0'+1;
                sum=i+1;
            }
            else sum+=s[i]-'0';
        }
        //printf("Case #%lld: %lld\n",k,ans);
        fprintf(fp,"Case #%lld: %lld\n",k,ans);
    }
  return 0;
}
