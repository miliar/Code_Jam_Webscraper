#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <unordered_map>
#include <functional>
#include <iostream>

using namespace std;

const int P=1000002013;


int main() {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, M;
		priority_queue<pair<int, int> > Q;
		vector<pair<int, int> > tab;
		scanf("%d %d", &N, &M);
		long long int S0=0, S1=0;
		for (int m=0; m<M; m++) {
			int o, e, p;
			scanf("%d %d %d", &o, &e, &p);
			long long int dist=(e-o);
			S0+=((dist*N- dist*(dist-1)/2)%P) *p;
			S0%=P;
			tab.push_back(make_pair(o, -p));
			tab.push_back(make_pair(e, p));
		}
		sort(tab.begin(), tab.end());
		for (unsigned int k=0; k<tab.size(); ++k) {
			if (tab[k].second<0) {
				Q.push(tab[k]);
			} else {
				int tmp=tab[k].second;
				pair<int, int> B;
				do {
					B=Q.top(); Q.pop();
					int bilety=min(tmp,-B.second);
					tmp-=bilety;
					B.second+=bilety;
					long long int dist=(tab[k].first-B.first);
					S1+=((dist*N- dist*(dist-1)/2)%P) *bilety;
					S1%=P;
					
				} while (tmp>0);
				if (B.second<0) Q.push(B);
			}
		}
		printf("Case #%d: %lld\n", t, (S0-S1+P)%P);
	}
	return 0;
}

