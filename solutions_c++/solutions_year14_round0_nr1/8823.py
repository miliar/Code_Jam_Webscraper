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
#define FOR(t,l,r) for (int t=l; t<(int)r; t++)
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

int a[4][4], b[4][4];

int main () {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		int x; cin >>x; --x;
		FOR(i,0,4) FOR(j,0,4) cin >>a[i][j];
		int y; cin >>y; --y;
		FOR(i,0,4) FOR(j,0,4) cin >>b[i][j];
		set<int> s1; FOR(i,0,4) s1.insert(a[x][i]);
		set<int> s2; FOR(i,0,4) s2.insert(b[y][i]);
		set<int> s3;
		for (set<int>::iterator it=s1.begin(); it!=s1.end(); it++)
			if (s2.find(*it)!=s2.end()) s3.insert(*it);
		if (s3.empty()) cout <<"Case #"<<tt<<": Volunteer cheated!\n";
		else if ((int)s3.sz>1) cout <<"Case #"<<tt<<": Bad magician!\n";
		else cout <<"Case #"<<tt<<": "<<*s3.begin()<<endl;
	}
return 0;
}








