
//Miller_Rabin �㷨�ж�����//
//Pollard_rho�ֽ�����//
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <iostream>
#define N 50010
typedef long long ll;
using namespace std;
const int S=20; //����㷨���ж�����,SԽ��,�д����ԽС
//����ΪMiller_Rabin�ж�����//
ll n,m;
ll mult_mod(ll a,ll b,ll c)  //����a*b%c,�����ݼ�//
{
    a%=c;
    b%=c;
    ll ret=0;
    while(b)
    {
        if(b&1)
            {ret+=a;ret%=c;}
        a<<=1;
        if(a>=c)
            a%=c;
        b>>=1;
    }
    return ret;
}
//����x^n%c,������//
ll pow_mod(ll x,ll n,ll mod)
{
    if(n==1)    return x%mod;
    x%=mod;
    ll tmp=x;
    ll ret=1;
    while(n)
    {
        if(n&1) ret=mult_mod(ret,tmp,mod);
        tmp=mult_mod(tmp,tmp,mod);
        n>>=1;
    }
    return ret;
}

bool check(ll a,ll n,ll x,ll t)
{
    ll ret = pow_mod(a,x,n);
    ll last = ret;
    for(int i =1;i<=t;i++)
    {
        ret = mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1)  return true;        //�Ǻ���//
        last  = ret;
    }
    if(ret!=1)  return true;
    return false;
}
// Miller_Rabin()�㷨�����ж�
//����������true.(������α�����������ʼ�С)
//��������false;
bool Miller_Rabin(ll n)
{
    if(n<2) return false;
    if(n==2) return true;
    if((n&1)==0)    return false;   //�ж�ż��//
    ll x = n-1;
    ll t = 0;
    while((x&1)==0){x>>=1;t++;}   //�ҳ�n-1�Ķ������������Ķ��ٸ�1//
    for(int i=0;i<S;i++)
    {
        ll a=rand()%(n-1)+1;        //�������һ��1��n-1������//
        if(check(a,n,x,t))
            return false;
    }
    return true;
}

// pollard_roh�������ֽ��㷨//
ll factor[100];
int tol;
ll gcd(ll a,ll b)
{
    if(a==0)    return 1;
    if(a<0) return gcd(-a,b);
    while(b)
    {
        ll t=a%b;
        a=b;
        b=t;
    }
    return a;
}
ll Pollard_rho(ll x,ll c)
{
    ll i=1,k=2;
    ll x0=rand()%x;     //����һ��0~x-1������//
    ll y=x0;
    while(1)
    {
        i++;
        x0=(mult_mod(x0,x0,x)+c)%x;
        ll d=gcd(y-x0,x);
        if(d!=1&&d!=x)  return d;
        if(y==x0)   return x;
        if(i==k){
            y=x0;k+=k;
        }
    }
}

void findfac(ll n)
{
    if(Miller_Rabin(n))
    {
        factor[tol++]=n;
        return;
    }
    ll p=n;
    while(p>=n) p=Pollard_rho(p,rand()%(n-1)+1);
    findfac(p);
    findfac(n/p);
}
ll ans[N];
bool judge(ll x)
{
    ll i,j;
    ll tmp;
    for(i=2;i<=10;i++)
    {
        tmp=0;
        for(j=0;j<n;j++)
        {
            tmp*=i;
            tmp+=((1<<(n-j-1))&x)>0?1:0;
        }
        ans[i]=tmp;
        if(Miller_Rabin(ans[i]))
            return 0;
        else
        {
            tol=0;
            findfac(ans[i]);
            ans[i]=factor[0];
        }
    }
    for(j=0;j<n;j++)
        printf("%d",((1<<(n-j-1))&x)>0?1:0);
    printf(" ");
    for(i=2;i<=10;i++)
    {
        printf("%I64d",ans[i]);
        if(i==10)
            printf("\n");
        else
            printf(" ");
    }
    return 1;
}
int main()
{
    int T,i1=1;
    ll k;
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%I64d%I64d",&n,&m);
        k=0;k=1;k^=(1<<(n-1));
        printf("Case #%d:\n",i1++);
        while(1)
        {
            if(m==0)
                break;
            if(judge(k))
                m--;
            k+=2;
            if(k>(1<<n))
                break;
        }
    }
    return 0;
}
