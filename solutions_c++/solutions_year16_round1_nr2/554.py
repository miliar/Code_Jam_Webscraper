#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

int main(){
	int t, tCounter, N;
	cin >> t;
	int i,j;
	int list[50];
	int nums[2501];
	int tmp;
	for (tCounter = 1; tCounter <= t; tCounter++) {
		cin >> N;
		cout << "Case #" << tCounter << ": ";
		for (i=0;i<2501;i++)
			nums[i]=0;
		for (i=0;i<2*N-1;i++)
			for (j=0;j<N;j++) {
				cin>>tmp;
				nums[tmp]++;
			}
		j=0;
		for (i=0;i<2501;i++)
			if (nums[i] %2 ==1) {
				list[j]=i;
				j++;
			}

		sort(list,list+N-1);
		for (i=0;i<N;i++)
			cout << list[i]<<" " ;
		cout << endl;
	}
	return 0;
}

