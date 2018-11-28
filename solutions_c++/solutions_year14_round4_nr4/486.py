#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <cstdio>

using namespace std;

vector<int> SOL;
vector<string> S;
vector<vector<int> > d;

struct node {
	int next[26] = {0};
};

int count(int pos) {
	vector<node> nodes(1);
	for(int i=0; i < d[pos].size(); i++) {
		string a = S[d[pos][i]];
		int no = 0;
		for(int j=0; j < a.size(); j++) {
			if(nodes[no].next[a[j] - 'A'] == 0) {
				nodes[no].next[a[j] - 'A'] = nodes.size();
				nodes.resize(nodes.size() + 1);
			}
			no = nodes[no].next[a[j] - 'A'];
		}
	}
	return nodes.size();
}

void b(int pos) {
	if(pos == S.size()) {
		int sum = 0;
		for(int i=0; i < d.size(); i++) { sum += count(i); if(d[i].size() == 0) return; }
		SOL[sum]++;
		return;
	}
	for(int i=0; i < d.size(); i++) {
		d[i].push_back(pos);
		b(pos+1);
		d[i].resize(d[i].size() - 1);
	}
}
void solve(int t) {
	cout << "Case #"<< t<<": ";
	int N, M;
	cin >> M >> N;
	S.resize(M);
	SOL.resize(0); SOL.resize(47 * 2, 0);
	d.resize(0); d.resize(N);

	for(int i=0; i < M; i++) cin >> S[i];

	b(0);

	for(int i= 47*2 -1; i > 0; i--) {
		if(SOL[i] ==0) continue;
		cout << i << " " << SOL[i] << endl;
		return;
	}
}
int main(void) {
	int T;
	cin >> T;

	for(int t=1;t<=T;t++) solve(t);
}