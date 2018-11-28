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
LL t,n,i,p,q,r,s;
LL arr[1000005];
int main()
{
	scanf("%I64d",&t);
	LL cs = 0;
	while (t--) {
		scanf("%I64d %I64d %I64d %I64d %I64d",&n, &p, &q, &r, &s);
		LL sum = 0;
		for (i=0;i<n;++i) {
			arr[i] = ((i*p+q)%r) + s;
			sum += arr[i];
		}
		LL sumleft = 0;
		LL summid = 0;
		LL posl;
		LL res = 1000000000000000000LL;
		summid = arr[0];
		LL sumright = sum - arr[0];
		res = max(arr[0], sumright);
		posl = 0;
		for (i=1;i<n;++i) {
			while (posl < i) {
				res = min(res,max(max(sumleft,summid),sumright));
				if (sumleft > summid)
					break;
				sumleft += arr[posl];
				summid -= arr[posl];
				res = min(res,max(max(sumleft,summid),sumright));
				++posl;
			}
			res = min(res,max(max(sumleft,summid),sumright));
			if (posl > 1)
				res = min(res,max(max(sumleft - arr[posl-1],summid + arr[posl-1]),sumright));
			summid += arr[i];
			sumright -= arr[i];
			res = min(res,max(max(sumleft,summid),sumright));
			if (posl > 1)
				res = min(res,max(max(sumleft - arr[posl-1],summid + arr[posl-1]),sumright));
		}
		while (posl < n) {
			res = min(res,max(max(sumleft,summid),sumright));
			if (sumleft > summid)
				break;
			sumleft += arr[posl];
			summid -= arr[posl];
			res = min(res,max(max(sumleft,summid),sumright));
			++posl;
		}
		res = min(res,max(max(sumleft,summid),sumright));
			if (posl > 1)
				res = min(res,max(max(sumleft - arr[posl],summid + arr[posl]),sumright));
		sumleft = 0;
		sumright = sum;
		for (i=0;i<n;++i) {
			res = min(res,max(sumleft,sumright));
			sumleft += arr[i];
			sumright -= arr[i];
			res = min(res,max(sumleft,sumright));
		}
		printf("Case #%I64d: %.15lf\n",++cs, 1.0*(sum-res)/(1.0*(sum)));
	}
}
