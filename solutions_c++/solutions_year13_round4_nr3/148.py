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

int n;
int Cas;

int a[2010];
int b[2010];
int x[2010];
bool used[2010];

bool saiki(int t){
	if(t==n){
		for(int i=n-1; i>=0; --i){
			int fuga = 1;
			repp(j,i+1,n-1){
				if(x[i] > x[j]) fuga = max(fuga,b[j]+1);
			}
			if(b[i] != fuga) return false;
		}
		printf("Case #%d: ", Cas+1);
		rep(i,n-1) cout << x[i]+1 << " ";
		cout << x[n-1]+1 << endl;
		return true;
	}
	rep(i,n)if(!used[i]){
		int hoge = 1;
		rep(j,t){
			if(x[j] < i) hoge = max(hoge,a[j]+1);
		}
		if(a[t] == hoge){
			x[t] = i;
			used[i] = 1;
			if(saiki(t+1)) return true;
			used[i] = 0;
		}
	}
	return false;
}

int main(){
	int casenum; cin >> casenum;
	rep(cas, casenum){
		Cas = cas;
		cin >> n;
		rep(i,2010) used[i] = 0;
		rep(i,n) cin >> a[i];
		rep(i,n) cin >> b[i];
		saiki(0);
//		printf("Case #%d: %d\n", cas+1, solve());
	}
	return 0;
}

