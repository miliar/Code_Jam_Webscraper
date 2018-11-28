#include <cstdio>
#include <cmath>
#include <map>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>
#include<time.h>
using namespace std;


//****************************************************************
// Miller_Rabin
//****************************************************************
const int S=20;



long long mult_mod(long long a,long long b,long long c)
{
    a%=c;
    b%=c;
    long long ret=0;
    while(b)
    {
        if(b&1){ret+=a;ret%=c;}
        a<<=1;
        if(a>=c)a%=c;
        b>>=1;
    }
    return ret;
}




long long pow_mod(long long x,long long n,long long mod)//x^n%c
{
    if(n==1)return x%mod;
    x%=mod;
    long long tmp=x;
    long long ret=1;
    while(n)
    {
        if(n&1) ret=mult_mod(ret,tmp,mod);
        tmp=mult_mod(tmp,tmp,mod);
        n>>=1;
    }
    return ret;
}




bool check(long long a,long long n,long long x,long long t)
{
    long long ret=pow_mod(a,x,n);
    long long last=ret;
    for(int i=1;i<=t;i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1) return true;
        last=ret;
    }
    if(ret!=1) return true;
    return false;
}


bool Miller_Rabin(long long n)
{
    if(n<2)return false;
    if(n==2)return true;
    if((n&1)==0) return false;
    long long x=n-1;
    long long t=0;
    while((x&1)==0){x>>=1;t++;}
    for(int i=0;i<S;i++)
    {
        long long a=rand()%(n-1)+1;
        if(check(a,n,x,t))
            return false;
    }
    return true;
}


//************************************************
//pollard_rho
//************************************************
long long factor[100];
int tol;

long long gcd(long long a,long long b)
{
    if(a==0)return 1;
    if(a<0) return gcd(-a,b);
    while(b)
    {
        long long t=a%b;
        a=b;
        b=t;
    }
    return a;
}

long long Pollard_rho(long long x,long long c)
{
    long long i=1,k=2;
    long long x0=rand()%x;
    long long y=x0;
    while(1)
    {
        i++;
        x0=(mult_mod(x0,x0,x)+c)%x;
        long long d=gcd(y-x0,x);
        if(d!=1&&d!=x) return d;
        if(y==x0) return x;
        if(i==k){y=x0;k+=k;}
    }
}
void findfac(long long n)
{
    if(Miller_Rabin(n))
    {
        factor[tol++]=n;
        return;
    }
    long long p=n;
    while(p>=n)p=Pollard_rho(p,rand()%(n-1)+1);
    findfac(p);
    findfac(n/p);
}
int N, J;
int a[64];
long long b[25];
long long c[25];
map<long long, long long>mp;
long long getBase(int base) {
    long long res = 0;
    for (int i = 0; i < N; i++) {
        res = res*base + a[i];
    }
    return res;
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("a2.out","w",stdout);
    srand(time(NULL));
    int cas;
    scanf("%d", &cas);
    for (int cas_n = 0; cas_n < cas; cas_n++) {
        printf("Case #%d:\n", cas_n+1);
        scanf("%d%d", &N, &J);
        mp.clear();
        for (int j_n = 0; j_n < J; j_n++) {
            a[0] = a[N-1] = 1;
            for (int i = 1; i <= N-2; i++) a[i] = 0;
            while (true) {
                a[1+(rand()%(N-2))] = rand()%2;
                bool f = false;
                for (int i = 2; i <= 10; i++) {
                    b[i] = getBase(i);
                    if (i == 2 && mp[b[i]] == 1) f = true;
                    if (Miller_Rabin(b[i])) f = true;
                    tol = 0;
                    findfac(b[i]);
                    c[i] = factor[0];
                    if (tol == 0 || c[i] == b[i]) f = true;
                }
                if (!f) break;
            }
            mp[b[2]] = 1;
            for (int i = 0; i < N; i++) printf("%d", a[i]);
            for (int i = 2; i <= 10; i++) {
                printf(" %lld", c[i]);
            }
            puts("");
        }
    }
    return 0;
}
