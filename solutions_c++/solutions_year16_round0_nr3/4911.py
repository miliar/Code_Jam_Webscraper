#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

const int M = 8;
int pr[8] = {2,3,5,7,11,13,17,19};
int T,N,J;
int mask[32];
vector< pair<string, vector<int> > > result;

int have(int mask[], int base) {
	for(int z=0;z<M;++z) {
		int p = pr[z];
		int r = 0;
		int b = 1;
		for(int i=0;i<N;++i) {
			if(mask[i] == 1) {
				r = (r + b) % p;
			}
			b = b * base % p;
		}
		if(r == 0) return p;
	} return -1;
}

void backtr(int idx, int left) {
	if(result.size() >= J) return;
	if(left < 0) return;
	if(idx == 0) {
		backtr(idx+1, left);
	} else if(idx == N-1) {
		backtr(idx+1, left);
	} else if(idx == N) {
		vector<int> t;
		string x = "";
		for(int i=0;i<N;++i) {
			if(mask[i]) x.push_back('1');
			else x.push_back('0');
		} reverse(x.begin(), x.end());
		for(int base=2;base<=10;++base) {
			int r = have(mask, base);
			if(r == -1) return;

			t.push_back(r);
		}
		result.push_back(make_pair(x, t));
	} else {
		mask[idx] = 1;
		backtr(idx + 1, left-1);
		mask[idx] = 0;
		backtr(idx + 1, left);
	}
}
int main() {
	scanf("%d", &T);
	for(int cs=1;cs<=T;++cs) {
		printf("Case #%d:\n",cs);
		scanf("%d%d",&N,&J);
		mask[0] = 1, mask[N-1] = 1;
		for(int left=2;left<=N;left+=2) {
			backtr(0, left);
		}
		if(result.size() < J) {
			printf("WHAAAT: %d - %d", (int)result.size(), J);
			return 0;
		}
		for(int i=0;i<J;++i) {
			printf("%s", result[i].first.c_str());
			vector<int> &v = result[i].second;
			for(int j=0;j<v.size();++j) {
				printf(" %d", v[j]);
			} puts("");
		}
	}
}
