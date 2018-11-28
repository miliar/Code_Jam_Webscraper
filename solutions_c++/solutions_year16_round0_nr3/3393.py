#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <time.h>
#include <iomanip>
#include <cctype>

using namespace std;

typedef long long ll;

const int S=8; ///?????????

ll mult_mod(ll a,ll b,ll c)
{
    a%=c;
    b%=c;
    ll ret=0;
    ll temp=a;
    while(b)
    {
        if(b&1)
        {
            ret+=temp;
            if(ret>c)
                ret-=c;//???????
        }
        temp<<=1;
        if(temp>c)
            temp-=c;
        b>>=1;
    }
    return ret;
}

///??ret=(a^n)%mod
ll pow_mod(ll a,ll n,ll mod)
{
    ll ret=1;
    ll temp=a%mod;
    while(n)
    {
        if(n&1)
            ret=mult_mod(ret,temp,mod);
        temp=mult_mod(temp,temp,mod);
        n>>=1;
    }
    return ret;
}

///??????? a^(n-1)=1(mod n)???n?????
///?????????,?n-1=x*2^t
///?????true,????????false
bool check(ll a,ll n,ll x,ll t)
{
    ll ret=pow_mod(a,x,n);
    ll last=ret;//??????x
    for(int i=1;i<=t;i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1)
            return true;//????????
        last=ret;
    }
    if(ret!=1)
        return true;//???,?????
    return false;
}


///Miller_Rabbin??
///?????true(??????),????false
bool Miller_Rabbin(ll n)
{
    if(n<2) return false;
    if(n==2) return true;
    if((n&1)==0) return false;//??
    ll x=n-1;
    ll t=0;
    while((x&1)==0)
    {
        x>>=1;
        t++;
    }
    srand(time(NULL));
    for(int i=0;i<S;i++)
    {
        ll a=rand()%(n-1)+1;
        if(check(a,n,x,t))
            return false;
    }
    return true;
}

ll factor[100];
int tot;//?????? 0~to-1
ll gcd(ll a,ll b)
{
    ll t;
    while(b)
    {
        t=a;
        a=b;
        b=t%b;
    }
    if(a>=0) return a;
    return -a;
}

ll pollard_rho(ll x,ll c)
{
    ll i=1,k=2;
    srand(time(NULL));
    ll x0=rand()%(x-1)+1;
    ll y=x0;
    while(1)
    {
        i++;
        x0=(mult_mod(x0,x0,x)+c)%x;
        ll d=gcd(y-x0,x);
        if(d!=1&&d!=x) return d;
        if(y==x0) return x;
        if(i==k)
        {
            y=x0;
            k+=k;
        }
    }
}

void findfac(ll n,int k)
{
    if(n==1)
        return;
    if(Miller_Rabbin(n))
    {
        factor[tot++]=n;
        return;
    }
    ll p=n;
    int c=k;
    while(p>=n)
        p=pollard_rho(p,c--);
    findfac(p,k);
    findfac(n/p,k);
}


int t;
const int n=16;
const int m=50;
int counter=0;
int num[n];
ll ch[11][16];
ll sum[11];

//void table()
//{
//	for(i=2;i<=(1<<(n+1));i++)
//	{
//		if(isprime[i]==0)
//		{
//			for(j=2*i;j<=(1<<(n+1));j+=i)
//			{
//				isprime[j]=1;
//			}
//		}
//	}
//}

void table2()
{
	long long i,j,k;
	for(i=2;i<=10;i++)
	{
		ll tmp=1;
		ch[i][0]=tmp;
		for(j=1;j<=15;j++)
		{
			tmp*=i;
			ch[i][j]=tmp;
		}
	}
}

void trans(ll x)
{
	long long i,j,k;
	for(i=0;i<=15;i++)
	{
		num[i]=(x&(1<<i))?1:0;
	}
}

int main()
{
	//	table();
	long long i,j,k;
	freopen("out2","w",stdout);
	table2();
	cout<<"Case #1:"<<endl;
	for(i=((1<<(n-1))+1);;i+=2)
	{
//		cout<<counter<<endl;
		trans(i);
		sum[2]=i;
		bool flag=true;
		for(j=2;j<=10;j++)
		{
			sum[j]=0;
			for(k=0;k<=15;k++)
			{
				sum[j]+=num[k]*ch[j][k];
			}
			if(Miller_Rabbin(sum[j]))
			{
				flag=false;
				break;
			}
		}
		if(flag)
		{
			counter++;
			for(j=15;j>=0;j--)
				cout<<num[j];
			for(j=2;j<=10;j++)
			{
				tot=0;
		        findfac(sum[j],107);
		        sort(factor,factor+tot);
		        cout<<" "<<factor[0];
			}
			cout<<endl;
		}
		if(counter==50)break;
	}
	fclose(stdout);
	return 0;
}
