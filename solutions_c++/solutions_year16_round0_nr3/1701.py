#include <bits/stdc++.h>
#include <cmath>
#include <climits>
#include <cstdio>
#include <boost/multiprecision/cpp_int.hpp>

namespace mp = boost::multiprecision;

using namespace std;

#define endl '\n'
#define PB push_back
#define ALL(a)  (a).begin(),(a).end()
#define SZ(a) int((a).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n)  FOR(i,0,n)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#define RBP(i,a) for(auto& i : a)
#define DEBUG(x) cout<<#x<<": "<<(x)<<endl
#define F first
#define S second
#define SNP string::npos
#define WRC(hoge,x) cout << "Case #" << (hoge)+1 << ": " << x << endl
#define ten(n) (LL)pow(10,n)
#define INF ten(8)

typedef pair<int,int> P;
typedef long long int LL;
typedef unsigned long long ULL;
typedef pair<LL,LL> LP;

void ios_init(){ ios::sync_with_stdio(false); cin.tie(0);	
	//cout.setf(ios::fixed);
	//cout.precision(12);
}

vector<int> pl = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227};

int main()
{
	ios_init();
	int T;
	cin >> T;
	REP(hoge,T){
		int n;
		cin >> n;
		int J;
		cin >> J;
		int cnt = 0;
		WRC(hoge,"");
		REP(i,1LL << (n-2)){
			bool f = true;
			vector<int> anv;
			FOR(b,2,11){
				int t = i;
				mp::cpp_int num = 1;
				mp::cpp_int base = b;
				REP(i,n-2){
					if(t&1){
						num += base;
					}
					base *= b;
					t >>= 1;
				}
				num += base;
				f = false;
				//DEBUG(num);
				REP(j,SZ(pl)){
					if(num%pl[j] == 0){
						anv.push_back(pl[j]);
						f = true;
						break;
					}
				}
				if(!f) break;
			}
			if(!f) continue;
			else{
				cnt++;
				int t = i;
				string s;
				s += '1';
				REP(i,n-2){
					s += '0'+(t&1);
					t >>= 1;
				}
				s += '1';
				RREP(i,SZ(s)){
					cout << s[i];
				}
				cout << ' ';
				assert(SZ(anv) == 9);
				REP(i,SZ(anv)){
					cout << anv[i] << ((i == SZ(anv)-1) ? endl : ' ');
				}
			}
			if(cnt == J) break;
		}
		assert(cnt == J);
	}
	return 0;
}


//http://www.boost.org/