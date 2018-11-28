#include <bits/stdc++.h>
using namespace std;

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, n) FOR(i, 0, n)

vector<bool> vec(10, false);
void split(int num) {
	while(num) {
		vec[num%10] = true;
		num /= 10;
	}
}


int solve(int num) {
	int origin = num;
	FORR(i, 10) vec[i] = false;
	bool ok = true;
	num = 0;
	while(ok) {
		num += origin;
		ok = false;
		split(num);
		FORR(i, 10) if(!vec[i]) {ok = true;break;}
	}
	return num;
}

int main() {
	int t, num, res;
	scanf("%d", &t);
	FOR(i, 1, t+1) {
		printf("Case #%d: ", i);
		scanf("%d", &num);
		if(num == 0) printf("INSOMNIA\n");
		else printf("%d\n", solve(num));
	}
}
