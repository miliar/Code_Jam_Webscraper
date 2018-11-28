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
const int MN=1000+100;

int t,n;
int list[MN];
int cnt[MN];
pie srt[MN]; 
int dp[MN][MN];
int fll(int l,int r)
{
	if (l+r>=n) return 0;
	if (dp[l][r]!=-1) return dp[l][r];
	int & res=dp[l][r];
	res=(1<<29);
	int k=l+r;
	int x=srt[k].second;
	res=min(cnt[x]+fll(l+1,r),(n-k-1-cnt[x])+fll(l,r+1));
	return res;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		cin>>n;
		for (int i=0;i<n;i++) cin>>list[i],srt[i]=pie(list[i],i);
		sort(srt,srt+n);
		for (int i=0;i<n;i++)
		{
			cnt[i]=0;
			for (int j=0;j<i;j++)
				cnt[i]+=(list[j]>list[i]);
		}
		memset(dp,-1,sizeof(dp));
		cout<<"Case #"<<tc<<": "<<fll(0,0)<<endl;
	}
	return 0;
}
