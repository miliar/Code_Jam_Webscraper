#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int ds[1005];
int blah(int d, int target){
	int out = target;
	for(int j = 0; j < d; j++){
		out += ((ds[j]+target-1)/target) - 1;
	}
	return out;
}


int main(){
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		int d;
		scanf("%d", &d);
		int highest = 0;
		for(int j = 0; j < d; j++){
			scanf("%d", ds + j);
			highest = max(highest,ds[j]);
		}
		//out += (int)((high + tmpa - 1)/tmpa);
		//int target = out;
		//for(int j = 0; j < d; j++){
		//	out += ((ds[j] + target - 1)/target) - 1;
		//}
		int out = blah(d,1);
		for(int j = 2; j <= highest; j++){
			out = min(out,blah(d,j));
		}
		printf("Case #%d: %d\n", i, out);
	}
	return 0;
}
		
