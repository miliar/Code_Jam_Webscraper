#include <iostream>

using namespace std;

int arr[1001];

int getMax(){
	for(int i=1000; i>=0;i--){
		if(arr[i] > 0){
		return i;
		}
	}
	return -1;
}

int minOf(int a,int b){
	if(a < b)return a;
	return b;
}

int bestArr(){
	int m = getMax();
	if(m == 0 || m == -1)return 0;
	if(m==1)return 1;

	int minVal = m;
	
	for(int j=1;j<=m/2;j++){
		int c = arr[m];
		arr[j] += c;
		arr[m-j] += c;
		arr[m] = 0;
		minVal = minOf(minVal,bestArr()+c);
		arr[j] -= c;
		arr[m-j] -= c;
		arr[m] = c;
	}
	return minVal;
}

int main(void){

	freopen("B-small5.in", "r", stdin);
	freopen("b5.out", "w", stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int n;
		cin>>n;
		for(int i=0;i<=1000;i++){
			arr[i] = 0;
		}
		for(int i=0;i<n;i++){
			int x;
			cin>>x;
			arr[x]++;
		}
		printf("Case #%d: %d\n", t+1, bestArr());

	}

}