#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define rep(i,st,ed) for (int i=st; i<ed; i++)
#define foreach(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)

const int MAXN=100001;
const int INF=0x3f3f3f3f;
const double eps=1e-8;

struct data{
	int x,y;
	data(){}
	data(int x, int y):x(x),y(y){}
};

bool cmp(const data &a, const data &b){
	return a.x<b.x;
}

int n,m;
long long result;
vector<long long> v;
vector<data> in,out;

long long calc(long long x, long long y, long long total){
	return 1LL*(n+n-(y-x)+1)*(y-x)/2*total;
}

void init(){
	int x,y,p;
	result=0;
	cin>>n>>m;
	v.clear(); in.clear(); out.clear();
	rep(i,0,m){
		cin>>x>>y>>p;
		in.push_back(data(x,p));
		out.push_back(data(y,p));
		v.push_back(x); v.push_back(y);
		result+=calc(x,y,p);
	}
	sort(v.begin(),v.end());
	v.erase(unique(v.begin(),v.end()),v.end());
	sort(in.begin(),in.end(),cmp);
	sort(out.begin(),out.end(),cmp);
}

long long solve(){
	long long ret=0;
	stack<data> stk;
	int x=0,y=0;
	rep(i,0,v.size()){
		while (x<in.size() && in[x].x==v[i]){
			stk.push(in[x]);
			++x;
		}
		while (y<out.size() && out[y].x==v[i]){
			while (!stk.empty() && out[y].y>0){
				data temp=stk.top(); stk.pop();
				if (temp.y<=out[y].y){
					ret+=calc(temp.x,out[y].x,temp.y);
					out[y].y-=temp.y;
				} else{
					ret+=calc(temp.x,out[y].x,out[y].y);
					temp.y-=out[y].y;
					out[y].y=0;
					stk.push(temp);
				}
			}
			if (out[y].y==0) ++y;
		}
	}
	return result-ret;
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int ca;
	cin>>ca;
	rep(i,0,ca){
		init();
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
	return 0;
}

