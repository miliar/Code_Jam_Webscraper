#include <iostream>
#include <cstdlib>
using namespace std;

int cmp(const void *, const void *);

int main(){
	int T, N;
	cin >> T;
	for(int i=1;i<=T;i++){
		cin >> N;
		double we0[N], we1[N];
		for (int j=0;j<N;j++)
			cin >> we0[j];
		for (int j=0;j<N;j++)
			cin >> we1[j];
		qsort(we0, N, sizeof(double), cmp);
		qsort(we1, N, sizeof(double), cmp);
		cout << "Case #" << i << ": ";
		int j=0;
		for (int k=N-1;k>=0;k--){
			if (we0[k+j] < we1[k])
				j++;
		}
		

		//while (we0[j] < we1[N-j-1]){
		//	j++;
		//}
		cout << N-j << " ";
		j = 0;
		for (int k=N-1;k>=0;k--){
			if (we0[k] > we1[k+j])
				j++;
		}
		cout << j << endl;
	}
	return 0;
}

int cmp(const void * p, const void * q){
	if (*(double*)p > *(double*)q) return 1;
	else if (*(double*)p < *(double*)q) return -1;
}
