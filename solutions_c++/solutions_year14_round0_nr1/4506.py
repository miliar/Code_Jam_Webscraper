#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <string>
#include <map>

using namespace std;
typedef long long ll;
typedef pair<int,int> pr;

int main()
{
	// code here
	int T;
	set<int> s[2];
	set<int>::iterator it;
	scanf("%d", &T);
	for (int cc=1; cc<=T; cc++) {
		s[0].clear();	s[1].clear();
		int choose[2];
		int ar[2][4][4];
		for (int k=0; k<2; k++) {
			scanf("%d", choose+k);
			for (int i=0; i<4; i++) {
				for (int j=0; j<4; j++) {
					scanf("%d", &ar[k][i][j]);
					if (choose[k]-1 == i) {
						s[k].insert(ar[k][i][j]);
					}
				}
			}
		}
		
		int cnt=0, ans=0;
		for (it=s[0].begin(); it!=s[0].end(); it++) {
			if (s[1].count(*it)) {
				cnt++;
				ans = *it;
			}
		}

		if (cnt > 1) {
			printf("Case #%d: Bad magician!\n", cc);
		}
		else if (cnt < 1) {
			printf("Case #%d: Volunteer cheated!\n", cc);
		}
		else {
			printf("Case #%d: %d\n", cc, ans);
		}
	}

	// code ends here
	return 0;
}
