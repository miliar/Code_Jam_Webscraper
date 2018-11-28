#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

int const MAX_N = 200100;
int const ITER = 3000000;

int nnew[15];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	int ind = 0;
	while (t-->0) {
		ind++;
		int n;
		scanf("%d",&n);

		for (int i=0; i<10; i++) nnew[i] = 0;
		long long g = n;
		int fnd = 0;
		long long ans = n;

		for (int e=0; e<ITER; e++) {
			long long x = g;
			while (x > 0) {
				nnew[x%10] = 1;
				x/=10;
			}
			int sum = 0;
			for (int j=0; j<10; j++)
				sum += nnew[j];
			if (sum >= 10) {
				fnd = 1;
				ans = g;
				break;
			}
			g += n;
		}

		printf("Case #%d: ",ind);
		if (fnd) cout<<ans<<"\n";
		else cout<<"INSOMNIA"<<"\n";
	}
	return 0;
}