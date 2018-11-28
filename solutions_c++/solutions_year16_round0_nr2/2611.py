#include <cstdio>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

double a[1000000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases = 0;
	scanf("%d",&cases);
	for(int casenum = 1; casenum <= cases; casenum++) {
		char s[200];
		scanf("%s", &s);
		char c = '+';
		int ans = 0;
		for(int i = strlen(s)-1; i>=0; i--) {
			if(s[i]!=c){
				ans++;
				c=s[i];
			}
		}
		printf("Case #%d: %d\n", casenum, ans);
	}
	return 0;
}