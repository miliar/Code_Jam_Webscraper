// By An-Li Alt Ting. Default code 2014-05-06.
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
bool f(LL x){
	while(1<x){
		if(x%2==1)
			return 1;
		x/=2;
	}
	return 0;
}
int main(int argc,char*argv[]){
	freopen("i.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	//ios_base::sync_with_stdio(0);
	int t;cin>>t;
	F(t){
		long long p,q;
		scanf("%lli/%lli",&p,&q);
		printf("Case #%i: ",i+1);
		int d=__gcd(p,q);
		p/=d;
		q/=d;
		bool ans=0;
		if(f(q)==0){
			int a=log2(p);
			int b=log2(q);
			printf("%i\n",b-a);
		}else
			puts("impossible");
	}
	return EXIT_SUCCESS;
}
