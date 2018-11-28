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
int a[58];
int r,c;
string ma[58];
int px[58],py[58],pd[58],goal[58];
map<pint,int> de;
int dx[4]={-1,0,0,1},dy[4]={0,1,-1,0};
pint move(int x,int y,int d){
	x+=dx[d];y+=dy[d];
	while(x<r && y<c && x>=0 && y>=0){
		if(ma[x][y]=='/') d^=1;else d^=2;
		x+=dx[d];y+=dy[d];
	}
	return mp(x,y);
}
bool cal(void){
	//rep(i,(r+c)*2) a[i]--;
	//rep(i,4) cout<<a[i]<<endl;
	rep(i,c) px[i]=-1,py[i]=i,pd[i]=3,px[2*c+r-1-i]=r,py[2*c+r-1-i]=i,pd[2*c+r-1-i]=0;
	rep(i,r) px[c+i]=i,py[c+i]=c,pd[c+i]=2,px[2*c+2*r-1-i]=i,py[2*c+2*r-1-i]=-1,pd[2*c+2*r-1-i]=1;
	//rep(i,r*2+c*2) cout<<px[i]<<' '<<py[i]<<' '<<pd[i]<<endl;
	rep(i,r*2+c*2) de[mp(px[i],py[i])]=i;
	/*rep(i,4){
		pint p=move(px[i],py[i],pd[i]);
		cout<<p.fi<<' '<<p.se<<endl;
	}*/
	rep(i,r*2+c*2) goal[i]=de[move(px[i],py[i],pd[i])];
	rep(i,r+c){
		if(goal[a[2*i]]!=a[2*i+1]) return false;
	}
	return true;
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		int f=0;
		printf("Case #%d: \n",i+1);
		cin>>r>>c;
		rep(j,(r+c)*2){
			cin>>a[j];a[j]--;
		}
		rep(k,(1<<(r*c))){
			//if(k==0) continue;
			rep(l,r){
				ma[l]="";
				rep(m,c){
					if((k&(1<<(l*c+m)))) ma[l]+='/';else ma[l]+='\\';
				}
			}
			//rep(l,r) cout<<ma[l]<<endl;
			if(cal() && f<1){
				rep(l,r) cout<<ma[l]<<endl;
				f=1;
				break;
			}
		}
		if(f<1) cout<<"IMPOSSIBLE"<<endl;
	}
}
