#include <bits/stdc++.h>
using namespace std;

#define dump(n) cout<<"# "<<#n<<'='<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

const int INF=1e9;
const int MOD=1e9+7;
const double EPS=1e-9;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}
template<typename T>
ostream& operator<<(ostream& os,const vector<T>& a){
	os<<'[';
	rep(i,a.size()) os<<(i?" ":"")<<a[i];
	return os<<']';
}

struct FenwickTree{
	vector<ll> data;
	FenwickTree(int n):data(n+1){}
	void Add(int i,int x){
		for(i++;i<data.size();i+=i&-i)
			data[i]+=x;
	}
	ll Sum(int i){
		ll res=0;
		for(;i;i-=i&-i)
			res+=data[i];
		return res;
	}
	ll Sum(int i,int j){
		return Sum(j)-Sum(i);
	}
};

bool ok(const vi& a)
{
	int i=1;
	for(;i<a.size() && a[i-1]<a[i];i++);
	for(;i<a.size() && a[i-1]>a[i];i++);
	return i==a.size();
}

int swapcount(const vi& p)
{
	int n=p.size();
	FenwickTree ft(n);
	int res=0;
	rep(i,n){
		res+=i-ft.Sum(p[i]);
		ft.Add(p[i],1);
	}
	return res;
}

void solve_naive()
{
	int n; cin>>n;
	vi a(n);
	rep(i,n) cin>>a[i];
	vi p(n); iota(all(p),0);
	int res=INF;
	do{
		vi b(n);
		rep(i,n) b[i]=a[p[i]];
		if(ok(b)){
			if(swapcount(p)==6)
				dump(p);
			res=min(res,swapcount(p));
		}
	}while(next_permutation(all(p)));
	cout<<res<<endl;
}

int calc(const vi& a,int p)
{
	int n=a.size();
	int cnt=0;
	
	vi is(p);
	iota(all(is),0);
	sort(all(is),[&](int i,int j){return a[i]<a[j];});
	cnt+=swapcount(is);
	
	is.resize(n-(p+1));
	iota(all(is),0);
	sort(all(is),[&](int i,int j){return a[p+1+i]>a[p+1+j];});
	cnt+=swapcount(is);
	
	return cnt;
}

void solve()
{
	//solve_naive(); return;
	int n; cin>>n;
	vi a(n);
	rep(i,n) cin>>a[i];
	
	vi is(n); iota(all(is),0);
	sort(all(is),[&](int i,int j){return a[i]<a[j];});
	rep(i,n) a[is[i]]=i;
	
	int res=0;
	for(int i=0,l=0,r=n-1;i<n;i++){
		int j=find(all(a),i)-begin(a);
		if(j-l<=r-j){
			rotate(begin(a)+l,begin(a)+j,begin(a)+j+1);
			res+=j-l;
			l++;
		}
		else{
			rotate(begin(a)+j,begin(a)+j+1,begin(a)+r+1);
			res+=r-j;
			r--;
		}
	}
	cout<<res<<endl;
}

int main()
{
	int T; scanf("%d",&T);
	rep(i,T){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
