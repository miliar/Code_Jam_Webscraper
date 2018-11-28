#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
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
		char S[1024];
		scanf("%s", S);
		int n=strlen(S);
		S[n]='+';
		int res=0;
		for (int i=0; i<n; i++) {
			res+=(S[i]!=S[i+1]);
		}
		
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
