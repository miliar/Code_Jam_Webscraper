#include <cstdio>
#include <string>

using namespace std;

const int MAX = 9999;

string tree[MAX];

//P -> R -> S
string init(int round, int rock, int paper, int scissors) {
	if (round == 0) {
		if (rock == 1) return "R";
		if (paper == 1) return "P";
		if (scissors == 1) return "S";
		return "ERROR";
	} else {
		int max = rock;
		if (paper > max) max = paper;
		if (scissors > max) max = scissors;

		if (-(max - rock - paper - scissors) < max) return "IMPOSSIBLE";

		int rp, ps, sr;
		if (max == rock) {
			ps = (paper + scissors - rock) >> 1;
			rp = paper - ps;
			sr = scissors - ps;
		} else if (max == paper) {
			sr = (scissors + rock - paper) >> 1;
			rp = rock - sr;
			ps = scissors - sr;
		} else {
			rp = (rock + paper - scissors) >> 1;
			sr = rock - rp;
			ps = paper - rp;
		}

		string next = init(round-1, sr, rp, ps);
		if (next == "IMPOSSIBLE") return next;

		string ret = "";
		for (char c : next) {
			if (c == 'R') ret.append("RS");
			if (c == 'P') ret.append("PR");
			if (c == 'S') ret.append("PS");
		}

		return ret;
	}
}

void solve(int n, string iv) {
	int gap = 1 << n;
	for (int i = 0; i < gap; i++) {
		tree[gap + i] = iv[i];
	}
	for (int now = gap-1; now >= 1; now--) {
		if (tree[now*2] < tree[now*2 + 1]) tree[now] = tree[now*2] + tree[now*2 + 1];
		else tree[now] = tree[now*2 + 1] + tree[now*2];
	}
}

int main() {
	freopen("output.txt", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);
	for (nowCase = 1; nowCase <= numCase; nowCase++) {
		int n, rock, paper, scissors;
		scanf("%d%d%d%d", &n, &rock, &paper, &scissors);
		
		string r = init(n, rock, paper, scissors);
		if (r == "IMPOSSIBLE") {
			printf("Case #%d: IMPOSSIBLE\n", nowCase);
		} else {
			solve(n, r);
			printf("Case #%d: %s\n", nowCase, tree[1].data());
		}
	}

	return 0;
}