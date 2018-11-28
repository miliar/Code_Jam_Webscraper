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

const string IMPOSSIBLE="IMPOSSIBLE";

bool test(const vs& grid,int i,int j,int di,int dj)
{
	int h=grid.size(),w=grid[0].size();
	for(;;){
		i+=di,j+=dj;
		if(i<0 || h<=i || j<0 || w<=j) return false;
		if(grid[i][j]!='.') return true;
	}
}

void solve()
{
	int h,w; cin>>h>>w;
	vs grid(h);
	rep(i,h) cin>>grid[i];
	
	int res=0;
	rep(i,h) rep(j,w) if(grid[i][j]!='.'){
		int dir=string("^v<>").find(grid[i][j]);
		int tmp=INF;
		rep(k,4)
			if(test(grid,i,j,"\xff\x1\0\0"[k],"\0\0\xff\x1"[k]))
				tmp=min<int>(tmp,k!=dir);
		if(tmp==INF){
			res=INF;
			break;
		}
		res+=tmp;
	}
	if(res==INF)
		cout<<IMPOSSIBLE<<endl;
	else
		cout<<res<<endl;
}

int main()
{
	int tc; scanf("%d",&tc);
	rep(i,tc){
		printf("Case #%d: ",i+1);
		solve();
	}
}
