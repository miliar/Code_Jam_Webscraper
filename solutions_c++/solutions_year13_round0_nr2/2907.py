#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int board[200][200];
int N, M;
bool check(int s, int t) {
	int find1 = 0;
	int find2 = 0;
	for (int i = 0;i < N;++i) {
		if(board[i][t] > board[s][t]) {
			find1 = 1;
			break;
		}
	}
	for (int i = 0;i < M;++i) {
		if(board[s][i] > board[s][t]) {
			find2 = 1;
			break;
		}
	}
	if(find1 && find2) {
		return false;
	}
	return true;
}
void solve()
{
	scanf("%d%d", &N, &M);
	for (int i = 0;i < N;++i) {
		for (int j = 0;j < M;++j) {
			scanf("%d", &board[i][j]);
		}
	}
	for (int i = 0;i < N;++i) {
		for (int j = 0;j < M;++j) {
			if(!check(i, j)) {
				cout<<"NO"<<endl;
				return;
			}
		}
	}
	cout<<"YES"<<endl;
}
int main()
{
	//freopen("data.txt", "r", stdin);

	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1;i <= n;++i) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}