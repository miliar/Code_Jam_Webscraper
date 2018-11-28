/* attention to overflow */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <queue>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <numeric>
#include <tuple>
#include <iomanip>

#define dump(x) cerr<< #x << " = " << x <<endl
#define ALL(container) (container).begin(),(container).end()

using namespace std;
const int INF = 1 << 25;
void io() { cin.tie(0); ios::sync_with_stdio(false);}
template <class S,class T> ostream& operator<<(ostream& os, const pair <S,T> &s){return os<<'('<<s.first<<','<<s.second<<')';}
/*printf("%.9Lf\n",cf);*/
const int MOD = 1000000007;
const double EPS=1e-8;

int trans(char c){
	if(c=='i'){
		return 2;
	}else if(c=='j'){
		return 3;
	}else if(c=='k'){
		return 4;
	}
	return 1;
}

int g[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int get(int first,int second){
	bool plus=first*second>0;
	return plus?g[abs(first)][abs(second)]:-1*g[abs(first)][abs(second)];
}

int rep(int x,int i,int ed,string &s){
	//cerr<<x<<endl;
	if(i==ed) return x;
	return rep(get(x,trans(s[i])),i+1,ed,s);
}

int main() {
	io();
	int T;
	cin>>T;

	for(int i=0;i<T;i++){
		int X,L;
		cin>>L>>X;
		string s;
		cin>>s;
		//cerr<<L<<' '<<X<<' '<<s<<endl;
		int lp=rep(1,0,s.size(),s);
		//cerr<<lp<<endl;

		int ret=1;
		int bb=lp;
		int XX=X;
		while(XX>0){
			if(XX&1){
				ret=get(ret,bb);
			}
			bb=get(bb,bb);
			XX/=2;
		}
		cout<<"Case #"<<i+1<<": ";
		if(ret!=-1){
			cout<<"NO"<<endl;
		}else{
			string ss="";
			//dump(s);
			//cerr<<min(X,16)<<endl;
			for(int j=0;j<min(X,16);j++){
				ss=ss+s;
			}
			//dump(ss);
			vector <int> check(5,INF);
			check[4]=-1;
			int xx=1;
			for(int i=0;i<ss.size();i++){
				xx=get(xx,trans(ss[i]));
				//cerr<<xx<<endl;
				if(xx==2){
					check[xx]=min(check[xx],i);
				}else if(xx==4){
					check[xx]=max(check[xx],i);
				}
			}
			//dump(check[2]);
			//dump(check[4]);
			if(check[2]<check[4]){
				cout<<"YES"<<endl;
			}else{
				cout<<"NO"<<endl;
			}
		}
	}



	return 0;
}