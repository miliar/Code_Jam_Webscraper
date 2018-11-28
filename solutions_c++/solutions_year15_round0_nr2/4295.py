#include <bits/stdc++.h>
using namespace std;

vector<int> arr;
int mini;

int main() {
	int T;
	scanf("%d",&T);
	for (int z=1;z<=T;++z) {
		mini=1000000;
		int D;
		scanf("%d",&D);
		arr.clear();
		for (int i=0;i<D;++i) {
			int d;
			scanf("%d",&d);
			arr.push_back(d);
		}
		for (int i=1;i<=1000;++i) {
			int now=i;
			for (int j=0;j<(int)arr.size();++j) {
				now+=arr[j]/i;
				if (arr[j]%i==0) --now;
			}
			if (mini>now) mini=now;
		}
		printf("Case #%d: %d\n",z,mini);
	}
}
