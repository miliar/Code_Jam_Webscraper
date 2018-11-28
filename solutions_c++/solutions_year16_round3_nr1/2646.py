/*
    Just For You 97116:)
*/

#include <bits/stdc++.h>

using namespace std;

typedef long long unsigned llu;
typedef long long lld;
typedef long ld;
typedef stringstream ss;

//shortcuts
#define mem(a,b) memset(a,b,sizeof(a))
#define X real()
#define Y imag()

//important constants
#define pi M_PI
#define mod7 10000007
#define mod9 1000000009
#define mod97 1000000007
#define MAX 100005
#define infi 2000000000 //infinity

//Read Inputs
#define si(n) scanf("%d",&n);
#define sli(n) scanf("%lld",&n);
#define slim(n,m) scanf("%lld%lld",&n,&m);

long long int min(long long int a, long long int b)
{
    return a<b?a:b;
}

long long int max(long long int a, long long int b)
{
    return a>b?a:b;
}

inline void checkNagative(long long &num)
{
    while (num < 0) num += mod97;
}

long long powerMod(long long a, long long b, long long c)
{
    long long result = 1;
    long long temp = 1;
    long long mask = 1;
    for (int i = 0; i < 64; i++)
    {
        mask = (i == 0) ? 1 : (mask * 2);
        temp = (i == 0) ? (a % c) : (temp * temp) % c;
            
        if ((b & mask) == mask)
            result = (result * temp) % c;
    }
    return result;
}

inline long long multiply(long long num, long long amt)
{
     checkNagative(num);
     checkNagative(amt);
     if (num >= mod97) num %= mod97;
     if (amt >= mod97) amt %= mod97;
     num *= amt;
     if (num >= mod97) num %= mod97;
//   checkNagative(num);
     return num;
}

long long int gcd(long long int a, long long int b)
{
    long long int c;
    while(b!=0)
    {
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int main()
{
    freopen("input.txt","r",stdin);
    //freopen("1Cchecksmalloutput.txt","w",stdout);
    freopen("1Clargeoutput.txt","w",stdout);
    
    lld t,n,m,i,j,k,l,x,y,z,flag,count,sum,a[MAX],b[MAX],c[MAX],d,mx;
    char s[MAX],r[MAX];
    sli(t);
    for(i=1;i<=t;i++)
    {
        count=sum=flag=mx=0;
        sli(n);
        if(n==2)
        {
            scanf("%lld%lld",&x,&y);
            if(x==y)
            {
                printf("Case #%lld: ",i);
                for(j=0;j<x;j++)
                    printf("AB ");
                printf("\n");
            }
            else if(x>y)
            {
                printf("Case #%lld: ",i);
                while(x!=y)
                {
                    printf("A ");
                    x--;
                }
                for(j=0;j<x;j++)
                    printf("AB ");
                printf("\n");       
            }
            else
            {
                printf("Case #%lld: ",i);
                while(x!=y)
                {
                    printf("B ");
                    y--;
                }
                for(j=0;j<y;j++)
                    printf("AB ");
                printf("\n");          
            }
        }
        else
        {
            sum=0;
            for(j=65;j<65+n;j++)
            {
                scanf("%lld",&a[j]);
                sum+=a[j];
            }
            mx=a[0];
            k=0;
            printf("Case #%lld: ",i);
            while(sum!=2)
            {
                for(j=65;j<65+n;j++)
                {
                    if(mx<a[j])
                    {
                        mx=a[j];
                        k=j;
                    }
                }
                printf("%c ",(char)k);
                a[k]--;
                sum--;
                mx=a[k];
            }
            for(j=65;j<65+n;j++)
            {
                if(a[j]!=0)
                    printf("%c",(char)j);
            }
            printf("\n");
        }
    }
    return 0;
}