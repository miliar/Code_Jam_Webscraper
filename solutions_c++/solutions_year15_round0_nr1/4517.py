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

int main(){
	int tc, casenum = 1;
	scanf("%d", &tc);
	while(tc--){
		int n, x, ans = 0, sum = 0;
		string s;
		scanf("%d", &n);
		cin >> s;
		for(int i = 0; i <= n; i++){
			x = s[i] - '0';
			if(i == 0 && x < 1){ ans++; sum++;}
			if(x > 0 && sum < i) {ans += i-sum; sum = i;}
			sum += x;
		}
		printf("Case #%d: %d\n", casenum++, ans);
	}
}