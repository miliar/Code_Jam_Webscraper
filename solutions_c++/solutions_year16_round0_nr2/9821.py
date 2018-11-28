#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;
const int MAXN = 10;
int dp[1 << MAXN];
string solve(){
	string s;
	cin >> s;
	int a = 0;
	for(int i = 0; i < s.size(); i++)
		a |= ((s[i] == '-' ? 1 : 0) << i);
	return to_string(dp[a]);
}
int main(int argc, char *argv[]){
	for(int i = 0; i < (1 << MAXN); i++)
		dp[i] = (1 << MAXN);
	queue<pair<int, int>> q;
	q.push(make_pair(0, 0));
	while(!q.empty()){
		int a = q.front().first;
		int d = q.front().second;
		q.pop();
		if(dp[a] < d)
			continue;
		dp[a] = d;
		for(int i = 0; i < MAXN; i++){
			int b = (((1 << MAXN) - 1) ^ ((1 << (i + 1)) - 1)) & a;
			for(int j = 0; j <= i; j++)
				b |= ((((1 << j) & a) >> j) ^ 1) << (i - j);
			q.push(make_pair(b, d + 1));
		}
	}
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	return 0;
}