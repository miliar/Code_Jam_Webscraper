#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define INF	(int)1e9
#define EPS 1e-9
#define what_is(x) cerr << #x << " is " << x << endl;

int dir[8][2] = {{1,1},{1,0},{1,-1},{0,-1},   // NE,E,SE,S
			    {-1,-1},{-1,0},{-1,1},{0,1}}; // SW,W,NW,N

int dir2[4][2] = {{1,0}, {0,-1}, {-1, 0}, {0,1}};

map<int, int> cnt;
int memo[1010];

int solve(int n){
	while(!cnt[n]) n--;
	if(n <= 3 && cnt[n]) return n; 
	//if(memo[n] != -1) return memo[n];

	int opt1, opt2, opt3 = INF;
	opt1 = n; //just wait for n minutes

	//split all pancakes of this size to n/2 and n-n/2
	cnt[n/2] += cnt[n];
	cnt[n-n/2] += cnt[n];
	opt2 = cnt[n] + solve(n-1);
	cnt[n/2] -= cnt[n];
	cnt[n-n/2] -= cnt[n];

	//split pancakes into 3 in 2 minutes each
	if(n % 3 == 0){
		cnt[n/3] += 3*cnt[n];
		opt3 = 2*cnt[n] + solve(n-1);
		cnt[n/3] -= 3*cnt[n];
	}
	//cout << n << " " << opt1 << " " << opt2 << " " << opt3 << endl;
	return memo[n] = min(opt1, min(opt2, opt3));
}

int main(){
	int tc, casenum = 1;
	scanf("%d", &tc);
	while(tc--){
		cnt.clear();
		memset(memo, -1, sizeof memo);
		int d, x;
		scanf("%d", &d);
		for(int i = 0; i < d; i++){
			scanf("%d", &x);
			cnt[x]++;
		}
		printf("Case #%d: %d\n", casenum++, solve(1000));
	}
}