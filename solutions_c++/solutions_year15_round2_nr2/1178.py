#include <bits/stdc++.h>
#define forall(i,a,b)               for(int i=a;i<=b;i++)
#define pb                          push_back
#define mp			  			    make_pair
#define MOD                         1000000007

#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map <string, int> msi;

int cnt[1 << 18];
int R, C, N;
 
int foo(int i)
{
	int ans = 0;
	forall(r,0,R-1)
	{
		forall(c,0,C-1)
		{
			if (c > 0 && (i & (1 << (r * C + c))) && (i & (1 << (r * C + c - 1))))
				ans++;
			if (r > 0 && (i & (1 << (r * C + c))) && (i & (1 << (r * C + c - C))))
				ans++;
		}
	}
	return ans;
}

int main()
{
	 #ifndef ONLINE_JUDGE
     	freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
     #endif
     //ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	forall(kase,1,t)
	{
		
		cin>>R>>C>>N;
		int ans = R * C * N * 100;
		for (int i = 1; i < (1 << (R * C)); i++)
		{
			cnt[i] = cnt[i - (i & -i)] + 1;

			if (cnt[i] == N) 
				ans= min(ans, foo(i));
		}
		printf("Case #%d: %d\n", kase, ans);
		

	}
	return 0;
}
