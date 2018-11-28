#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

int main() {
	int cases;
	scanf("%d",&cases);
	for(int round=1; round<=cases; round++) {
		int n;
		scanf("%d",&n);
		vi data(n);
		for(int i=0; i<n; i++)
			scanf("%d",&data[i]);
		vi order=data;
		sort(order.begin(),order.end());
		for(int i=0; i<n; i++)
			data[i]=lower_bound(order.begin(),order.end(),data[i])-order.begin();
		int ans=0;
		for(int i=0; i<n; i++) {
			int pos=0;
			while(data[pos]!=i)
				pos++;
			ans+=min(pos,(int)data.size()-pos-1);
			data.erase(data.begin()+pos);
		}
		printf("Case #%d: %d\n",round,ans);
	}
	return 0;
}
