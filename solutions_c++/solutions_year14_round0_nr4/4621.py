#include <iostream>
#include <cstdlib>
using namespace std;

int cmp(const void *, const void *);

int main(){
int T, N;
cin >> T;
	for(int i=1;i<=T;i++){
	cin >> N;
	double arr1[N], arr2[N];
		for (int j=0;j<N;j++)
		cin >> arr1[j];

		for (int j=0;j<N;j++)
		cin >> arr2[j];
	qsort(arr1, N, sizeof(double), cmp);
	qsort(arr2, N, sizeof(double), cmp);
	cout << "Case #" << i << ": ";
	int j=0;
		for (int k=N-1;k>=0;k--){
			if (arr1[k+j] < arr2[k])
			j++;
		}

	cout << N-j << " ";
	j = 0;
		for (int k=N-1;k>=0;k--){
			if (arr1[k] > arr2[k+j])
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
