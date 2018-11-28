#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
#include <set>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())


int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		int M,N;
		cin >> M >> N;
		vector<string> words(M);
		fu(i,0,M) cin >> words[i];
		int cnts[1000];
		memset(cnts,0,sizeof(cnts));
		int maxcnt=0;
		fu(i,0,1<<(M+M)) {
			set<string> blocks[4];
			bool good=true;
			fu(j,0,M) {
				int k=(i>>(j+j))&3;
				if(k>=N) good=false;
				fu(l,0,words[j].size()+1) blocks[k].insert(words[j].substr(0,l));
			}
			int cnt=0;
			if(!good) continue;
			fu(i,0,4) cnt+=blocks[i].size();
			cnts[cnt]++;
			maxcnt = max(maxcnt, cnt);
		}
		cout << "Case #" << ts << ": " << maxcnt << " " << cnts[maxcnt] << endl;
	}
}
