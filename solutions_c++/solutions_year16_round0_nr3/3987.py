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

i64 n,j,t;
int a[20];
bool pr[100100];

void erato()
{
	for(i64 i=2; i<100100; i++)
	{
		if(pr[i]==0)
			for(i64 j=i*i; j<100100; j+=i)
				pr[j]=1;
	}
}

i64 trans(i64 o)
{
	i64 res=0,st=1;
	for(int i=n-1; i>=0; i--)
	{
		res+=a[i]*st;
		st*=o;
	}
	return res;
}


vector <int> v;

bool chk(i64 c)
{
	for(int i=4; i<=1010; i++)
	{
		if(c%i==0 && pr[i]==1)
		{
			v.pb(i);
			return 1;
		}
	}
	return 0;
}

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	erato();
	cout <<"Case #1:\n";

	cin >>n>>j;
	for(i64 I=(1ll<<(n-1))+1; I<(1ll<<(n)); I++)
	{             
		t=I;
		forn(i,n)
		{
			a[i]=t%2;
			t/=2;
		}
		reverse(a,a+n);
		if(a[0]!=1 || a[n-1]!=1)
			continue;
		/*
		forn(i,n)
			cout <<a[i];
		cout <<":";

		for(int i=2; i<10; i++)
			cout <<trans(i)<<' ';
		cout <<endl;
		*/
		//continue;
		
		bool ok=1;
		v.clear();
		for(int i=2; i<=10; i++)
		{
			if(chk(trans(i))==0)
				ok=0;
		}

		if(ok)
		{
			j--;
			forn(i,n)
				cout <<a[i];
			cout <<' ';
			forn(i,9)
				cout <<v[i]<<' ';
			cout <<endl;
		}
		if(j==0)
			break;
	}

	return 0;
}
