/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std;

const int mod = 1000000007;
const int MAXN= 2100;
const int MAXT= 2e5;

int C[MAXN][MAXN], fact[MAXN];
int have[MAXT], cnt[MAXT];
int child[MAXT][26];

int mul (int a, int b){
	return ((long long)a * (long long)b) % mod;
}

int add (int a, int b){
	return (a+b)%mod;
}

int m,n;

int dfs (int pos){
	int ret = have[pos];
	for (int i=0; i<26; i++) if (child[pos][i] != -1)
		ret+= dfs(child[pos][i]);
	return ret;
}

int POW (int base, int p){
	int ret = 1, cur = base;
	while (p){
		if (p & 1) ret = mul(ret, cur);
		p>>=1;
		cur = mul(cur, cur);
	}
	return ret;
}

pair<int,int> solve (int pos, int n){
	int m = have[pos];
	if (m < n)		
		return make_pair(0,0);
//	if (m == n)
//		return pair<int,int>(dfs(pos), fact[m]);
	int ret = n;
	vector <int> W(26);
	for (int i=0; i<26; i++) if (child[pos][i] != -1){
		pair<int,int> temp = solve(child[pos][i], min(have[child[pos][i]], n));
		W[i] = temp.second;
		ret+= temp.first;
	}
	int coeff = 0;
	for (int k=0; k<n; k++){
		int sign = 1;
		if (k%2)
			sign = -1;
		int temp = C[n][k];
		if (cnt[pos])
			temp = mul(temp, POW(n-k, cnt[pos]));
		for (int i=0; i<26; i++) if (child[pos][i] != -1){
			int tt = min(have[child[pos][i]], n);
			temp = mul(temp, mul(C[n-k][tt], W[i]));
		}
		coeff = ((long long)coeff + (long long)sign * (long long)temp) % mod;
		if (coeff < 0)
			coeff+= mod;
	}
	return pair<int,int>(ret, coeff);
}

void main2(){
	cin >> m >> n;
	int tot = 1;
	memset(child, -1, sizeof child);
	memset(have, 0, sizeof have);
	memset(cnt , 0, sizeof cnt);
	for (int i=0; i<m; i++){
		string s; cin >> s;
		int cur = 0;
		for (int j=0; j<(int)s.size(); j++){
			have[cur]++;
			if (child[cur][s[j]-'A'] == -1)
				child[cur][s[j]-'A'] = tot++;
			cur = child[cur][s[j]-'A'];
		}
		have[cur]++;
		cnt [cur]++;
	}
	pair<int,int> X = solve(0, n);
	cout << X.first << ' ' << X.second << endl;
}

int main(){
	fact[0] = 1;
	for (int i=1; i<MAXN; i++)
		fact[i] = mul(fact[i-1], i);
	for (int i=0; i<MAXN; i++){
		C[i][0] = 1;
		for (int j = 1; j<=i; j++)
			C[i][j] = add(C[i-1][j], C[i-1][j-1]);
	}
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
