//---------------------------------------------------------------------
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
using namespace std;


//---------------------------------------------------------------------

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int qq=0; qq<t; qq++) {
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double mn = 1e100;
		double on_one_sec = 2.0, tm = 0.0;
		mn = min(mn, x/on_one_sec);
		for (int to_b = 0; to_b<50000000; to_b++) {
			mn = min(mn, tm + x/on_one_sec);
			tm += c/on_one_sec;
			on_one_sec += f;
			mn = min(mn, tm + x/on_one_sec);
		}
		printf("Case #%d: %.7lf",qq+1,mn);
		if (qq<t-1) printf("\n");
	}

	return 0;
}