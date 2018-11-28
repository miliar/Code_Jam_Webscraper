# include <bits/stdc++.h>

# define ff first
# define ss second
# define mp(x,y) make_pair(x,y)
# define tr(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
# define MAXN 1001

template<typename A, typename B> inline void amax(A &x, B y) {if(x < y) x = y;}
template<typename A, typename B> inline void amin(A &x, B y) {if(!(x < y)) x = y;}

typedef long long lld;

using namespace std;

int n, t;
int A[MAXN];

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	scanf("%d",&t);
	
	int ans;
	int cnt;
	
	for(int u=0; u<t; u++){
		int ans = MAXN;
		
		scanf("%d",&n);
		
		for(int i=0; i<n; i++)
			scanf("%d",A+i);
		
		for(int i=1; i<MAXN; i++){
			cnt = 0;
			
			for(int j=0; j<n; j++)
				cnt += (A[j] / i + (A[j] / i * i != A[j])) - 1;
			
			amin(ans, cnt+i);
		}
		
		printf("Case #%d: %d\n",u+1,ans);
	}
}
