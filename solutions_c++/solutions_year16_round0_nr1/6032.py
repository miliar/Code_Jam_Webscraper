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
		int n;
		scanf("%d", &n);
		if (n==0) {
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		int C[10]={0};
		int CC=10;
		int res=0;
		do {
			res+=n;
			for (int i=res; i; i/=10) {
				int ii=i%10;
				if (C[ii]==0) {
					C[ii]=1;
					CC--;
				}
			}
		} while (CC);
		
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
