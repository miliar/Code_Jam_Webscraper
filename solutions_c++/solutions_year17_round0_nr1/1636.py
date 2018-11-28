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
#define N 2009
ll bit[N];

void update(ll x,ll v){
	x+=1;
	while(x<N){
		bit[x]+=v;
		x+=x&(-x);
	}
	return ;
}

ll get(ll x){
	if(x<0)
		return 0;
	x++;
	ll ans=0;
	while(x>0){
		ans+=bit[x];
		x-=x&(-x);
	}
	return ans;
}

int main()
{
//	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	ll ttt;
	sll(ttt);
	for(int tc=1;tc<=ttt;tc++){
		printf("Case #%d: ",tc);
		set(bit,0);
		string s;
		ll k;
		cin>>s;
		cin>>k;
		ll n=sz(s);
		rep(i,0,n){
			ll tmp=get(i)-get(i-k);
			if(tmp%2==1){
				if(s[i]=='-')
					s[i]='+';
				else
					s[i]='-';
			}
			if(i<=n-k){
				if(s[i]=='-'){
					s[i]='+';
					update(i,1);
				}
			}
		}
		bool fl=false;
		rep(i,0,n){
			if(s[i]=='-')
				fl=true;
		}
		if(fl)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<get(n)<<endl;
	}
	return 0;
}


