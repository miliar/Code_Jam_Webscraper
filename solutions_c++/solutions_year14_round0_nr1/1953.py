#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdio>

using namespace std;

#define mp make_pair
typedef long long llong;
typedef unsigned long long ullong;
typedef pair<int, int> PI;
typedef pair<int, PI> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;

int f1[5];
int f2[5];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int t = 1; t <= tc; ++t){
		int r;
		scanf("%d", &r);
		--r;
		VI V;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				int v;
				scanf("%d", &v);
				if(i == r) f1[j] = v;
			}
		}
		scanf("%d", &r);
		--r;
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				int v;
				scanf("%d", &v);
				if(i == r) f2[j] = v;
			}
		}
		int c = 0, ans = -1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				if(f1[i] == f2[j]) c++, ans = f1[i];
		printf("Case #%d: ", t);
		if(c == 1){
			printf("%d\n", ans);
		}else if(c > 1){
			printf("Bad magician!\n");
		}else{
			printf("Volunteer cheated!\n");
		}
	}
	return 0;
}


