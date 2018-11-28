//==========================================================================
// Author      : NIRWAN DOGRA
// Version     : 4.3.2
// Copyright   : Your copyright notice
// Description : C++, Ansi-style
//============================================================================
#include<algorithm>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<string>
#include <stdio.h>
#include <stdlib.h>
//////////definitions
#define dd cout<<"HERE"<<endl;
#define gg getch();
#define pi pair<int,int>
#define pii pair<pi,int>
#define ff first
#define ss second
#define ST set<int>
#define VEC vector<int>
#define QU queue<int>
#define MAP map<int ,int>
#define l long
#define ll long long
#define forr(i,n) for(int i=0;i<n;i++)
#define forrr(i,j,n) forr(i,n){forr(j,n)
#define S(n) scanf("%d",&n);
#define P(n) printf("%d\n",n);
#define SL(n) scanf("%lld",&n);
#define PL(n) printf("%lld\n",n);
#define C(n) cin>>n;
#define DEBUG if(0)
#define PAUSE system("pause");
#define SET(a,val) memset(a,val,sizeof a);
#define pb push_back
#define CO(n) cout<<n<<endl;
#define MOD 1000000007
#define INF 1000000007
#define MAXI 11111111

using namespace std;
//power function
inline int max_(int a,int b){if(a>=b){return a;}else return b;}
inline int min_(int a,int b){if(a>=b){return b;}else {return a;}}
inline int mod(int a,int b){return (a < b ? a : a % b); }

template< class T > T sq(T &x) { return x * x; }
template< class T > T abs(T &n) { return (n < 0 ? -n : n); }
template< class T > T max(T &a, T &b) { return (!(a < b) ? a : b); }
template< class T > T min(T &a, T &b) { return (a < b ? a : b); }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > T mod(T &a, T &b) { return (a < b ? a : a % b); }
template< class T > bool inside(T &a, T &b, T &c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }


////MAIN CODE BEGINS NOW...........

ll int a[MAXI+10];

bool palin(ll int vv)
{
	int hh[22];int temp;
	forr(i,20)
	{
		if(vv==0)
		{
			temp=i;
			break;
		}
		hh[i]=vv%10;
		vv=vv/10;
	}
	forr(i,temp)
	{
		if(hh[i]!=hh[temp-i-1])
		{
			return 0;
		}
	}
	return 1;
} 

int tot;map<ll ,ll >pos;
int pre()
{
   tot=0;
   forr(i,MAXI)
   {
   	ll val=(ll)i*(ll)(i);;
   	if(palin(val) && palin(i))
   	{
   		a[tot]=val;
   		pos[val]=tot++;
   	}
   }
}

int main()
{
	#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout);
    #endif
    pre();
    //forr(i,tot)
    {
    	//cout<<a[i]<<" ";
    }
    //CO("")
int T;C(T);ll int k,aa,bb;int N;
k=0;ll int ans;;

while(T--)
{
	C(aa>>bb)
	int ele1=*lower_bound(a,a+tot,bb);
	int ele2=*lower_bound(a,a+tot,aa);
	int extra=0;
	if(ele1<=bb)
	{
		extra++;
	}
	if(ele2>=aa)
	{
		extra++;
	}
	ans=pos[*lower_bound(a,a+tot,bb)];
	ans-=pos[*lower_bound(a,a+tot,aa)];
	if(extra==2)
	{
		CO("Case #"<<(++k)<<": "<<ans+1)
		continue;
	}
	if(extra==1)
	{
		CO("Case #"<<(++k)<<": "<<ans)
		continue;
	}
	if(extra==0)
	{
		CO("Case #"<<(++k)<<": "<<ans-1)
		continue;
	}
}
return 0;
}


