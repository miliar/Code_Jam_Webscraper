#include <bits/stdc++.h>
#define YES "GABRIEL"
#define NO "RICHARD"
using namespace std;
int tcs, x, r, c;
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%i%i%i", &x, &r, &c);
		if(x > (r*c) || x > max(r, c) || (r * c) % x != 0 || x > 6 || (min(r, c) == 1 && x > 2) || (min(r, c) == 2 && max(r, c) == 4 && x == 4)) { printf("Case #%i: %s\n", tc, NO); continue; }
		printf("Case #%i: %s\n", tc, YES);
	}
}