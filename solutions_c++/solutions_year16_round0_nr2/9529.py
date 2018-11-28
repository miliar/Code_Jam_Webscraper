#define _CRT_SECURE_NO_WARNINGS

#include <bits/stdc++.h>
using namespace std;

typedef long long           ll;
typedef unsigned long long  ull;
typedef pair<int,int>       ii;
typedef pair<ll,ll>         pll;
typedef pair<double,double> dd;

typedef vector<int>         vi;
typedef vector<ll>          vll;
typedef vector<ii>          vii;
typedef vector<pll>         vpll;
typedef vector<string>      vs;

#define umap            unordered_map
#define uset            unordered_set

#define OO              1e18
#define oo              1e9
#define EPS             1e-12

#define Read            freopen("in.txt", "r", stdin)
#define Write           freopen("out.txt", "w", stdout)

#define clr(a)          memset(a,0,sizeof a)
#define clr_dp(a)       memset(a,-1,sizeof a)
#define all(v)          v.begin(),v.end()
#define sz(v)           (int) v.size()
#define rev(v)			reverse(all(v))
#define in(v,tar)		(v.find(tar) != v.end())

#define pb              push_back
#define fi              first
#define se              second 
#define mp              make_pair
#define mt				make_tuple
#define elm(t,indx)		get<indx>(t)

#define lop(i,n)        for(int i=0;i<n;++i)
#define loplr(i,l,r)    for(int i=l;i<=r;++i)
#define	lopv(i,n,v)		for(int i=0;i<n;i+=v)
#define lop_1(i,n)		for(int i=1;i<n;++i)

#define sc	            scanf
#define pf				printf
#define pfn				printf("\n")

#define TEST			cout<<"HERE\n"

#define r_arr(a,n)		lop(i,n) cin>>a[i]
#define r_grid(a,n,m)	lop(i,n) lop(j,m) cin>>a[i][j]

#define cnt_ones(x) 	__builtin_popcount(x)
#define sq(a)			(a*a)

#define debug(args...)  {dbg,args; cerr << endl;}
struct debugger{
    template<typename T> debugger& operator , (const T& v){    
        cerr<<v<<" ";    
        return *this;    
    }
} dbg;

ll gcd(ll a, ll b){ return((b == 0)?a:gcd(b,a%b));  }
ll lcm(ll a, ll b){ return (a*b)/gcd(a,b); }

/**********************************************************/



int main(){
#ifndef ONLINE_JUDGE
	Read;
	Write;
#endif
	
	int t,c =1;
	cin >> t;
	string s;
	
	while(t--){
		cin>>s;
		
		int i = 0, cnt = 0;
		while(i<sz(s)){
			if(s[i] == '-'){
				int j = i;
				while(j<sz(s) && s[j] == '-')
					++j;
				cnt += ((i == 0)?1:2);
				i = j;
			}else 
				++i;		
		}	
		
		cout << "Case #" << c++ << ": " << cnt << endl;
	}
	
	return 0;
}


