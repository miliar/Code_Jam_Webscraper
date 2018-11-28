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

bool equal(double a,double b)
{
	return abs(a-b)<EPS;
}

void solve_small()
{
	int n; double v,x; cin>>n>>v>>x;
	vd rs(n),cs(n);
	rep(i,n) cin>>rs[i]>>cs[i];
	//cout<<endl; dump(rs); dump(cs);
	
	if(n>2){
		cout<<"give up"<<endl;
		return;
	}
	
	if(n==1){
		if(equal(cs[0],x))
			printf("%.9f\n",v/rs[0]);
		else
			cout<<IMPOSSIBLE<<endl;
	}
	
	if(n==2){
		if(cs[0]>cs[1]){
			swap(cs[0],cs[1]);
			swap(rs[0],rs[1]);
		}
		
		if(x<cs[0]-EPS || cs[1]+EPS<x){
			cout<<IMPOSSIBLE<<endl;
			return;
		}
		
		double r=0;
		if(equal(cs[0],x)) r+=rs[0];
		if(equal(cs[1],x)) r+=rs[1];
		if(r>0){
			printf("%.9f\n",v/r);
			return;
		}
		
		double v0=(cs[1]-x)/(cs[1]-cs[0])*v;
		double v1=v-v0;
		double t0=v0/rs[0],t1=v1/rs[1];
		printf("%.9f\n",max(t0,t1));
	}
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
