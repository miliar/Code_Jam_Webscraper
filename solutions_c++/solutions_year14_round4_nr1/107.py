#include<cstring>
#include<vector>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for (int tc=1; tc<=T; tc++) {
		int n,W; scanf("%d%d",&n,&W);
		static int X[10005];
		for(int i=0;i<n;i++)scanf("%d",&X[i]);
		sort(X,X+n);
		int l=0,r=n-1;
		int answer=0;
		while (l<=r) {
			if (l==r) { answer++; break; }
			if (X[l]+X[r]<=W) {
				answer++;
				l++;
				r--;
			} else {
				answer++;
				r--;
			}
		}
		printf("Case #%d: %d\n",tc,answer);
	}
}
