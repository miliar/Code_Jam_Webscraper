//============================================================================
// Name        : Lawnmower.cpp
// Author      : Simon R‡cz
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	int T;
	scanf("%d\n", &T);

	for (int t=1 ;t<=T ;++t) {
		int N, M;
		scanf("%d %d\n", &N, &M);
		int a;
		multimap<int, pair<int,int> > mm;
		for (int n=1; n<=N; ++n) {
			for (int m=1; m<=M ;++m) {
				scanf("%d", &a);
				mm.insert(make_pair(1000-a, make_pair(n,m)));
			}
		}
		set<int> lines;
		for (int i=1; i<=N+M ;++i) {
			lines.insert(i);
		}

		bool okay = true;
		set<int> sub;
		set<int> diff;
		int H = 100;
		for (multimap<int, pair<int,int> >::iterator it=mm.begin(); it!=mm.end(); ++it) {
			int n = it->second.first;
			int m = it->second.second;
			int h = 1000 - it->first;
			if (h!=H) {
				H = h;
				if(!sub.empty()) {
					set_difference(lines.begin(), lines.end(), sub.begin(), sub.end(), inserter(diff, diff.begin()));
					lines = diff;
					sub.clear();
					diff.clear();
				}
			}
			set<int>::iterator sit;
			sit = lines.find(n);
			if (sit == lines.end()) {
				sit = lines.find(N+m);
				if (sit == lines.end()) {
					okay = false;
					goto bail;
				}
			}
			sub.insert(n);
			sub.insert(N+m);
		}

		bail:
		if (okay) {
			printf("Case #%d: YES\n", t);
		} else {
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}
