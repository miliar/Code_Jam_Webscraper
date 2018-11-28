#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <list>
#include <queue>
using namespace std;

#define LL long long
#define V vector
#define VD V<double>
#define VI V<int>
#define VII V<VI>
#define FOR(t,l,r) for (LL t=l; t<(int)r; t++)
#define FORL(t,l,r) for (LL t=l; t<(LL)r; t++)
#define max(x,y) ((x>y)?x:y)
#define min(x,y) ((x<y)?x:y)
#define abs(x) (((x)<0)?-(x):(x))
const double mth_pi=2*acos(0.);
#define pi mth_pi
#define inf (1<<23)
#define eps 1e-10
#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) a.begin(),a.end()
#define mii map<int,int>
#define pii pair<int,int>
#define x first
#define y second

bool isVow (char x) {
	if (x=='a') return 1;
	if (x=='e') return 1;
	if (x=='i') return 1;
	if (x=='o') return 1;
	if (x=='u') return 1;
return 0;
}

bool ch (string s, int n) {
	int l=s.sz, cur=0;
	FOR(t,0,n) cur+=(isVow(s[t]));
	if (cur==0) return 1;
	FOR(t,n,l) {
		cur+=(isVow(s[t]));
		cur-=(isVow(s[t-n]));
		if (cur==0) return 1;
	}
return 0;
}

int main () {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	LL T; cin >>T;
	FOR(tt,1,T+1) {
		int ans=0;
		string s; int n; cin >>s>>n;
		int l=s.sz;
		FOR(t,0,l) FOR(i,n,l-t+1) {
			string p=string(s,t,i);
			if (ch(p,n)) ans++;
		}
		cout <<"Case #"<<tt<<": "<<ans<<endl;
	}
return 0;
}
