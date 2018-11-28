#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(ll (i)=0;(i)<(n);(i)++)
#define dbg(args...) {debug,args; cerr << endl;}

#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define P1(a) (a).first
#define P2(a) (a).second
#define T1(a) (a).first
#define T2(a) (a).second.first
#define T3(a) (a).second.second
#define INF 1e20
#define EPS 1e-8

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<int,pii> tiii;

class debu{
	public:
	template<class someClass>
	debu & operator,(someClass arg){
		cerr << arg << " ";
		return *this;
	}
} debug;


void init(){
    cout << setprecision(8)<< fixed;
}

#define MOD 1000000007ll

ll pow(ll b, ll exp){
    switch(exp){
        case 0ll: return 1ll;
        case 1ll: return b%MOD;
        default: ll a = pow(b, exp/2ll);
            a = (a*a)%MOD;
            if (exp%2==0) return a;
            else return (a*b)%MOD;
    }
    return -1;
}

map< vector<string>, ll> sizes;

ll compute(vector<string> & list){
    map<vector<string>,ll>::iterator it = sizes.find(list);
    if (it!=sizes.end()) return (*it).second;
    set<string> pref;
    rep(i,list.size()){
        rep(j, list[i].length()){
            pref.insert(list[i].substr(0,j+1));
        }
    }
    sizes[list] = pref.size()+1;
    return pref.size()+1;
}

ll solve(ll testnr){
    ll M, N;
    cin >> M >> N;
    vector<string> S(M);
    
    rep(i,M){
        cin >> S[i];
    }
    
    ll combs = pow(N, M);
    //dbg(combs);
    ll count = 0;
    ll worst = 0;
    
    sizes.clear();
    
    for(ll part = 0 ; part < combs; part++){
        ll p = part;
        vector<vector<string> > list(N);
        rep(i,M){
            list[p%N].push_back(S[i]);
            p/=N;
        }
        ll size = 0;
        bool not_filled = false;
        rep(i,N) {
            size += compute(list[i]);
            if (list[i].size()==0) not_filled = true;
        }
        if (not_filled) continue;
        if (size > worst){
            count = 1ll;
            worst = size;
        } else if (size == worst) count++;
    }
    
    cout << worst << " " << (count%MOD);
    return count;
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ": ";
        solve(i);
        cout << "\n";
    }
    
    return 0;
}
