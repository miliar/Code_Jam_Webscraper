#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
#include <algorithm>
#define MAXL 10
#define BASE 10000
using namespace std;

struct BigNum
{
    int num[MAXL+1];
    int len;
    BigNum()
    {
    }
    BigNum(int n)
    {
        memset(num,0,sizeof(num));
        len=0;
        while(n!=0)
        {
            num[len++]=n%BASE;
            n=n/BASE;
        }
    }
    BigNum& operator+=(const BigNum &a)
    {
        int i;
        len=max(len,a.len);
        for(i=0;i<len;i++)
        {
            num[i]=num[i]+a.num[i];
            num[i+1]=num[i+1]+num[i]/BASE;
            num[i]=num[i]%BASE;
        }
        if(num[len]>0)
        {
            len++;
        }
        return *this;
    }
    BigNum& operator*=(int k)
    {
        int i,cry;
        if(k==0)
        {
            memset(num,0,sizeof(num));
            len=0;
            return *this;
        }
        cry=0;
        for(i=0;i<len;i++)
        {
            cry=cry+num[i]*k;
            num[i]=cry%BASE;
            cry=cry/BASE;
        }
        while(cry>0)
        {
            num[len++]=cry%BASE;
            cry=cry/BASE;
        }
        return *this;
    }
    friend BigNum operator+(const BigNum &a,const BigNum &b)
    {
        BigNum ret;
        ret=a;
        ret+=b;
        return ret;
    }
    friend BigNum operator*(const BigNum &a,int k)
    {
        BigNum ret;
        ret=a;
        ret*=k;
        return ret;
    }
    friend int operator%(const BigNum &a,int k)
    {
        int i,rmd;
        rmd=0;
        for(i=a.len-1;i>=0;i--)
        {
            rmd=(rmd*BASE+a.num[i])%k;
        }
        return rmd;
    }
    friend bool operator<(const BigNum &a,const BigNum &b)
    {
        return compare(a,b)<0;
    }
    friend int compare(const BigNum &a,const BigNum &b)
    {
        int i;
        if(a.len!=b.len)
        {
            return a.len-b.len;
        }
        for(i=a.len-1;i>=0;i--)
        {
            if(a.num[i]!=b.num[i])
            {
                return a.num[i]-b.num[i];
            }
        }
        return 0;
    }
};

set<BigNum> S;
int dig[32];
int fac[10];

int main()
{
    freopen("C-large.out","w",stdout);
    BigNum m;
    int i,j,k,f,g;
    printf("Case #1:\n");
    for(i=1;i<=500;i++)
    {
        memset(dig,0,sizeof(dig));
        memset(fac,0,sizeof(fac));
        for(j=0;j<32;j++)
        {
            if((j==0)||(j==31))
            {
                dig[j]=1;
            }
            else
            {
                dig[j]=rand()%2;
            }
        }
        m=0;
        f=1;
        for(k=2;k<=10;k++)
        {
            m=0;
            for(j=0;j<32;j++)
            {
                m=m*k+dig[j];
            }
            g=1;
            for(j=2;j<=10000;j++)
            {
                if(m%j==0)
                {
                    fac[k]=j;
                    g=0;
                    break;
                }
            }
            if(g==1)
            {
                f=0;
                break;
            }
        }
        if((f==1)&&(S.insert(m).second==true))
        {
            for(j=0;j<32;j++)
            {
                printf("%d",dig[j]);
            }
            for(k=2;k<=10;k++)
            {
                printf(" %d",fac[k]);
            }
            printf("\n");
        }
        else
        {
            i--;
        }
    }
    return 0;
}
