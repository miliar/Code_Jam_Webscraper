#include <cstdio>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({lint x;scanf("%lld", &x);x;})
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001

int main() {
	
	int t;
	double C,F,X;
	t=SS;	
	
	for (int testnum=1; testnum<=t; testnum++) {		
		
		int targetRow, cardNum, cnt[16];

		rep(i,16)
			cnt[i] = 0;

		cin>>targetRow;
		targetRow--;

		rep(i,16) {
			cin>>cardNum;
			if (i/4 == targetRow)
				cnt[cardNum-1]++;
		}
		
		cin>>targetRow;
		targetRow--;

		rep(i,16) {
			cin>>cardNum;
			if (i/4 == targetRow)
				cnt[cardNum-1]++;
		}		
		
		int ans, totCount=0;

		rep(i,16) {
			if (cnt[i]>1) {
				ans = i+1;
				totCount++;
			}
		}

		printf("Case #%d: ",testnum);

		if(totCount == 0)
			printf("Volunteer cheated!\n");
		else if(totCount == 1)
			printf("%d\n", ans);
		else
			printf("Bad magician!\n");

	}
	return 0;
}

