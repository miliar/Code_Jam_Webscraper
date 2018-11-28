#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<ctime>
#include<complex>
#include<functional>
#include<climits>
#include<cassert>
#include<iterator>
#include<unordered_map>
using namespace std;


int t;

int n;

int T[26][26];

string s;

int K[26][26];

bool dp[5][1 << 4];
int ok(){
	int dif = 0;
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			if (K[i][j] < T[i][j]){
				return INT_MAX;
			}
			if (K[i][j] != T[i][j]){
				dif++;
			}
		}
	}
	vector<int> ord;
	for (int i = 0; i < n; i++){
		ord.push_back(i);
	}
	do{
		for (int i = 0; i <= n; i++){
			for (int j = 0; j < (1 << n); j++){
				dp[i][j] = false;
			}
		}
		dp[0][0] = true;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < (1 << n); j++){
				if (dp[i][j]){
					bool ooo = false;
					for (int k = 0; k < n; k++){
						if (K[ord[i]][k] == true && ((j >> k) & 1) == 0){
							dp[i + 1][j | (1 << k)] = true;
							ooo = true;
						}
					}
					if (!ooo){
						dp[i + 1][j] = true;
					}
				}
			}
		}
		for (int j = 0; j + 1 < (1 << n); j++){
			if (dp[n][j])return INT_MAX;
		}
	} while (next_permutation(ord.begin(), ord.end()));
	return dif;
}
int main(){
	cin >> t;
	int TT = 0;
	while (t--){
		cin >> n;
		TT++;
		for (int i = 0; i < n; i++){
			cin >> s;
			for (int j = 0; j < s.size(); j++){
				if (s[j] == '1'){
					T[i][j] = 1;
				}
				else{
					T[i][j] = 0;
				}
			}
		}
		int N = n*n;
		int ans = INT_MAX;
		for (int i = 0; i < (1 << N); i++){
			for (int j = 0; j < N; j++){
				if ((i >> j) & 1){
					K[j / n][j % n] = 1;
				}
				else{
					K[j / n][j % n] = 0;
				}
			}
			ans = min(ans, ok());
		}
		printf("Case #%d: ", TT);
		cout << ans << endl;
	}
	return 0;
}