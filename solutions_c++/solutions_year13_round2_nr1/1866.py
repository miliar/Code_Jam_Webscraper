#include <cstdio>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;
vector<int> motki;

int solve() {
	motki.clear();
	int sum;
	scanf("%d", &sum);
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; ++i) {
		int b;
		scanf("%d", &b);
		motki.push_back(b);
	}
	sort(motki.begin(), motki.end());
	int min=n;
	if(sum==1) return n;
	int koszt=n;
	for(int i=0; i<n; ++i) {
		//printf("\t %d", motki[i]);
		//int tempsum=sum;
		while(sum<=motki[i]) {
			koszt++;
			sum=sum*2-1;
			//printf("masa!");
		}
		koszt--;
		if(koszt<min) min=koszt;
		sum+=motki[i];
		//koszt--;
	}
	if(koszt<min) min=koszt;
	return min;
}

int main () {
	int t;
	scanf("%d",&t);
	for(int i=0; i<t;++i) {
		printf("Case #%d: %d\n",i+1, solve());
	}
	return 0;
}

