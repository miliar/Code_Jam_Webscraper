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

string conv(const string& x){
	string res;
	char pre = x[0];
	REP(i,SZ(x)){
		if(pre != x[i]){
			res += pre;
			pre = x[i];
		}
	}
	res += x[SZ(x)-1];
	return res;
}

int main()
{
	ios_init();
	int T;
	cin >> T;
	REP(hoge,T){
		int dp[2][110];
		string in;
		cin >> in;
		in = conv(in);
		//DEBUG(in);
		dp[0][0] = 1; //-
		dp[1][0] = 0; //+
		FOR(i,1,SZ(in)){
			dp[0][i] = dp[1][i-1]+1;
			dp[1][i] = dp[0][i-1]+1;
		}
	//	DEBUG(in[0]);
		if(in[0] == '+'){
			WRC(hoge,dp[1][SZ(in)-1]);
		}else{
			WRC(hoge,dp[0][SZ(in)-1]);
		}
	}
	return 0;
}
