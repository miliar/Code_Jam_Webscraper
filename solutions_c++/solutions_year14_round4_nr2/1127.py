#include <map>
#include <set>
#include <queue>
#include <ctime>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(a) a.begin(),a.end()
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VII;

const double eps = 1e-8;
const double pi = acos(-1.0);

const int N = 1005;
int C[1005];
int sum(int x){
	int res = 0;
	for(;x;x-=x&-x){
		res += C[x];
	}
	return res;
}

void add(int x, int val){
	for(; x<N; x+=x&-x){
		C[x] +=val;
	}
}

vector<int> all;
int a[1005], c[1005];
int calc(int l, int r, int f){
	if(l>r) return 0;
	all.clear();
	int cnt = 0, res=0, i;
	for(i=l;i<=r;++i){
		c[++cnt] = a[i]*f;
		all.pb(c[cnt]);
	}
	sort(all.begin(), all.end());
	all.erase(unique(all.begin(), all.end()), all.end());
	int SZ = all.size();
	for(i=1;i<=cnt;++i){
		c[i] = lower_bound(all.begin(),all.end(), c[i])-all.begin()+1;
		res += sum(N-1)-sum(c[i]);
		add(c[i], 1);
	}
	for(i=1;i<=cnt;++i)
		add(c[i], -1);
	return res;
}

int b[N];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int tt, n, i, j;
	scanf("%d",&tt);
	for(int cal = 1; cal <= tt; ++cal){
		scanf("%d",&n);
		for(i=1;i<=n;++i) scanf("%d",&a[i]);
		int ans = 1000000;
		for(i=1;i<=n;++i){
			int tmp = calc(1, i, 1)+calc(i+1,n,-1);
			if(tmp < ans) ans = tmp;
		}
	//	printf("Case #%d: %d\n", cal, ans);
int ans1 = 1000000;
		for(i=1;i<=n;++i) b[i]=i;
		do{
			bool okay = false;
			for(i=1;i<=n;++i){
				for(j=1;j<=i;++j) if(a[b[j]]<a[b[j-1]]) break;
				if(j==i+1){
					for(j=i+1;j<=n;++j) if(a[b[j]]>a[b[j-1]]) break;
					if(j==n+1) okay = true;
				}
			}
			if(okay){
				int res = 0;
				for(j=1;j<=n;++j){
					res += sum(n)-sum(b[j]);
					add(b[j], 1);
				}
				for(j=1;j<=n;++j)
					add(b[j], -1);
				if(res < ans1)
				ans1 = res;
			}

		}while(next_permutation(b+1,b+n+1));
		printf("Case #%d: %d\n", cal, ans1);
		//if(ans1!=ans)printf("%d %d\n", ans1, ans);
		//else puts("-1");

	}
    return 0;
}

