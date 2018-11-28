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
		int n; scanf("%d",&n);
		vector<int> A (n);
		for(int i=0;i<n;i++) {
			scanf("%d",&A[i]);
		}
		int answer=0;
		while (A.size()>1){
			int i=min_element(A.begin(),A.end())-A.begin();
			answer+=min(i,(int)A.size()-1-i);
			A.erase(A.begin()+i);
		}
		printf("Case #%d: %d\n",tc,answer);
	}
}
