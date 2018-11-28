#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ld,ld> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

int main(){
	int T;
	cin >> T;
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		
		int n;
		ld v,x;
		ld r[102],c[102];
		scanf("%d%lf%lf",&n,&v,&x);
		rep(i,n){
			scanf("%lf%lf",&r[i],&c[i]);
		}
		
		ld vps = 0.0;
		ld sum_p = 0.0;
		ld sum_m = 0.0;
		vector<P> sou_p;
		vector<P> sou_m;
		rep(i,n){
			if(x == c[i]){
				vps += r[i];
			}
			else if(x < c[i]){
				sum_p += (c[i]-x)*r[i];
				sou_p.pb( P ( c[i]-x , r[i] ) );
			}
			else {
				sum_m += (x-c[i])*r[i];
				sou_m.pb( P ( x-c[i] , r[i] ) );
			}
		}
		if(sum_p == sum_m){
			rep(i,sou_p.size()){
				vps += sou_p[i].sc;
			}
			rep(i,sou_m.size()){
				vps += sou_m[i].sc;
			}
		}
		else{
			if(sum_p > sum_m){
				swap(sum_p,sum_m);
				swap(sou_p,sou_m);
			}
			rep(i,sou_p.size()){
				vps += sou_p[i].sc;
			}
			sor(sou_m);
			rep(i,sou_m.size()){
				if(sum_p <= sou_m[i].fr*sou_m[i].sc){
					vps += sum_p / sou_m[i].fr;
					break;
				}
				else {
					vps += sou_m[i].sc;
					sum_p -= sou_m[i].fr*sou_m[i].sc;
				}
			}
		}
		
		if(vps == 0.0)puts("IMPOSSIBLE");
		else printf("%.9lf\n",v/vps);
	}
}
			
