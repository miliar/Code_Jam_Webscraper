#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
using namespace std;
int n,m,i,j,tn,x,y,z,g,k,ti,r,c,w;
int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("Q1.txt", "w", stdout);
	scanf("%d", &tn);
	for(ti = 1; ti <= tn; ti++){
		scanf("%d%d%d", &r, &c, &w);
		int ans = (c * r - 1) / w + w;
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
