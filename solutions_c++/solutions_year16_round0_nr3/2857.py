//Shubham Vijayvargiya

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

#define pb push_back
#define mp make_pair
#define eb emplace_back
#define F first
#define S second
#define sz(a) (int)(a.size())
#define set(a,b) memset(a,b,sizeof(a))
#define let(x,a) __typeof(a) x(a)
#define rep(i, begin, end) for (ll i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define all(v) (v).begin(),(v).end()
#define sll(x) { scanf("%lld",&x); }
#define si(x) { scanf("%d",&x); }
#define slf(x) { scanf("%lf",&x); }
#define pll(x) { printf("%lld\n",x); }
#define pi(x) { printf("%d\n",x); }
#define tcases() long long testcases; cin>>testcases ; while(testcases--)

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " = " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " = " << arg1<<" | ";__f(comma+1, args...);
}

#else
#define trace(...)
#endif

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
typedef long double ld;
typedef pair<long long,long long> pll;
typedef vector<long long> vll;
typedef vector<pll> vpll;
typedef vector<vll> vvll;

const ll mod=1000000007;
//-----------------------------------------------------------------------------------------------------------------------------------------------//

ll g[15],cnt=0;

void print(ll i){
	string s;
	while(i){
		s = s+ to_string(i%2);
		i/=2;
	}
	reverse(all(s));
	cout<<s<<" ";
	rep(j,2,11){
		cout<<g[j]<<" ";
	}
	cout<<endl;
	cnt++;
}


int main()
{
//	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	ll tc,n,k,l,tmp,fl;
	sll(tc);
	for(int tcc=1;tcc<=tc;tcc++){
		sll(n);sll(k);
		cout<<"Case #"<<tcc<<":"<<endl;
		for(ll i=1;i<(1<<n);i++){
			fl=0;
			set(g,-1);
			ll j=i;
			if(!(j&1)){
				continue;
			}
//			if(j==35)
//				trace("yyyy");
			if(!((j>>(n-1))&1)){
				continue;
			}
//			if(j==35)
//				trace("yyyy");
			for(int p=2;p<=10;p++){
				l=1;
				tmp=0;
				for(int u=0;u<16;u++){
					if(j&(1<<u)){
						tmp+=l;
					}
					l*=p;
				}
				for(int u=2;u*u<=tmp;u++){
					if(tmp%u==0){
						g[p]=u;
						break;
					}
				}
				if(g[p]==-1)
					break;
			}
			for(int p=2;p<=10;p++){
				if(g[p]==-1){
					fl=1;
				}
			}
			if(fl)
				continue;
			print(j);
			if(cnt==k)
				break;
		}
	}

	return 0;
}


