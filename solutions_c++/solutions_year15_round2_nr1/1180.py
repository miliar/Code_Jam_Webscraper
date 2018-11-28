#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

ll rev(ll x){
	ll ret=0;
	while(x){
		ret=(ret*10)+(x%10);
		x/=10;
	}
	return ret;
}

int BFS(ll n){
	set<ll> st;
	queue<ll> q;
	q.push(1);
	st.insert(1);

	int level=1;
	while(!q.empty()){
		int sz=q.size();

		for(int i=0;i<sz;++i){
			ll x=q.front();
			q.pop();
			if(x==n)return level;

			ll y=rev(x);
			++x;
			if(x<=n && !st.count(x))q.push(x),st.insert(x);
			if(y<=n && y>x-1 && !st.count(y))q.push(y),st.insert(y);
		}
		++level;
	}
	return 0;
}


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);


	int t,cs=0;cin>>t;
	while(t--){
		ll n;cin>>n;
		cout<<"Case #"<<++cs<<": "<<BFS(n)<<"\n";
	}
	return 0;
}
