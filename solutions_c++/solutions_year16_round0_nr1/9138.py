
#include"stdio.h"
#include"iostream"
#include"vector"
#include"string"
#include"string.h"
#include"algorithm"
#include"cmath"
#include"set"
#include"bitset"
#include"map"
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<ctime>
#include<queue>

using namespace std;
 
 
#define ABS(a) ((a<0)?(-a):a)
#define MAX(a,b) ((a<b)?(b):(a))
#define MIN(a,b) ((a>b)?(b):(a))
#define FOR(i,n) for(int i=0;i<n;++i)
#define FORA(a,n) for(int i=a;i<n;++i) 
#define pb push_back
#define MP make_pair
 
#define TN5 100000 
#define TN6 1000000 
#define TN7 10000000 
#define TN8 100000000
#define TN9 1000000000 
#define TN10 10000000000 
 
typedef long long LL; 
typedef long double LD;
const long double eps=0.000000001;
const double pi=3.141592653589;
#define MAXN 500005

const LL mod=1000000007;
 

LL gcd(LL a,LL b)
{
	if(a>b)
		swap(a,b);

	while(a!=0&&b!=0)
	{
		b%=a;
		swap(a,b);
	}
	return a+b;
}
LL poww(LL v, LL p)
{
	 if (p == 0) return 1;

	 if (p & 1)
	 {
	  return (poww(v, p - 1) * v) % mod;
	 }
	 else
	 {
	  LL t = poww(v, p / 2);
	  return (t * t) % mod;
	 }
}
void calc_primes(int n,vector<bool> &primes)
{
	//vector<bool> primes;//<-or create as global;
	primes.resize(n,true);
	primes[1]=false;
	
	for(int i=2;i*i<n;++i)
	{
		if(!primes[i])continue;
		for(int j=i*i;j<n;j+=i)
		{
			primes[j]=false;
		}
	}
}
LL ext_gcd (LL a, LL b, LL & x, LL & y) {
	if (a == 0) {
		x = 0; y = 1;
		return b;
	}
	LL x1, y1;
	LL d = ext_gcd (b%a, a, x1, y1);
	x = y1 - (b / a) * x1;
	y = x1;
	return d;
}
bool vect_comp(pair<int,int> a,pair<int,int> b)
{
	return (a.first*b.second-a.second*b.first > 0);
}
bool get_bit(int &v,char &num)
{
	return ((v>>num)&1);
}
void set_bit(int &v,const char &num)
{
	v = v | (1<<num);
}
int count_bit(int v)
{
	int cnt = 0;
	while(v>0)
	{
		cnt+=v&1;
		v = v>>1;
	}
	return cnt;
}



int n,n0;
int t;
bool cif[10];
int cnt;

void parse(int n)
{
	while(n>0)
	{
		if(cif[n%10]==false)
		{
			cif[n%10]=true;
			cnt++;
		}
		n/=10;
	}
}

void solve()
{
	FOR(i,10)
	{
		cif[i]=0;
	}
	cnt=0;
	cin>>n;
	if(n==0)
	{
		cout<<"INSOMNIA\n";
		return;
	}	
	n0=n;	
	parse(n);
	while(cnt<10)
	{
		n+=n0;
		parse(n);
	}
	cout<<n<<endl;

}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("OUTPUT.TXT","w",stdout);
	cin>>t;
	FOR(i,t)
	{
		//LL startTime = clock();
		cout<<"Case #"<<i+1<<": ";
		solve();
		//printf("\n\n\t TIME: %.5lf", double((clock() - startTime)) / 1000.0f); /// CLOCKS_PER_SEC));
	}
	
	
	return 0;	

	return 0;  
		
	return 0;  
  
}
