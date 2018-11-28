#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define forn(i, n) for(int i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;

int T,n,r,s,p;
int kr,ks,kp;
char c[4400][4400];
string ans,tans;

void make(int i, int j)
{
	if(i==n+1)
		return;

	if(c[i][j]=='R')
		c[i+1][2*j]='R',c[i+1][2*j+1]='S';
	if(c[i][j]=='S')
		c[i+1][2*j]='S',c[i+1][2*j+1]='P';
	if(c[i][j]=='P')
		c[i+1][2*j]='P',c[i+1][2*j+1]='R';	

	make(i+1,2*j);
	make(i+1,2*j+1);
}

void swaper(int pos, int kol)
{
	forn(i,kol)
		swap(c[n][pos+i],c[n][pos+kol+i]);
}

void minim()
{
	//cout <<l<<' '<<size<<endl;
	//cout <<"comp "<<c[n][l]<<' '<<c[n][l+size]<<endl;
	
	for(int size=1; size<(1<<n); size*=2)
	{
		for(int l=0; l<(1<<n)-size; l+=2*size)
		forn(i,size)
		{
			if(c[n][l+i]<c[n][l+size+i])
				break;
			if(c[n][l+i]>c[n][l+size+i])
			{
				//cout <<"swap "<<l<<' '<<l+size<<endl;
				swaper(l,size);
	    		break;
		    }
		}
	}
}

bool ok()
{
	int kr=0,ks=0,kp=0;
	forn(i,1<<n)
	{
		if(c[n][i]=='R')
			kr++;
		if(c[n][i]=='S')
			ks++;
		if(c[n][i]=='P')
			kp++;
	}
	if(kr==r && ks==s && kp==p)
		return 1;
	return 0;		
}

void pr()
{
	tans="";
	forn(i,1<<n)
		tans+=c[n][i];
}

void print()
{
	cout <<endl;
	forn(i,n+1)
	{
		forn(j,1<<i)
			cout <<c[i][j];
		cout <<endl;
	}
	cout <<endl;
}

int main()
{
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);

	cin >>T;
	forn(I,T)
	{
		cin >>n>>r>>p>>s;
		cout <<"Case #"<<I+1<<": ";
		
		ans="zz";

		c[0][0]='R';
		make(0,0);
		//print();
		minim();
		//print();
		//continue;

		if(ok())
		{
			pr();
			ans=min(ans,tans);
		}

		c[0][0]='S';
		make(0,0);
		minim();

		if(ok())
		{
			pr();
			ans=min(ans,tans);
		}
		c[0][0]='P';
		make(0,0);
		minim();

		if(ok())
		{
			pr();
			ans=min(ans,tans);
		}

		if(ans=="zz")
			ans="Impossible";
		cout <<ans<<endl;
	}


	
	return 0;
}