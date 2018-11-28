#include<stdio.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
using namespace std;

typedef long long int LL;
LL MOD = 1000002013;

LL Calc(LL N, LL distance){
	return distance * (2*N - (distance-1)) / 2;
}

int main() {
	int T, caseNum;
	scanf("%d",&T);
	
	for(caseNum=1; caseNum<=T; ++caseNum) {
		int N, M;
		scanf("%d%d",&N, &M);

		vector<int> compress;
		map<int,int> enter, leave;	//[station] = count

		LL ideal = 0;

		for(int i=0; i<M; ++i){
			int e,o,p;
			scanf("%d%d%d",&e,&o,&p);
			enter[e]+=p;
			leave[o]+=p;
			compress.push_back(e);
			compress.push_back(o);

			ideal += p * Calc(N, o-e);
			
		}
		sort(compress.begin(), compress.end());
		compress.erase(unique(compress.begin(), compress.end()), compress.end());

		LL res = 0;

		deque<pair<int,int>> d;	// <beginStatsion, count>
		for(int s : compress){
			int e = enter[s];
			int o = leave[s];
			
			if(e){
				d.push_back(make_pair(s, e));
			}
			if(o){
				while(o){
					pair<int,int> &ref = d.back();
					int c = min(o, ref.second);
					o -= c;
					ref.second -= c;

					int diff = (s-ref.first);

					res += c * Calc(N, diff);
					res %= MOD;

					if(ref.second == 0){
						d.pop_back();
					}
				}
			}
		}

		printf("Case #%d: %lld\n", caseNum, (ideal - res + MOD)%MOD);
	}
	return 0;
}
