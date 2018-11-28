#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;


#define INF 1e+10
#define EPS 1e-10
#define EQ(a,b) (abs(a-b)<EPS)

//誤差を考慮して足し算
long long add(long long a,long long b){
	return a+b;
}
struct P{//2次元ベクトル
	long long x,y;
	P(){}
	P(long long x,long long y):x(x),y(y){}
	P operator + (P p){
		return P(add(x,p.x),add(y,p.y));
	}
	P operator - (P p){
		return P(add(x,-p.x),add(y,-p.y));
	}
	/*P operator * (double d){
		return P(x*d,y*d);
	}
	P operator / (double d){
		return P(x/d,y/d);
	}*/
	long long dot(P p){//内積
		return add(x*p.x,y*p.y);
	}
	long long det(P p){//外積
		return add(x*p.y,-y*p.x);
	}
	bool equal(P p)const{
		return x==p.x&&y==p.y;
	}
	bool operator == (P p)const{
		return equal(p);
	}
	/*double norm()const{
		return sqrt(x*x+y*y);
	}*/
};
//凸包
bool cmp_x(const P& p,const P& q){
	if(p.x!=q.x)return p.x<q.x;
	return p.y<q.y;
}
vector<P> convex_hull(vector<P>& ps){
	if(ps.empty())return ps;
	sort(ps.begin(),ps.end(),cmp_x);
	int k=0;
	vector<P> qs(ps.size()*2);
	for(int i=0;i<ps.size();i++){
		while(k>1 && (qs[k-1]-qs[k-2]).det(ps[i]-qs[k-1]) < 0 )k--;
		qs[k++]=ps[i];
	}
	for(int i=ps.size()-2,t=k;i>=0;i--){
		while(k>t && (qs[k-1]-qs[k-2]).det(ps[i]-qs[k-1]) < 0 )k--;
		qs[k++]=ps[i];
	}
	qs.resize(k-1);
	return qs;
}



int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	rep(testcase,t){
		int n;
		P p[15];
		cin>>n;
		rep(i,n)cin>>p[i].x>>p[i].y;

		cout<<"Case #"<<testcase+1<<":\n";
		rep(i,n){
			int ans=n-1;
			rep(j,1<<n)if(j>>i&1){
				vector<P> pv;
				rep(k,n)if((j>>k&1)==0)pv.push_back(p[k]);
				vector<P> conv1(convex_hull(pv));
				pv.push_back(p[i]);
				vector<P> conv2(convex_hull(pv));

				if(conv1!=conv2){
					ans=min(ans,n-(int)pv.size());
				}
			}
			cout<<ans<<endl;
		}
	}
	return 0;
}