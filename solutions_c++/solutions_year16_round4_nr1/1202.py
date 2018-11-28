#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

vector<char> go(const vector<char> &v){
	vector<char> ret;
	for (const auto &c : v){
		if (c == 'R'){
			ret.push_back('R');
			ret.push_back('S');
		}
		else if (c == 'S'){
			ret.push_back('P');
			ret.push_back('S');
		}
		else{
			ret.push_back('P');
			ret.push_back('R');
		}
	}
	return ret;
}

void mysort(vector<char> &v, int depth){
	int i = 0;
	int blk = (1 << depth);
	while (i < v.size()){
		vector<char> L(v.begin() + i, v.begin() + i + blk);
		vector<char> R(v.begin() + i + blk, v.begin() + i + blk + blk);
		if (R < L) swap(L, R);
		for (int j = 0; j < blk; j++)
			v[i + j] = L[j];
		for(int j=0;j<blk;j++)
			v[i + blk + j] = R[j];
		i += blk;
		i += blk;
	}
}
int N, R, P, S;

bool chk(const vector<char>& v){
	return count(v.begin(), v.end(), 'R') == R
		&& count(v.begin(), v.end(), 'S') == S
		&& count(v.begin(), v.end(), 'P') == P;
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc); scanf("%d%d%d%d", &N, &R, &P, &S);
		// case 'R'
		vector<char> r(1, 'R'), p(1, 'P'), s(1, 'S');
		for (int i = 0; i < N; i++) r = go(r), p = go(p), s = go(s);

		vector<char> r1, p1, s1;
		if (chk(r)){
			r1 = r;
			for (int i = 0; i < N; i++) mysort(r1, i);
		}
		if (chk(p)){
			p1 = p;
			for (int i = 0; i < N; i++)mysort(p1, i);
		}
		if (chk(s)){
			s1 = s;
			for (int i = 0; i < N; i++) mysort(s1, i);
		}

		if (!r1.size() && !s1.size() && !p1.size()){
			printf("IMPOSSIBLE\n");
		}
		else{
			vector<char> res(1 << (N - 1), 'Z');
			if (r1.size()) res = min(res, r1);
			if (s1.size()) res = min(res, s1);
			if (p1.size()) res = min(res, p1);
			for (char c : res) printf("%c", c);
			printf("\n");
		}
	}
}