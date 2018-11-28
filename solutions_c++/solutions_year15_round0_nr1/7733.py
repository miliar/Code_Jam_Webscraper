#include <iostream>
#include <vector>
#include <numeric>
#include <climits>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm> 
#include <map> 
#include <set>

#define ALL(v) (v).begin(),(v).end()
#define REP(i,p,n) for(int i=p;i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define dump(a) (cerr << #a << "=" << (a) << endl)
#define DUMP(list) cout << "{"; for(auto nth : list){ cout << nth << " ";}cout << "}" << endl;

using namespace std;

template<class T> T MIN(const T& a, const T& b) { return a < b ? a : b; }
template<class T> T MAX(const T& a, const T& b) { return a > b ? a : b; }
template<class T> void MIN_UPDATE(T& a, const T& b) { if (a > b) a = b; }
template<class T> void MAX_UPDATE(T& a, const T& b) { if (a < b) a = b; }



int main(){
	int T;
	cin >> T;
	rep(i,T){
		int s;
		string k;
		cin >> s >> k;
	
		int ans=0,tmp=0;
		rep(j,s+1){
			if((k[j]-'0')>0&&tmp<j){ans+=j-tmp; tmp+=j-tmp;}
			tmp+=(k[j]-'0');	
		}

		cout << "Case #" << i+1 << ": " << ans << endl;

	}
}
