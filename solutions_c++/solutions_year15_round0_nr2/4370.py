#include <stdio.h>
#include <algorithm>
using namespace std;

int t, d;
int num[10];

int recurse(int ind, int maxCakes, int splits){
	if(ind == d){
		//printf("returning ind = %d, maxCakes = %d, splits = %d\n", ind, maxCakes, splits);
		return maxCakes + splits;
	}
	int c = num[ind];
	int s1 = c/2, s2 = c/3;
	if(2*s1 < c){s1++;}
	if(3*s2 < c){s2++;}
	//printf("ind = %d, maxCakes = %d, splits = %d, c = %d, s1 = %d, s2 = %d\n", ind, maxCakes, splits, c, s1, s2);
	return min(recurse(ind+1, max(maxCakes, c), splits), min(recurse(ind+1, max(maxCakes, s1), splits+1), recurse(ind+1, max(maxCakes, s2), splits+2)));
}

int main(){
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		scanf("%d", &d);
		for(int j = 0; j < d; j++){
			scanf("%d", &num[j]);
		}
		printf("Case #%d: %d\n", i+1, recurse(0, 0, 0));
	}
	
	return 0;
}
