#include <iostream>
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <queue>
using namespace std;

typedef long long LL;

#define MAX(a,b) (a>=b?a:b)
#define MIN(a,b) (a<=b?a:b)

#ifndef ONLINE_JUDGE
    #define gc getchar
#else
    #define gc getchar_unlocked
#endif
#define LL long long

typedef struct
{
    int val;
    int in;
}node;
bool cmp(node n1,node n2)
{
    if(n1.val<n2.val)
        return true;
    else
        return false;
}

LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }
int abs(int a) { return a >=0 ? a : -a; }
inline void input(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(; ((c<48 || c>57) && c != '-'); c = gc());
    if(c=='-') {
    	neg = 1;
    	c = gc();
    }
    for(; c>47 && c<58 ; c = gc()) {
    	x = (x<<1) + (x<<3) + c - 48;
    }
    if(neg)
    	x = -x;
}

inline void Output(int X)
{
    if(X<0)
    {
        putchar('-');
        X=-X;
    }
    int Len=0,Data[10];
    while(X)
    {
        Data[Len++]=X%10;
        X/=10;
    }
    if(!Len)
        Data[Len++]=0;
    while(Len--)
        putchar(Data[Len]+48);
}

//clock_t start=clock(),end;
//cout<<"\tTIME="<<(end-start)/CLOCKS_PER_SEC<<endl;

int main(int argc, char** argv)
{
    #ifndef ONLINE_JUDGE
        freopen("in.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
    int t,n,ans=0,sum;
	input(t);
	for(int tc=1;tc<=t;tc++){
		ans=sum=0;
		input(n);
		char a[n+5];
		cin>>a;
		for(int i=0;i<=n;i++){
			int digit=a[i]-'0';
			if(sum<i){
				ans+=i-sum;
				sum=i+digit;
			}
			else{
				sum+=digit;
			}
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
    return 0;
}

