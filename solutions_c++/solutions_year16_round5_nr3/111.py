//*
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

double sq(double x)
{
	return x*x;
}

struct xyz
{
	double x, y, z;
	xyz(){}
	xyz(double x, double y, double z):x(x), y(y), z(z){}
	void print()
	{
		printf("%lf %lf %lf\n", x, y, z);
	}
	void print(string s)
	{
		cout<<s<<" ";
		printf("%lf %lf %lf\n", x, y, z);
	}
};

xyz operator+(xyz p, xyz q)
{
	return xyz(p.x+q.x, p.y+q.y, p.z+q.z);
}

xyz operator-(xyz p, xyz q)
{
	return xyz(p.x-q.x, p.y-q.y, p.z-q.z);
}

xyz operator*(xyz p, double x)
{
	return xyz(p.x*x, p.y*x, p.z*x);
}

xyz operator/(xyz p, double x)
{
	return xyz(p.x/x, p.y/x, p.z/x);
}

double dp(xyz p, xyz q)
{
	return p.x*q.x+p.y*q.y+p.z*q.z;
}

xyz cp(xyz p, xyz q)
{
	return xyz(p.y*q.z-p.z*q.y, p.z*q.x-p.x*q.z, p.x*q.y-p.y*q.x);
}

double len(xyz p)
{
	return sqrt(sq(p.x)+sq(p.y)+sq(p.z));
}

xyz norm(xyz p)
{
	return p/len(p);
}

double dis(xyz p, xyz q)
{
	return len(p-q);
}


int n;
double S;

xyz a[2000];
xyz v[2000];

int cnt[2000];
int live[2000];
set<int> edge[2000];

struct EDGE
{
	double s, e;
	EDGE(){}
	EDGE(double s, double e):s(s), e(e){}
};

int eval(int type, int x, int y)
{
	int u;
	if(type == 0) u=1;
	else if(type == 1) u=2;
	else if(type == 2) u=0;
	else u=3;
	return u*100000000+x*10000+y;
}

struct EVENT
{
	double t;
	int type;
	int x, y;
	EVENT(double t, int type, int x):t(t), type(type), x(x), y(0){}
	EVENT(double t, int type, int x, int y):t(t), type(type), x(x), y(y){}
	bool operator<(const EVENT &p) const
	{
		if(abs(t-p.t) > ERR) return t < p.t;
		else
		{
			return eval(type, x, y) < eval(p.type, p.x, p.y);
		}
	}
};

vector<EVENT> ev;

void back(int x)
{
	if(live[x]) return;
	if(!cnt[x]) return;
	live[x]=1;
	for(auto e : edge[x])
	{
		back(e);
	}
}

int param(double x)
{
	int i, j, k;
	ev.clear();
	for(i=0;i<n;i++) cnt[i]=live[i]=0, edge[i].clear();
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			xyz A=a[i]-a[j];
			xyz V=v[i]-v[j];
			double low, high;
			if(len(V) < ERR)
			{
				if(len(A) <= x+ERR)
				{
					low=0;
					high=MAX;
				}
				else continue;
			}
			else
			{
				double aa, bb, cc;
				aa=sq(len(V));
				bb=2*dp(A, V);
				cc=sq(len(A))-sq(x);
				if(sq(bb)-4*aa*cc < 0) continue;
				low=(-bb-sqrt(bb*bb-4*aa*cc))/2/aa;
				high=(-bb+sqrt(bb*bb-4*aa*cc))/2/aa;
				low=max(low, 0.);
				high=max(high, 0.);
			}
			ev.emplace_back(low, 0, i, j);
			ev.emplace_back(high, 1, i, j);
			ev.emplace_back(max(low-S, 0.0), 2, i);
			ev.emplace_back(max(low-S, 0.0), 2, j);
			ev.emplace_back(high, 3, i);
			ev.emplace_back(high, 3, j);
		}
	}
	sort(all(ev));
	if(!ev.size()) return 0;
	if(ev[0].t < ERR && ev[0].type == 2 && ev[0].x == 0);
	else return 0;
	live[0]=1;
	for(auto e : ev)
	{
		if(e.type == 0)
		{
			int x=e.x, y=e.y;
			edge[x].insert(y);
			edge[y].insert(x);
			if(live[x] == live[y]) continue;
			if(!live[x]) swap(x, y);
			back(y);
		}
		else if(e.type == 1)
		{
			edge[e.x].erase(e.y);
			edge[e.y].erase(e.x);
		}
		else if(e.type == 2)
		{
			cnt[e.x]++;
			for(auto f : edge[e.x])
			{
				if(live[f])
				{
					back(e.x);
					break;
				}
			}
		}
		else
		{
			cnt[e.x]--;
			if(cnt[e.x] == 0) live[e.x]=0;
		}
		if(live[1]) return 1;
	}
	return 0;
}

int main()
{
	int i, j, k, l;
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>TT;
	for(T=1;T<=TT;T++)
	{
		cin>>n>>S;
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf", &a[i].x, &a[i].y, &a[i].z, &v[i].x, &v[i].y, &v[i].z);
		}
		double low=0, high=10000000, mid;
		param(2.1);
		for(i=0;i<50;i++)
		{
			mid=(low+high)/2;
			if(param(mid)) high=mid;
			else low=mid;
		}
		printf("Case #%d: %.20lf\n", T, mid);
	}
	return 0;
}
//*/