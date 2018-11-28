/*
	In the Name of God
	Aida Sadat Mousavifar
*/

#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;

#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define N 5019
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
typedef vector<ll> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;

string rep;
void make_rep(ll num)
{
	rep="";
	while(num>0)
	{
		rep=((char)(num%2+'0'))+rep;
		num/=2;
	}
}

ll conv(ll b)
{
	ll val=0;
	FOR(i, (rep.sz))
		val=val*b+rep[i]-'0';
	return val;
}

int check(ll val, ll& div)
{
	for(ll k=2; k*k<=val; k++)
	{
		if(val%k==0)
		{
			div=k;
			return 1;
		}
	}
	return 0;
}

int main()
{
	int T; cin>>T;
	int n,j,t=1; cin>>n>>j;
	cout<<"Case #1:\n";
	for(ll num=((1LL<<(n-1))+1); num<=((1LL<<n)-1); num+=2)
	{
		if(t>j) break;		
		vi divs;
		make_rep(num);			
		for(ll b=2; b<=10; b++)
		{
			ll val=conv(b);		
			ll div=-1;			
			if(check(val, div)==0) goto hell;
			divs.PB(div);		
		}	
		cout<<rep;
		FOR(i,divs.sz) cout<<" "<<divs[i];
		cout<<endl;
		t++;
		hell: ;
	}

}

