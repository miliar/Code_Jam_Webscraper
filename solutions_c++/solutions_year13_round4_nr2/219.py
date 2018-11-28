#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
#include <queue>
#include <set>
#include <map>
using namespace std;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
#define SIZE(x) ((int)(x).size())
#define for0(i,n) for(int i=0;i<(n);i++)
#define for1(i,n) for(int i=1;i<=(n);i++)
#define for0r(i,n) for(int i=(n)-1;i>=0;i--)
#define for1r(i,n) for(int i=(n);i>=1;i--)
typedef long long ll;
typedef pair<int,int> pii;

ll rec(int n,ll p)
{
	if((1LL<<n)==p)return p-1;
	ll half = 1LL<<(n-1);
	if(p<=half)return 0;
	ll g = rec(n-1,p-half);
	return 2*g+2;
}

void solve()
{
	int n;
	ll p;
	scanf("%d %I64d",&n,&p);
	printf(" %I64d",rec(n,p));
	ll t = 1LL<<n;
	int c=0;
	while(t>p)
	{
		t/=2;
		c++;
	}
	printf(" %I64d\n",(1LL<<n)-(1LL<<c));
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,TC=0;
	scanf("%d",&T);
	while (++TC<=T)
	{
		printf("Case #%d: ",TC);
		solve();
	}
	return 0;
}
