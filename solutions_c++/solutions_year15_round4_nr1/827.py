#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
string ma[114];
int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};
int de(char c){
	if(c=='^') return 0;
	if(c=='v') return 1;
	if(c=='<') return 2;
	if(c=='>') return 3;
	return -1;
}
int cal(void){
	int ret=0,h,w;
	cin>>h>>w;
	rep(i,h) cin>>ma[i];
	rep(i,h) rep(j,w){
		int t=de(ma[i][j]),mask=0;
		if(t<0) continue;
		rep(k,4){
			int f=0;
			for(int l=1;;l++){
				int x=i+l*dx[k],y=j+l*dy[k];
				if(x<0 || y<0 || x>=h || y>=w) break;
				if(ma[x][y]!='.'){f=1;break;}
			}
			mask+=(f<<k);
		}
		if(mask<=0) return -1;
		if(!(mask&(1<<t))) ret++;
	}
	return ret;
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		cerr<<i<<endl;
		int ret=cal();
		if(ret<0) printf("Case #%d: IMPOSSIBLE\n",i+1);
		else printf("Case #%d: %d\n",i+1,ret);
	}
}
