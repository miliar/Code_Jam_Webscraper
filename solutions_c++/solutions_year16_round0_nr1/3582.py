#include<bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;


set<int> dgs;

bool add_digits(int x){
	if(x == 0)dgs.insert(0);
	while(x > 0){
		dgs.insert(x%10);
		x/=10;
    }
	return dgs.size() >= 10;
}

void testcase(int T){
	int n, x;
	scanf("%d", &n);
	dgs.clear();

	x=n;
	int cnt = 0;
	for(; !add_digits(x) && cnt < 1000; cnt++)x+=n;
//  assert(cnt < 1000);
	if(cnt < 1000)printf("Case #%d: %d\n", T, x);
	else printf("Case #%d: INSOMNIA\n", T);
}

int main(){
	int T;
	scanf("%d", &T);
	REP(i, T)testcase(i+1);


	return 0;
}
