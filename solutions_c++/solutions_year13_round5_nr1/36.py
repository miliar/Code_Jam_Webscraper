#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

struct timer{
	time_t start;
	timer(){start=clock();}
	~timer(){cerr<<1.*(clock()-start)/CLOCKS_PER_SEC<<" secs"<<endl;}
};

typedef istringstream iss;
typedef long long ll;
typedef pair<int,int> pi;
typedef stringstream sst;
typedef vector<int> vi;

ll B,N,X[40];

void main2(){
	cin>>B>>N;
	rep(i,N)cin>>X[i];
	rep2(i,N,37)X[i]=0;
	sort(X,X+37);
	X[37]=INF*INF;
	double ans=0;
	rep2(pos,1,37){
		if(X[pos-1] == X[pos])continue;
		ll fil=0;
		rep(i,pos)fil += X[pos-1] - X[i];
		if(B < fil)continue;
		ll b=B-fil;
		ll tip = b / pos;
		ll total = min(X[pos-1]+tip,X[pos]-1) * pos;
		rep(i,pos)total -= X[i];
		//cout<<pos<<": "<<fil<<" "<<b<<" "<<tip<<" "<<total<<" "<<total*36./pos-total<<endl;
		ans=max(ans,total*36./pos-total);
		
		rep2(hit,1,pos){
			ll rest = b - (pos-hit);
			if(rest<0)continue;
			ll tip2 = rest / pos;
			ll bet = min(X[pos-1]+tip2,X[pos]-1);
			ll spend = bet * pos + (pos-hit);
			rep(i,pos)spend -= X[i];
			ll total2 = bet * hit;
			rep(i,hit)total2 -= X[i];
			//cout<<pos<<" "<<hit<<": "<<bet<<" "<<spend<<" "<<total2<<" "<<total2*36./hit-spend<<endl;
			ans=max(ans,total2*36./hit-spend);
		}
	}
	
	cout<<setprecision(16)<<ans<<endl;
}

int main(){
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
