#include <bits/stdc++.h>

#define _overload(_1,_2,_3,name,...) name
#define _rep(i,n) _range(i,0,n)
#define _range(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload(__VA_ARGS__,_range,_rep,)(__VA_ARGS__)

#define _rrep(i,n) _rrange(i,n,0)
#define _rrange(i,a,b) for(int i=int(a)-1;i>=int(b);--i)
#define rrep(...) _overload(__VA_ARGS__,_rrange,_rrep,)(__VA_ARGS__)

#define _all(arg) begin(arg),end(arg)
#define uniq(arg) sort(_all(arg)),(arg).erase(unique(_all(arg)),end(arg))
#define getidx(ary,key) lower_bound(_all(ary),key)-begin(ary)
#define clr(a,b) memset((a),(b),sizeof(a))
#define bit(n) (1LL<<(n))
#define popcount(n) (__builtin_popcountll(n))

template<class T>bool chmax(T &a, const T &b) { return (a<b)?(a=b,1):0;}
template<class T>bool chmin(T &a, const T &b) { return (b<a)?(a=b,1):0;}

using namespace std;
using ll=long long;

int n,r,p,s;
string tmp="";

map<char,int> order[15];

void init(){
	order[0]['P']=0,order[0]['R']=1,order[0]['S']=2;
	rep(i,1,15){
		int p=min(3*order[i-1]['P']+order[i-1]['R'],3*order[i-1]['R']+order[i-1]['P']);
		int r=min(3*order[i-1]['R']+order[i-1]['S'],3*order[i-1]['S']+order[i-1]['R']);
		int s=min(3*order[i-1]['S']+order[i-1]['P'],3*order[i-1]['P']+order[i-1]['S']);
		vector<pair<int,char>> ary;
		ary.push_back(make_pair(p,'P'));
		ary.push_back(make_pair(r,'R'));
		ary.push_back(make_pair(s,'S'));
		sort(_all(ary));
		rep(j,3) order[i][ary[j].second]=j;
	}
	
	return;
}

void rec(char win,int d){
	if(d==0){
		tmp+=win;
		return;
	}

	switch(win){
		case 'P':
			if(order[d-1]['P']<order[d-1]['R']){
				rec('P',d-1);
				rec('R',d-1);
			}else{
				rec('R',d-1);
				rec('P',d-1);
			}
			break;
		case 'R':
			if(order[d-1]['R']<order[d-1]['S']){
				rec('R',d-1);
				rec('S',d-1);
			}else{
				rec('S',d-1);
				rec('R',d-1);
			}
			break;
		case 'S':
			if(order[d-1]['S']<order[d-1]['P']){
				rec('S',d-1);
				rec('P',d-1);
			}else{
				rec('P',d-1);
				rec('S',d-1);
			}
			break;	
	}	
}

int main(void){
	init();
	int T;
	cin >> T;
	rep(testcase,1,T+1){
		cin >> n >> r >> p >> s;

		string ans="IMPOSSIBLE";

		for(auto &win:"PRS"){
			tmp="";
			rec(win,n);
			int cr=0,cp=0,cs=0;
			for(auto &c:tmp){
				if(c=='R') cr++;
				if(c=='P') cp++;
				if(c=='S') cs++;
			}
			if(cr==r && cp == p && cs == s){
				if(ans=="IMPOSSIBLE")
					ans=tmp;
				else
					chmin(ans,tmp);	
			}
		}
		cout << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}