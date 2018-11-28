#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define mp make_pair
#define INF (1e9)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;

const double eps = 1e-3;
const int ss=(int)1e6+3;
const int base=inf;

bool pred (const pair<int,int>& i, const pair<int,int>& j) 
{
    if (i.first==j.first)
        return i.second>j.second;
    else
        return i.first>j.first;
}
int p[10000005] = {0};
int d[10000005] = {0}; 
bool isPalindrom(LL x)
{
	LL res = 0;
	LL copy = x;
 	while(copy>0)
	{
		res*=10;
		res+=copy%10;
		copy/=10;
	}
	if(x==res) return true;
	else return false;
}
int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	FOR(i,1e7+1)
	{
		LL rt = i*i;
		p[i] = isPalindrom(i) && isPalindrom(rt);
	}
	FOR(i,1e7+1)
	{
		d[i+1] = d[i] + p[i]; 
	}
	int t;
	cin>>t;
	FOR(ppp,t)
	{
		LL a,b;
		cin>>a>>b;
		LL ra = ceil(sqrt(a));
		LL rb = floor(sqrt(b));
		cout<<"Case #"<<ppp+1<<": "<<d[rb+1] - d[ra]<<endl;
	}
	return 0;
}
