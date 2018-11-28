#include <bits/stdc++.h>
using namespace std;

#define dump(...) cout<<"# "<<#__VA_ARGS__<<'='<<(__VA_ARGS__)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

using uint=unsigned int;
using ll=long long;
using ull=unsigned long long;
using pii=pair<int,int>;
using vi=vector<int>;
using vvi=vector<vi>;
using vl=vector<ll>;
using vvl=vector<vl>;
using vd=vector<double>;
using vvd=vector<vd>;
using vs=vector<string>;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}

template<typename Tuple>
void print_tuple(ostream&,const Tuple&){}
template<typename Car,typename... Cdr,typename Tuple>
void print_tuple(ostream& os,const Tuple& t){
	print_tuple<Cdr...>(os,t);
	os<<(sizeof...(Cdr)?",":"")<<get<sizeof...(Cdr)>(t);
}
template<typename... Args>
ostream& operator<<(ostream& os,const tuple<Args...>& t){
	print_tuple<Args...>(os<<'(',t);
	return os<<')';
}

template<typename Ch,typename Tr,typename C>
basic_ostream<Ch,Tr>& operator<<(basic_ostream<Ch,Tr>& os,const C& c){
	os<<'[';
	for(auto i=begin(c);i!=end(c);++i)
		os<<(i==begin(c)?"":" ")<<*i;
	return os<<']';
}

constexpr int INF=1e9;
constexpr int MOD=1e9+7;
constexpr double EPS=1e-9;

void solve_small()
{
	int n; cin>>n; cin.ignore();
	vs ss(n);
	rep(i,n) getline(cin,ss[i]);
	
	map<string,int> f;
	vvi a(n);
	rep(i,n){
		istringstream iss(ss[i]);
		for(string s;iss>>s;){
			f.emplace(s,f.size());
			a[i].push_back(f[s]);
		}
	}
	
	vi fs(f.size());
	rep(i,a[0].size()) fs[a[0][i]]|=1;
	rep(i,a[1].size()) fs[a[1][i]]|=2;
	
	int res=INF;
	rep(_,1<<n-2){
		int b=_<<2;
		vi gs=fs;
		repi(i,2,n) rep(j,a[i].size())
			gs[a[i][j]]|=1<<(b>>i&1);
		res=min<int>(res,count(all(gs),3));
	}
	cout<<res<<endl;
}

int main()
{
	int tc; scanf("%d",&tc);
	rep(i,tc){
		printf("Case #%d: ",i+1);
		solve_small();
		//solve();
	}
}
