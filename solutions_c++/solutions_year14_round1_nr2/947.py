// By An-Li Alt Ting. Default code 2014-03-28.
#include<stdint.h>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<bitset>
#include<deque>
#include<functional>
#include<iomanip>
#include<iostream>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<utility>
#include<valarray>
#include<vector>
//#include<bits/extc++.h>
//#include<bits/stdc++.h>
//#include<ext/algorithm>
//#include<ext/numeric>
//#include<ext/rope>
//#include<ext/slist>
//#include<ext/pb_ds/assoc_container.hpp>
//#include<ext/pb_ds/priority_queue.hpp>
//#include<ext/pb_ds/tree_policy.hpp>
using namespace std;
//using namespace __gnu_cxx;
//using namespace __gnu_pbds;
typedef long long	LL;	// long long
typedef double		LF;	// long float
typedef map<int,int>	MI;	// map int
typedef pair<int,int>	PI;	// pair int
typedef queue<int>	QI;	// queue int
typedef set<int>	SI;	// set int
typedef vector<int>	VI;	// vector int
//typedef tree<int,char,less<int>,rb_tree_tag,tree_order_statistics_node_update>TI;
//typedef tree<PI,char,less<PI>,rb_tree_tag,tree_order_statistics_node_update>TPI;
//typedef tree<int,int,less<int>,rb_tree_tag,tree_order_statistics_node_update>TII;
//typedef tree<PI,int,less<int>,rb_tree_tag,tree_order_statistics_node_update>TPII;
#define x first
#define y second
#define pb push_back
#define it iterator
#define F(n) FO(i,n)				// for i in [0,$n)
#define FO(i,n) FI(i,0,n)			// for $i in [0,$n)
#define FI(i,f,l) for(int i=(f),ei=(l);i<ei;i++)
#define FD(i,f,l) for(int i=(f),ei=(l);i>ei;i--)
#define FA(a) for(__typeof((a).begin())it=(a).begin(),ea=(a).end();\
		it!=ea;++it)		// for *it in a
/*inline LL GI(){    // getchar input integer
	char s,d;
	while(s=getchar(),s==' '||s=='\n');
	LL x=s=='-'?0:s-'0';
	while(d=getchar(),'0'<=d&&d<='9')x=x*10+d-'0';
	return s=='-'?-x:x;
}*/
/*struct sv{	// union-find tree
	sv*p;
	sv():p(this){}
	sv*r(){return p==this?p:(p=p->r());}
	sv&operator=(sv&v){return*(r()->p=v.r());}
	bool operator==(sv&v){return r()==v.r();}
};*/
const int mv=1e3;int cv;
VI G[mv];
bool vs[mv];
int vsz[mv];
int sz(int v,int p=-1){
	vsz[v]=1;
	VI a;
	FA(G[v]){int w=*it;
		if(w!=p){
			a.pb(sz(w,v));
		}
	}
	sort(a.begin(),a.end(),greater<int>());
	if(2<=a.size())
		vsz[v]+=a[0]+a[1];
	return vsz[v];
}
int main(int argc,char*argv[]){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	//ios_base::sync_with_stdio(0);
	int t;cin>>t;
	F(t){
		cin>>cv;
		F(cv)G[i].clear();
		F(cv-1){
			int v,w;cin>>v>>w;v--,w--;
			G[v].pb(w);
			G[w].pb(v);
		}
		int ans=INT_MAX;
		F(cv){
			memset(vs,0,sizeof vs);
			ans=min(ans,cv-sz(i));
		}
		printf("Case #%i: %i\n",i+1,ans);
	}
	return EXIT_SUCCESS;
}
