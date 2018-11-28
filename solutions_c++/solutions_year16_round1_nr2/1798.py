#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long lld;

#define SIZE 100

#define IN freopen("B-large.in","r",stdin);
#define OUT freopen("B-large.out","w",stdout);

int T, N;
int mark[2500+10];

int main()
{
	IN
	OUT
	int i,j,t, a;
	string S;

	cin >> T;

	for(t=1;t<=T;t++){
		memset(mark, 0, sizeof(mark));
		cin >> N;

		vector<int> ans;

		for(i=0;i<2*N-1; i++) {
			for(j=0; j<N; j++) {
				cin >> a;
				mark[a]++;
			}
		}

		for(i=1; i<=2500; i++) {
			if(mark[i] & 1) {
				ans.push_back(i);
			}
		}

		sort(ans.begin(), ans.end());
		// assert(ans.size(), N);

		printf("Case #%d: ",t);
		cout << ans[0];
		for(i=1; i<ans.size(); i++) {
			cout << " " << ans[i];
		}

		cout << endl;
	}
	return 0;
}
