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
#define WRC(hoge,x) cout << "Case #" << (hoge)+1 << ": " << x 
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
		int k,c,s;
		cin >> k >> c >> s;
		WRC(hoge,"");
		if(k == s) REP(i,k) cout << i+1 << (i == k-1 ? endl : ' ');
		else{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
