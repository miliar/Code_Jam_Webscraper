#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;


int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		vector<int> tab[128];
		vector<char> S0;
		char s[128];
		int N;
		scanf("%d%s", &N, s);
		for(int i=0, j=1; s[i]; i = j++) {
			while(s[i]==s[j]) j++;
			tab[S0.size()].push_back(j-i);
			S0.push_back(s[i]);
		}
		bool ok=true;
		for(int n=1; n<N; n++) {
			vector<char> S1;
			scanf("%s", s);
			for(int i=0, j=1; s[i]; i = j++) {
				while(s[i]==s[j]) j++;
				tab[S1.size()].push_back(j-i);
				S1.push_back(s[i]);
			}
			ok=ok && (S0==S1);
		}

		printf("Case #%d: ", t);
		if (ok) {
			int res=0;
			for (int i=0; i<S0.size(); i++) {
				sort(tab[i].begin(), tab[i].end());
				int m=tab[i][tab[i].size()/2];
				for(int x:tab[i]) res+=abs(x-m);
			}
			printf("%d\n", res);
		} else {
			printf("Fegla Won\n");
		}
	}
	return 0;
}

