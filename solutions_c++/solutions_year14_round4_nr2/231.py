//nathanajah's template
//28-11-2012
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <ctime>
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned LL
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(),(a).end()
#ifdef DEBUG
	#define debug(...) \
	fprintf(stderr,__VA_ARGS__)
#else
	#define debug(...) 
#endif
using namespace std;

inline string GetString()
{
	char GS[1000005];
	scanf("%s",GS);string ret=GS;
	return ret;
}

inline char getc()
{
	char c=' ';
	while (c==' ' || c=='\t' || c=='\r' || c=='\n')
		c=getchar();
	return c;
}
//ENDOFTEMPLATE

int bit[1005];
int dp[1005][1005];
int arr[1005];
map <int,int> balik;
int sortarr[1005];
int pos[1005];
int leftless[1005];

int get(int x) {
	int ret = 0;
	while (x>0) {
		ret += bit[x];
		x -= (x&-x);
	}
	return ret;
}

void upd(int x, int y) {
	while (x < 1005) {
		bit[x] += y;
		x += (x&-x);
	}
}

int t,n,i,j;

int hitung(int l, int r) {
	if (l+r==n)
		return 0;
	int &ret = dp[l][r];
	if (ret>=0)
		return ret;
	//put it to the left
	//int posi = l+1;
	int more = n-1-l-r;
	int leftmore = pos[l+r] - leftless[l+r];
	
	ret = hitung(l+1,r) + leftmore;
	ret = min(ret, hitung(l,r+1) + more - leftmore);
	return ret;
}
int main()
{
	scanf("%d",&t);
	int cs = 0;
	while (t--) {
		memset(bit,0,sizeof(bit));
		memset(dp,-1,sizeof(dp));
		balik.clear();
		scanf("%d",&n);
		for (i=0;i<n;++i) {
			scanf("%d",&arr[i]);
			sortarr[i] = arr[i];
		}
		sort(sortarr,sortarr+n);
		for (i=0;i<n;++i) {
			balik[sortarr[i]] = i;
		}
		for (i=0;i<n;++i)
			arr[i] = balik[arr[i]];
		for (i=0;i<n;++i)
			pos[arr[i]] = i;
		for (i=0;i<n;++i) {
			leftless[i] = get(pos[i]+1);
			upd(pos[i]+1, 1);
		}
		printf("Case #%d: %d\n",++cs, hitung(0,0));
	}
}
