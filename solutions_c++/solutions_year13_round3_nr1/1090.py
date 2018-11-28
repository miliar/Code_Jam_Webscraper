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
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
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

ll solve(int testnr){
    string s;
    int n;
    cin >> s;
    cin >> n;
    int l = s.length();
    ll count = 0;
    int running = 0;
    int prev = -1;
  //  dbg(s,n);
    for(int i=0;i<l;i++){
        switch(s[i]){
            case'a': case'e':case'i':case'o':case'u':
                running = 0;
                break;
            default:
                running++;
        }
        if (running>=n){
            count+= (i-n-prev + 1) * (l-i);
            prev = i-n+1;
        }
    }
    return count;
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ": " << solve(i) << "\n";
    }
    
    return 0;
}
