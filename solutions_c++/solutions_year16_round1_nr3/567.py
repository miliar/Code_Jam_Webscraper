#include <iostream>
#include <string.h>

using namespace std;


	int t, tCounter, N;
	int i, j;
	int BFF[1001];
	int maxim, ring, current;
	int lens[1001];
	int spec[1001],specs;
	int other[1001],others;
	int branch;

int dfs (int index) {
	int local_max=0;
	int tmp;
	for (int local_ind=0;local_ind<others;local_ind++) {
		if (BFF[other[local_ind]]==index) {
			tmp = dfs(other[local_ind]);
			if (tmp>local_max)
				local_max=tmp;
		}
	}
	return local_max+1;
}

int main(){
	cin >> t;
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cin >> N;
		for (i=0;i<N;i++) {
			cin >> BFF[i];
			BFF[i]--;
			lens[i]=0;
		}
		maxim = 0;
		cout << "Case #" << tCounter << ": ";
		specs=0;
		others=0;
		ring = 0;
		branch=0;
		for (i=0; i<N; i++) {
			current=i;
			for (j=0;j<N;j++){
				if (BFF[current]==i) {
					lens[i]=j+1;
					break;
				}
				current=BFF[current];
			}
		}
		for (i=0; i<N; i++) {
			if (lens[i]>maxim)
				maxim=lens[i];
			if (lens[i]==2) {
				spec[specs]=i;
				specs++;
			}
			if (lens[i]==0) {
				other[others]=i;
				others++;
			}
		}

		for (i=0;i<specs;i++) {
			branch += dfs(spec[i]);
		}
		if (branch > maxim)
			maxim=branch;
		cout << maxim ;
		cout << endl;
	}
	return 0;
}

