#include <bits/stdc++.h>
#include <cmath>
#include <climits>
#include <cstdio>

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

int main()
{
	ios_init();
	int T;
	cin >> T;
	REP(hoge,T){
		LL n;
		cin >> n;
		if(n == 0){
			WRC(hoge,"INSOMNIA");
			continue;
		}
		LL x = n;
		set<int> s;
		LL ans = -1;
		while(ans == -1){
			stringstream ss;
			ss << x;
			string st = ss.str();
			REP(i,SZ(st)){
				s.insert(st[i]-'0');
				if(SZ(s) >= 10){
					assert(SZ(s) == 10);
					ans = x;
					break;
				}
			}
			x += n;
		}
		WRC(hoge,ans);
	}
	return 0;
}
