#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long ll;
#define INF 1e8
#define maxn 2005+10
#define maxm 100086+10
//#define mod 7
#define eps 1e-7
#define PI acos(-1.0)
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%I64d",&n)
#define scan2(n,m) scanf("%d%d",&n,&m)
#define scans(s) scanf("%s",s);
#define ini(a) memset(a,0,sizeof(a))
#define out(n) printf("%d\n",n)
using namespace std;
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
//****************************************************************  
// Miller_Rabin 算法进行素数测试  
//速度快，而且可以判断 <2^63的数  
//****************************************************************  
const int S=20;//随机算法判定次数，S越大，判错概率越小  
  
  
//计算 (a*b)%c.   a,b都是long long的数，直接相乘可能溢出的  
//  a,b,c <2^63  
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
  
  
  
//计算  x^n %c  
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
  
  
  
  
  
//以a为基,n-1=x*2^t      a^(n-1)=1(mod n)  验证n是不是合数  
//一定是合数返回true,不一定返回false  
bool check(long long a,long long n,long long x,long long t)  
{  
    long long ret=pow_mod(a,x,n);  
    long long last=ret;  
    for(int i=1;i<=t;i++)  
    {  
        ret=mult_mod(ret,ret,n);  
        if(ret==1&&last!=1&&last!=n-1) return true;//合数  
        last=ret;  
    }  
    if(ret!=1) return true;  
    return false;  
}  
  
// Miller_Rabin()算法素数判定  
//是素数返回true.(可能是伪素数，但概率极小)  
//合数返回false;  
  
bool Miller_Rabin(long long n)  
{  
    if(n<2)return false;  
    if(n==2)return true;  
    if((n&1)==0) return false;//偶数  
    long long x=n-1;  
    long long t=0;  
    while((x&1)==0){x>>=1;t++;}  
    for(int i=0;i<S;i++)  
    {  
        long long a=rand()%(n-1)+1;//rand()需要stdlib.h头文件  
        if(check(a,n,x,t))  
            return false;//合数  
    }  
    return true;  
}  
  
  
//************************************************  
//pollard_rho 算法进行质因数分解  
//************************************************  
long long factor[100];//质因数分解结果（刚返回时是无序的）  
int tol;//质因数的个数。数组小标从0开始  
  
long long gcd(long long a,long long b)  
{  
    if(a==0)return 1;//???????  
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
//对n进行素因子分解  
ll findfac(long long n)  
{  
    long long p=n;  
    while(p>=n)p=Pollard_rho(p,rand()%(n-1)+1);  
    return p;
} 
int N,J;
vector<ll> ans;
bool check(string s)
{
	
	ans.clear();
	for(ll i = 2;i <= 10; i++)
	{
		ll ret = 1;
		for(ll j = 1;j < N ; j++)
		{
			ret *= i;
			if(s[j] == '1') ret += 1;
		}
		if(Miller_Rabin(ret)) return false;
		ans.push_back(findfac(ret));
	}
	return true;
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif  
	int T;
	cin>>T;
	int cas = 1;
	while(T--)
	{
		printf("Case #%d:\n",cas++);
		cin>>N>>J;
		ll tol = 1 << (N-2);
		for(int i = 0;i < tol && J >= 1; i++)
		{
			string s = "1";
			int tmp = i;
			for(int j = 0;j < N-2; j++)
			{
				if(tmp%2==1)
					s += '1';
				else
					s += '0';
				tmp /= 2;
			}
			s += "1";
			reverse(s.begin(),s.end());
			if(check(s))
			{
				cout<<s;		
				for(int j = 0;j < ans.size(); j++)
				{
					cout<<' '<<ans[j];
				}
				cout<<endl;
				J--;
			}
		}
	}
    return 0;
}