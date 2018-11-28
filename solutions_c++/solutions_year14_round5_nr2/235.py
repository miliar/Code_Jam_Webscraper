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
int t,p,q;
int h[1005];
int g[1005];
int numneed[1005];
int numrem[1005];
int numleave[1005];
int i,j;
LL dp[1005][105];
int n;


LL hitung(LL diff, LL pos) {
	if (diff < -1)
		return -1000000000000LL;
	if (pos == n)
		return 0;
	if (diff < -1)
		return -1000000000000LL;
	LL &ret = dp[diff+1][pos];
	if (ret>=0)
		return ret;
	ret = 0;
	ret = max(ret, hitung(diff + numleave[pos], pos+1));
	//try to take
	if (diff == -1) {
		int hnow = h[pos] - q;
		if (hnow > 0)
		{
			int needhit = 0;
			int tower = 0;
			int maxi = -1000000;
			for (int i = 0; i <= 10; i++) {
				if (hnow - q * i > 0) {
					int needhitnow = 0;
					while (hnow - q*i - p*needhitnow > 0)
						++needhitnow;
					if (i - needhitnow > maxi && needhitnow > 0) {
						maxi = i - needhitnow;
						needhit = needhitnow;
						tower = i;
					}
				}
			}
			/*
			bool canhold = false;
			while (true) {
				if ((hnow - needhit * p)%q > 0 && (hnow - needhit * p)%q <= p) {
					canhold = true;
					break;
				}
				if ((hnow - needhit * p)%q == 0 && p >= q) {
					canhold = true;
					break;
				}
				if (hnow - needhit * p <= p)
					break;
				++needhit;
			}
			int tower = 0;
			while ((hnow-(needhit) *p) - q*(tower+1) > 0)
				++tower;
			++needhit;
			if (!canhold)
				tower = 0;*/
			if (maxi > -1000000 && needhit <= tower + 1)
				ret = max(ret, g[pos] + hitung(tower - needhit, pos+1));
		}
	}
	else {
		int hnow = h[pos];
		int needhit = 0;
		int tower = 0;
		int maxi = -1000000;
		for (int i = 0; i <= 10; i++) {
			if (hnow - q * i > 0) {
				int needhitnow = 0;
				while (hnow - q*i - p*needhitnow > 0)
					++needhitnow;
				if (i - needhitnow > maxi && needhitnow > 0) {
					maxi = i - needhitnow;
					needhit = needhitnow;
					tower = i;
				}
			}
		}
		/*int needhit = 0;
		while (true) {
			if ((hnow - needhit * p)%q > 0 && (hnow - needhit * p)%q <= p)
				break;
			if ((hnow - needhit * p)%q == 0 && p >= q)
				break;
			if (hnow - needhit * p <= p)
				break;
			++needhit;
		}
		int tower = (hnow - needhit * p)/q;
		while ((hnow-(needhit) *p) - q*(tower+1) > 0)
			++tower;
		++needhit;
		if (diff == 0 && pos == 0)
			printf("%d %d\n",needhit, tower);*/
		if (maxi > -1000000 && needhit<= tower + diff + 1) {
			ret = max(ret, g[pos] + hitung(tower + diff - needhit, pos+1));
		}
	}
	return ret;
}

int main()
{
	int cs = 0;
	scanf("%d",&t);
	while (t--) {
		memset(dp,-1,sizeof(dp));
		scanf("%d %d %d",&p, &q, &n);
		for (i=0;i<n;++i)
			scanf("%d %d",&h[i],&g[i]);
		for (i=0;i<n;++i) {
			numleave[i] = h[i]/q;
			if (h[i]%q!=0)
				numleave[i]++;
			for (j=0;j<=10;++j) {
				if ((h[i] - p*j)>q && (h[i]-p*j)%q <= p) {
					numneed[i] = j + 1;
					numrem[i] = (h[i]-p*j)/q;
					if ((h[i]-p*j)%q == 0)
						--numrem[i];
					break;
				}
				if ((h[i]-p*j) <= 0) {
					numneed[i] = j;
					numrem[i] = 0;
					break;
				}
			}
		}
		printf("Case #%d: %I64d\n",++cs, hitung(0, 0));
	}
}
