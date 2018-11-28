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
		int n;
		int arr[1010];
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			scanf("%d", &arr[i]);
		}

		int maxgap = 0;
		int skipidx = 0;
		int ans1 = 0;
		for(int i = 1; i < n; i++){
			if(arr[i] < arr[i-1]){
				ans1 += (arr[i-1]-arr[i]);
				maxgap = max(maxgap, arr[i-1]-arr[i]);
			} 
		}
		//cout << maxgap << endl;
		int ans2 = 0;
		for(int i = 0; i < n-1; i++){
			if(arr[i] <= maxgap) ans2 += arr[i];
			else ans2 += maxgap;
		}

		printf("Case #%d: %d %d\n", casenum++, ans1, ans2);
	}
}