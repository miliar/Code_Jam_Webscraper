#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int cases;
	scanf("%d",&cases);
	int n,x;
	vector<int> data;
	for(int round=1; round<=cases; round++) {
		scanf("%d%d",&n,&x);
		data.resize(n);
		for(int i=0; i<n; i++)
			scanf("%d",&data[i]);
		sort(data.begin(),data.end());
		int ans=0;
		while(!data.empty()) {
			ans++;
			int a=data.back();
			data.pop_back();
			int remain=x-a;
			vector<int>::iterator it=upper_bound(data.begin(),data.end(),remain);
			if(it!=data.begin()) {
				data.erase(--it);
			}
		}
		printf("Case #%d: %d\n",round,ans);
	}
	return 0;
}
