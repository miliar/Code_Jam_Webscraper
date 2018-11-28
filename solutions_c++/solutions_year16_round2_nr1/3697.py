#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair

#define eps 0.0000001
#define pi  3.14159265359
#define inf 2000000000

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const int maxn = 2000 + 5;
const string digits[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int tt, n, cnt[200];
char S[maxn];

bool check(int k) {
	int len = digits[k].length();
	for (int i = 0; i < len; i++) {
		cnt[digits[k][i]]--;
		if (cnt[digits[k][i]] < 0) {
			for (int j = i; j >= 0; j--) {
				cnt[digits[k][j]]++;
			}
			return false;
		}
	}
	return true;
}

bool undo(int k) {
	int len = digits[k].length();
	for (int i = 0; i < len; i++) {
		cnt[digits[k][i]]++;
	}
}

bool dfs(int last, vector<int>& sol) {
	bool allzeros = true;
	for (int i = 'A'; i <= 'Z'; i++)
		if (cnt[i] != 0) {
			allzeros = false;
			break;
		}
	if (allzeros) {
    	for (int i = 0; i < sol.size(); i++) printf("%d", sol[i]);
    	printf("\n");
    	return true;
	}
	for (int i = last; i < 10; i++) {
		if (check(i)) {
			sol.push_back(i);
			bool ret = dfs(i, sol);
			if (ret) return true;
			else {
				sol.pop_back();
				undo(i);
			}
		}
	}
	return false;
}

int main() {
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
    	scanf("%s", S);
    	n = strlen(S);
    	for (int i = 'A'; i <= 'Z'; i++) cnt[i] = 0;
    	for (int i = 0; i < n; i++) cnt[S[i]]++;
    	printf("Case #%d: ", t);
    	vector<int> sol;
    	dfs(0, sol);
    }
    return 0;
}
