// /\||/\||
//
//
//////////////////////
// Program: 
// Written By Alireza Farhadi (LGM)
//////////////////////
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cassert>
#include <csignal>
#include <cmath>
#include <array>
#include <queue>
#include <stack>
#include <string>
#include <regex>
#include <set>
#include <map>
#include <tuple>
#include <list>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define show(x) cerr<<((#x))<<" = "<<((x))<<" "<<endl
#define bit(a,b) (((a)>>(b))&1)
#define get(x,i) (get<((i))>(((x))))
#define ALL(x) ((x)).begin(),((x)).end()
#define Mt make_tuple
#define gcd __gcd
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define bcntll(x) ((__builtin_popcountll(x)))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)
#define list _list

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}

typedef long long ll;
typedef pair<int,int> pie;
typedef tuple<int,int,int> trip;
typedef complex<double> point;

const double eps=1e-8;

int t,n,m;
string list[10000];
bool mark[10000];
int bd,cb;
int c(vector<string> all)
{
	set<string> mark;
	for (string x:all)
	{
		for (int i=0;i<=(int)x.size();i++)
			mark.insert(x.substr(0,i));
	}
	return mark.size();
}
void bt(int a,int cost)
{
	if (a==m)
	{
		for (int i=0;i<n;i++) if (!mark[i]) return ;
		if (cost==bd) cb++;
		else if (cost>bd) bd=cost,cb=1;
		return ;
	}
	vector <int> av;
	for (int i=0;i<n;i++) if (!mark[i])
		av.push_back(i);
	for (int j=0;j<(1<<(int)av.size());j++)
	{
		vector<string> g;
		for (int k=0;k<(int)av.size();k++) if (bit(j,k))
			mark[av[k]]=1,g.push_back(list[av[k]]);
		bt(a+1,cost+c(g));
		for (int k=0;k<(int)av.size();k++) if (bit(j,k))
			mark[av[k]]=0;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		cin>>n>>m;
		for (int i=0;i<n;i++) cin>>list[i];
		memset(mark,0,sizeof(mark));
		bd=-1,cb=0;
		bt(0,0);
		cout<<"Case #"<<tc<<": "<<bd<<" "<<cb<<endl;
	}
	return 0;
}
