#include<bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

int p, q, n, h[100], g[100];
int dp[110][1100][2];


int rec(int pos, int pass, int first){
	if(pos >= n) return 0;
	int &res = dp[pos][pass][first];
	if(res >= 0) return res;
	
	res = rec(pos + 1, pass + (h[pos] + q - 1) / q - !first, 1);
	
	//Ž©•ª‚ªi‰ñ‘ŠŽè‚ªj‰ñ‰£‚é
	rep(i, 20) rep(j, 20) if(i * p + j * q >= h[pos]){
		//‘ŠŽè‚ªŽE‚·
		if(j && i * p + (j - 1) * q < h[pos]){
			if(pass + j - i - !first >= 0)
			res = max(res, rec(pos + 1, pass + j - i - !first, 1));
		}
		if(i && (i - 1) * p + j * q < h[pos]){
			if(pass + 1 + j - i - !first >= 0)
			res = max(res, g[pos] + rec(pos + 1, pass + 1 + j - i - !first, 0));
		}
	}
	return res;
}

void solve(){
	memset(dp, -1, sizeof(dp));
	
	cin >> p >> q >> n;
	rep(i, n) cin >> h[i] >> g[i];
	
	cout << rec(0, 0, 1) << endl;
}

int main(){
	int CS; cin >> CS;
	rep(cs, CS){
		cout << "Case #" << cs + 1 << ": ";
		solve();
	}
	return 0;
}
