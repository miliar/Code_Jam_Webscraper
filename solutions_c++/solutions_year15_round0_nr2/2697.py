#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int cakes[1010];

int main() {
	int test;
	scanf("%d",&test);
	for(int t=1; t<=test; t++) {
		int d;
		scanf("%d",&d);
		for(int i=0; i<d; i++)
			scanf("%d",&cakes[i]);

		sort(cakes,cakes+d);

		int temp_ans = cakes[d-1];

		int min_ans=1010,ans;

		for(int i=2; i<cakes[d-1]; i++) {
			ans=0;

			for(int j=0; j<d; j++) {
				ans += (cakes[j]-1)/i;
			}

			ans += i;
			min_ans = min(min_ans,ans);
		}

		min_ans = min(temp_ans,min_ans);
		cout<<"Case #"<<t<<": "<<min_ans<<endl;
	}
	return 0;
}