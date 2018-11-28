#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<cstdlib>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;

#define mp make_pair
#define pb push_back

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

void output(int cas, char *s){
	printf("Case #%d: %s\n", cas+1, s);
}
int n, m;
int a[110][110];

int main(){
	int casenum; cin >> casenum;
	rep(casee, casenum){
		int mi[110], mj[110];
		rep(i, 110) mi[i] = mj[i] = -1;
		cin >> n >> m;
		rep(i, n) rep(j, m) cin >> a[i][j];
		rep(i, n) rep(j, m) mi[i] = max(mi[i], a[i][j]),
			mj[j] = max(mj[j], a[i][j]);
		rep(i, n) rep(j, m) if(a[i][j] != min(mi[i], mj[j])){
			output(casee, "NO");
			goto tugi;
		}
		output(casee, "YES");
tugi:;
	}
	return 0;
}

