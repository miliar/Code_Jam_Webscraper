#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<ctype.h>
#include<string>
#include<cstring>
#include<iostream>

#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<bitset>
#include<set>
#include<list>
#include<complex>

#define GC getchar_unlocked
#define MAX(a,b) ({a>b?a:b;})
#define MIN(a,b) ({a>b?b:a;})
#define P(x) printf("%d\n",x);
#define PLL(x) printf("%lld\n",x);
#define MP make_pair
#define PB push_back
#define SZ size()
#define CL clear()
#define X first
#define Y second
#define MOD 1000000007
#define max 10000000

using namespace std;
typedef long long int LL;
typedef unsigned long long int ULL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef vector<pair<int,int> > VPII;
typedef stack<int> SI;

template<class T>inline T input(T x){char c=GC();x=0;T s=1;while(c<48||c>57){if(c=='-')s=-1;c=GC();}while(c>=48&&c<=57){x=(x<<3)+(x<<1)+c-48;c=GC();}return x*s;}
template<class T>inline void output(T a){if(a){T v=a%10;output(a/10);putchar((char)(v+'0'));}}
template<class T>inline T gcd(T a,T b){return b?gcd(b,a%b):a;}
template<class T>inline T modinv(T a,T n){T i=n,v=0,d=1;while(a>0){T t=i/a,x=a;a=i%x;i=x;x=d;d=v-t*x;v=x;}return (v+n)%n;}
LL modpow(LL n ,LL k,LL mod){LL ans=1;while(k>0){if(k&1)ans=(ans*n)%mod;k>>=1;n=(n*n)%mod;}return ans%mod;}

int a[max + 10];

int checkPalin(LL x)
{
	LL str[20];
	int i = 0,j;
	while(x)
	{
		str[i++] = x % 10;
		x /= 10;
	}
	for(j=0;j<i/2;j++)
		if(str[j] != str[i-j-1])
			return 0;
	return 1;
}

void preCalc()
{
	LL i;
	a[0] = 0;
	for(i=1;i<=max;i++)
	{
		LL x = i * i;
		if(checkPalin(i) && checkPalin(x))
			a[i] = a[i-1] + 1;
		else
			a[i] = a[i-1];
	}
}

int main()
{
	preCalc();
	int test,t;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		LL A,B;
		scanf("%lld%lld",&A,&B);
		LL x = sqrt(A);
		if(x * x == A)
			x--;
		LL y = sqrt(B);
		printf("Case #%d: %d\n",t,a[y] - a[x]);
	}
	return 0;
}
