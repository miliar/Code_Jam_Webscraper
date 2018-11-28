#include<bits/stdc++.h>
using namespace std;
#define max(a,b) ((a)>(b))?(a):(b)
#define min(a,b) ((a)<(b))?(a):(b)
#define sync ios_base::sync_with_stdio(0);cin.tie(0)
#define rep(i,a,b) for(int i = int(a); i <= int(b); i++ )
#define all(a) a.begin(), a.end()
#define pb push_back
#define fill(a,v) memset(a, v, sizeof a)
#define sz(a) ((int)(a.size()))
#define mp make_pair
#define range(x,a,b) (x>=a && x<=b)
#define INF (int)1e9
#define EPS 1e-9
#define bitcount __builtin_popcount
#define gcd __gcd 
#define checkbit(n,b) ( (n >> b) & 1)
#define UNIQUE(a) sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())

template<typename T> inline const T abs(T const& x)
{
	return (x<0) ? -x : x;
}
int main()
{
	sync;
	#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	freopen("out_err", "w", stderr);
	#else
	// online submission
	#endif
	int t;
	cin >> t;
	rep(I,1,t)
	{
		cerr<<I<<endl;
		int res=0;
		string s;
		cin>>s;
		rep(x,0,s.length()-1)
			if(s[x]=='-')s[x]='0';
			else s[x] = '1';
		reverse(all(s));
		cerr<<I<<' '<<s<<'\n';
		bitset<101> tt(s);
		int len =s.length();
		while(tt.count()<len)
		{
			res++;
			if(tt.test(0))
			{
				int t=0;
				while(tt.test(t)&& t<len){tt.flip(t);t++;}
			}
			else
			{
				int t=0;
				while(!tt.test(t)&& t<len){tt.flip(t);t++;}
			}			
		}	
		cout<<"Case #"<<I<<": "<<res<<'\n';
	}
	return 0;
}


