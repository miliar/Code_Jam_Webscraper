#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:32000000")
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>
#include <bitset>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

VI prefixFunc(const string &s) {
    VI f(SZ(s)); int k=0;
    FOR(i,1,SZ(s)-1) {
        while(k && s[k] != s[i]) k=f[k-1];
        if(s[k] == s[i]) ++k;
        f[i]=k; }
	return f; }
int KMPsearch(const string &s, const string &p) {
    VI f = prefixFunc(p); int k=0, res=0;
    REP(i,SZ(s)) {
        while(k && p[k] != s[i]) k = f[k-1];
        if(p[k] == s[i]) ++k;
		if(k == SZ(p)) k = f[k-1], res++; }
	return res; }


#define N 111
typedef bitset<N> BS;

#define BEAMSIZE 10000
#define ITERS 1

int n,k;
int par[N];
char let[N],cool[N][N];
VI pref[N];

double ans[N];

void go()
{
	struct Rec {
		BS bs;
		char p[5];
		Rec() {
			bs.reset();
			CLEAR(p);
		}
	};
	vector<Rec> a,b;
	a.push_back(Rec());
	REP(step,n)
	{
		b.clear();
		REP(ii,SZ(a)) {
			REP(j,n) if (!a[ii].bs[j] && (par[j] == -1 || a[ii].bs[par[j]]))
			{
				Rec r = a[ii];
				r.bs.set(j);
				REP(qq,k)
				{
					char& pos = r.p[qq];
					if (pos < SZ(pref[qq])) {
						while (pos && cool[qq][pos] != let[j])
							pos = pref[qq][pos-1];
						if (cool[qq][pos] == let[j]) ++pos;
					}
				}
				b.push_back(r);
			}
		}
		random_shuffle(ALL(b));
		if (SZ(b) > BEAMSIZE) b.resize(BEAMSIZE);
		swap(a,b);
	}
	REP(qq,k)
	{
		int cnt = 0;
		REP(ii,SZ(a))
			if (a[ii].p[qq] == SZ(pref[qq]))
				++cnt;
		ans[qq] += cnt / (double)(SZ(a));
	}
}

vector<string> rec(int parent) {
	vector<vector<string>> ch;
	REP(i,n) if (par[i]==parent) {
		ch.push_back(rec(i));
	}
	VI pos;
	REP(j,SZ(ch))
		REP(cnt,SZ(ch[j][0]))
			pos.push_back(j);
	vector<string> r;
	string s(SZ(pos)+1,'.');
	if (parent!=-1) s[0]=let[parent];
	if (pos.empty()) {
		r.push_back(s);
		return r;
	}
	REP(iii,BEAMSIZE) {
		vector<string*> cand;
		REP(j,SZ(ch)) cand.push_back(&ch[j][rand() % SZ(ch[j])]);
		VI ind(SZ(ch),0);
		random_shuffle(ALL(pos));
		REP(j,SZ(pos))
		{
			s[j+1] = (*cand[pos[j]])[ind[pos[j]]++];
		}
		r.push_back(s);
	}
	return r;
}

void gobasic()
{
	vector<string> a = rec(-1);
	REP(qq,k)
	{
		int cnt = 0;
		REP(ii,SZ(a))
			if (KMPsearch(a[ii], string(cool[qq],cool[qq]+strlen(cool[qq]))))
				++cnt;
		ans[qq] += cnt / (double)(SZ(a));
	}
}

int main(int argc, char **argv)
{
	string FN = "b";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d:",test+shift);
		////////////////////////////////////////////////////////////
		scanf("%d",&n);
		REP(i,n) scanf("%d",&par[i]),--par[i];
		scanf("%s",let);
		scanf("%d",&k);
		REP(i,k)
		{
			scanf("%s",cool[i]);
			pref[i]=prefixFunc(string(cool[i],cool[i]+strlen(cool[i])));
		}
		CLEAR(ans);
		REP(i,ITERS)
		{
			gobasic();
			fprintf(stderr,".");
		}
		REP(i,k) ans[i] /= ITERS;
		REP(i,k)
			printf(" %.12lf",ans[i]);
		printf("\n");
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}