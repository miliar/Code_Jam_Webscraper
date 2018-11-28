#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define mp make_pair
#define X first
#define Y second

#define pb push_back
#define forI_(i,V,_) for(__typeof(V.end())i=_;i!=V.end();++i)
#define forI(i,V) forI_(i,V,V.begin())

#define rep(i,l,r) for(int i = l; i <= r; ++i)
#define per(i,r,l) for(int i = r; i >= l; --i)
#define rep_(i,l,r) for(int i = l; i < r; ++i)
#define per_(i,r,l) for(int i = r; i > l; --i)

string prob = "t";

const int maxn = 1010;
int a[maxn];

int main(){
#ifdef ONLINE_JUDGE
	if(prob == "t")
		prob = "";
#endif
	if(prob != ""){
		freopen((prob+".in").c_str(), "r", stdin);
		freopen((prob+".out").c_str(), "w", stdout);
	}
	int Test;
	scanf("%d", &Test);
	rep(Testi, 1, Test){
		printf("Case #%d: ", Testi);
		int n, m = 0;
		scanf("%d", &n);
		rep(i, 1, n){
			scanf("%d", a + i);
			m = max(m, a[i]);
		}
		int ans = m;
		rep(i, 1, m){
			int s = 0;
			rep(j, 1, n)
				s += (a[j] - 1)/ i;
			ans = min(ans, s + i);
		}
		printf("%d\n", ans);
	}
	return 0;
}
