#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

int T;
int n, x;
multiset<int> s;
int ans;

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		s.clear();
		scanf("%d%d", &n, &x);
		for(int i=0; i<n; i++) {
			int u;
			scanf("%d", &u);
			s.insert(u);
		}
		ans=0;
		while(!s.empty()) {
			ans++;
			multiset<int>::iterator it=(--s.end());
			int v=*it;
			s.erase(it);
			if(s.empty()) break;
			it=s.upper_bound(x-v);
			if(it!=s.begin()) {
				it--;
				s.erase(it);
			}
		}
		printf("Case #%d: %d\n", q, ans);
	}

	return 0;
}
