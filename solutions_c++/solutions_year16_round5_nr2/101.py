#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define UPD(a,b) { a = (a + (b)) % MD; }

const int MD = 1000000007;
const int INF = 0x3f3f3f3f;
const double pi = acos(-1.0);

double C[211][211], fac[111];
double f[111];
int s[111];
double calc_numbers(const vector<int> &vec) {
	int sum = 0;
	for (auto x: vec) {
		sum += s[x];
	}
	double ans = fac[sum];
	for (auto x: vec) {
		ans = ans / fac[s[x]];
		ans = ans * f[x];
	}
	return ans;
}

vector<int> son[111];
void dfs(int x) {
	s[x] = 1;
	vector<int> seq;
	for (auto y: son[x]) {
		dfs(y);
		s[x] += s[y];
		seq.push_back(y);
	}
	f[x] = calc_numbers(seq);
}

int n, m, par[111];
string query[11];
char title[111];
vector<int> tmp, cand;
int cnt[111];
double prob[111];
int main() {
	int T; cin >> T;
	C[0][0] = 1;
	fac[0] = 1;
	For(i,1,100) fac[i] = fac[i - 1] * i;
	For(i,0,200) For(j,0,200) {
		C[i + 1][j] += C[i][j];
		C[i + 1][j + 1] = C[i][j];
	}
	For(TK,1,T) {
		cerr << TK << endl;
		cin >> n;
		For(i,1,n) son[i].clear();
		For(i,1,n) {
			scanf("%d", &par[i]);
			son[par[i]].push_back(i);
		}
		scanf("%s", title + 1);
		cin >> m;
		For(i,1,m) cin >> query[i];
		For(i,1,n) if (!par[i]) {
			dfs(i);
		}
		memset(cnt, 0, sizeof cnt);
		For(TIME,1,10000) {
			cand.clear();
			For(i,1,n) if (par[i] == 0) cand.push_back(i);
			string S = "";
			For(cc,1,n) {
				double all = calc_numbers(cand);
				For(i,1,cand.size()) {
					int x = cand[i - 1];
					double nxt_all = 1.0 / f[x] * fac[s[x]] / (n - cc + 1);
					//for (auto y: tmp) nxt_all /= fac[s[y]] / f[y];
					nxt_all /= fac[s[x] - 1] / f[x];
					prob[i] = nxt_all;
				}
				For(i,1,cand.size()) prob[i] += prob[i - 1];
				For(i,1,cand.size()) prob[i] *= 1000;
				int x = rand() % 1000;
				int c = 0;
				For(i,1,cand.size()) if (prob[i - 1] <= x + 0.5 && x + 0.5 <= prob[i]) {
					c = i;
					break ;
				}
				S += title[cand[c - 1]];
				tmp = son[cand[c - 1]];
				For(j,1,cand.size()) if (j != c) tmp.push_back(cand[j - 1]);
				cand = tmp;
			}
			For(i,1,m) if (S.find(query[i]) != string::npos) {
				++cnt[i];
			}
		}
		printf("Case #%d:", TK);
		For(i,1,m) printf(" %.12f", (double)cnt[i] / 10000);
		puts("");
	}
	return 0;
}
