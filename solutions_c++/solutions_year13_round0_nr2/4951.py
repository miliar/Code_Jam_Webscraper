#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define reps(i,f,n) for(int i=f; i<int(n); ++i)
#define rep(i,n) reps(i,0,n)

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int INF = 1001001001;
const double EPS = 1e-10;

bool solve()
{
	int h, w;
	scanf("%d%d", &h, &w);
	
	int board[100][100];
	rep(i, h) rep(j, w){
		scanf("%d", &board[i][j]);
	}
	
	vector<pii> data[100];
	rep(i, h) rep(j, w){
		data[board[i][j]-1].push_back(pii(i, j));
	} 
	
	bool doney[100] = {false}, donex[100] = {false};
	for(int i=99; i>=0; --i){
		rep(j, data[i].size()){
			int y = data[i][j].first;
			int x = data[i][j].second;
			if(doney[y] && donex[x])
				return false;
		}
		rep(j, data[i].size()){
			int y = data[i][j].first;
			int x = data[i][j].second;
			doney[y] = donex[x] = true;
		}
	}
	return true;
}

int main()
{
	int t;
	scanf("%d", &t);
	rep(i, t){
		printf("Case #%d: %s\n", i+1, solve() ? "YES" : "NO");
	}
	return 0;
}
