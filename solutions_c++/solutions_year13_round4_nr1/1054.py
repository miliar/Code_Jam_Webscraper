#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

struct Pas
{
	int i, j;
	int p;
};

struct PasP
{
	Pas* pp;
};

long long n,m;
Pas	a[10000005];
PasP b[10000005];

bool operator<(const Pas& p1, const Pas& p2)
{
	if(p1.i != p2.i)
		return p1.i < p2.i;

	return p1.j < p2.j;
}

bool operator<(const PasP& p1, const PasP& p2)
{
	if(p1.pp->j != p2.pp->j)
		return p1.pp->j < p2.pp->j;

	return p1.pp->j < p2.pp->j;
}

long long ans1;
long long ans2;

const long long PP = 1000002013;

long long calc(int i)
{
	if(a[i].i == a[i].j)
		return 0;
	
	long long k = a[i].j - a[i].i -1;

	long long ans = (2*n - k)*(k+1)/2;
	ans%=PP;
	ans*=a[i].p;
	ans%=PP;
	return ans;
}

long long calcAns()
{
	int i;
	long long ans=0;
	for(i=0; i<m; ++i)
	{
		ans += calc(i);
		ans %= PP;
	}
	return ans;
}

void read()
{
	int i;
	fin>>n>>m;
	for(i=0; i<m; ++i)
		fin>>a[i].i>>a[i].j>>a[i].p;
	for(int i=0; i<m; ++i)
		b[i].pp = &a[i];
	ans1 = calcAns();
}

bool canSwap(Pas& j, Pas& i)
{
	return (j.i < i.i) && (j.j < i.j) && (j.j >= i.i) && (j.i != i.i) && j.p != 0 && i.p != 0;
}

void sswap(Pas& j, Pas& i)
{
	int l = min(j.p, i.p);
	i.p -= l;
	j.p -= l;
	
	a[m].i = j.i;
	a[m].j = i.j;
	a[m].p = l;
	b[m].pp = &a[m];
	++m;

	a[m].i = i.i;
	a[m].j = j.j;
	a[m].p = l;
	b[m].pp = &a[m];
	++m;
}

void sortt()
{
	sort(a, a+m);
	sort(b, b+m);
}

void solve()
{
	//sort(a, a+m);

	int i;
	long long mm = 0;
	while(m != mm)
	{
		//sort(a, a+m);
		sortt();
		mm = m;
	for(i=0; i<mm; ++i)
	{
		Pas p;
		p.i = p.j = a[i].i;
		PasP pk;
		pk.pp = &p;
		if(a[i].p > 0)
		{
		int j = lower_bound(b,b+mm,pk)-b;
		for(; j<m && b[j].pp->j < a[i].j; ++j)
		{
			if(canSwap(*b[j].pp,a[i]))
			{
				sswap(*b[j].pp,a[i]);
				
				//--i;
				//if(i<0)
				//	i=0;
				break;
			}
		}
		}
	}
	}
}

long long ans()
{
	ans2 = calcAns();
	long long ans = ans1 - ans2;
	ans %= PP;
	ans += PP;
	ans %= PP;
	return ans;
}

void write(int t)
{
	fout<<"Case #"<<t<<": "<<ans()<<endl;
}

int main()
{
	int t,tt;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		read();
		solve();
		write(t);
	}
	return 0;
}

