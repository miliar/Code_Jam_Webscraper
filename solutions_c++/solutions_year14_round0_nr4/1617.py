#include <iostream>
#include <algorithm>
using namespace std;

double blocksN[1000];
double blocksK[1000];

int War(int n){
	int res = n;
	int i = 0, j =0;
	for(; i < n; i++){
		for(; j < n; j++){
			if(blocksK[j] > blocksN[i]){
				res--;
				j++;
				break;
			}
		}
	}
	return res;
}

int DeceitfulWar(double* arr1, double *arr2, int n){
	if(n==1) {
		return arr1[0]<arr2[0]?0:1;
	}
	for(int i = 0; i < n; i++){
		if(arr1[i]>arr2[0])
		{
			for(int j = i+1; j < n; j++){
				arr1[j-1]=arr1[j];
			}
			return DeceitfulWar(arr1,arr2+1,n-1)+1;
		}
	}
	//cout<<arr1[0]<<" fakes and loses: "<<arr2[n-1]<<endl;
	return DeceitfulWar(arr1+1, arr2,n-1);
}

int main(){
	int num;
	cin>>num;
	int resWar[50];
	int resDWar[50];
	for(int k = 0; k <num; k++){
		int N;
		cin>>N;
		for(int i = 0; i < N; i++){
			cin>>blocksN[i];
		}
		for(int i = 0; i < N; i++){
			cin>>blocksK[i];
		}
		sort(blocksN, blocksN+N);
		sort(blocksK, blocksK+N);
		/*for(int i = 0;  i < N; i++){
			cout<<blocksN[i]<<" ";
		}
		cout<<endl;
		for(int i = 0;  i < N; i++){
			cout<<blocksK[i]<<" ";
		}
		cout<<endl;*/
		resWar[k]=War(N);
		resDWar[k]=DeceitfulWar(blocksN, blocksK, N);
	}
	for(int k = 0; k <num; k++){
		cout<<"Case #"<<k+1<<": "<<resDWar[k]<<" "<<resWar[k]<<endl;
	}
	return 0;
}