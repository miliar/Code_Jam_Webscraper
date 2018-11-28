#include<bits/stdc++.h>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define LL long long
#define F first
#define S second
 
#define fo(i, n) for(int i = 0; i < n; ++i)
#define whatis(X) cout << #X << " is " << X << endl;
 
const int N = 16;
const int inf = INT_MAX;
const int mod = (int)(1e9 + 7);
int used[11];
 
inline int add(LL x)
{
	int cnt=0;
	if(x==0)
	{
		cnt+=used[x]==0;
		used[x]=1;
	}
	else
	{
		while(x)
		{
			cnt+=used[x%10]==0;
			used[x%10]=1;
			x/=10;
		}
	}
	return cnt;
}

inline void solve(int test)
{
	int a;scanf("%d",&a);
	memset(used,0,sizeof used);
	LL all=10,fail=0,b=a,r=0;
	if(a==0)fail=1;
	for(;!fail;b+=a,r++)
	{
		int x=add(b);
		all-=x;
		if(all==0) break;
	}
	printf("Case #%d: ", test);
	if(fail) printf("INSOMNIA\n");
	else printf("%d\n", b);
}

int main() {
	#ifdef LOCAL
		freopen(".in", "r", stdin);
		freopen("a.out", "w", stdout);
	#endif
	int t;
	scanf("%d",&t);
	fo(i,t)
		solve(i+1);
	return 0;
}