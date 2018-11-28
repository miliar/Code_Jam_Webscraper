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

const int maxn = 10010;
char s[maxn];

int main(){
#ifdef ONLINE_JUDGE
	if(prob == "t")
		prob = "";
#endif
	if(prob != ""){
		freopen((prob+".in").c_str(), "r", stdin);
		freopen((prob+".out").c_str(), "w", stdout);
	}
	int T;
	scanf("%d", &T);
	rep(_T, 1, T){
		printf("Case #%d: ",_T);
		int n;
		scanf("%d %s\n", &n, s);
		int cur = 0, ans = 0;
		rep(i, 0, n){
			int t = s[i] - '0';
			if(t){
				int d = max(0, i - cur);
				ans += d;
				cur += d;
			}
			cur += t;
		}
		printf("%d\n", ans);
	}
	return 0;
}
