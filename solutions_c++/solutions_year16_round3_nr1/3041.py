#include <iostream>
#include <string>

using namespace std;

pair<int, int> max(int arr[],int size);
int print(pair<int, int> index, int arr[],int size,int total);

int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		cout << "Case #" << i+1 << ": ";
		int p,sub;
		int total=0;
		cin >> p;
		int arr[p];
		pair<int ,int> indexval;
		for(int j=0;j<p;j++){
			cin >> arr[j];
			total+=arr[j];
		}
		while(total>0){
			indexval=max(arr,p);
			sub=print(indexval,arr,p,total);
			if(sub==3){
				arr[indexval.second]-=1;
				arr[indexval.first]-=1;
				total-=2;
			}
			else{
				arr[indexval.second]-=sub;
				total-=sub;
			}
		}
		cout << endl;
	}
	return 0;
}

pair<int, int> max(int arr[],int size){
	int max=0;
	int nextmax=0;
	for(int i=0;i<size;i++){
		if(arr[max]<=arr[i]){
			nextmax=max;
			max=i;
		}
	}
	return make_pair(nextmax,max);
}

int print(pair<int, int> index, int arr[],int size,int total){
	int k=0;
	if(total==2){
		cout << char(index.second+65) << char(index.first+65);
		k=2;
	}
	else{
		if((total-2)/2 < arr[index.first]){
			if((total-1)/2 < arr[index.first]){
				cout << char(index.second+65) << char(index.first+65) << " ";
				k=3;
			}
			else{
				cout << char(index.second+65) << " ";
				k=1;
			}
		}
		else{
			cout << char(index.second+65) << char(index.second+65) << " ";
			k=2;
		}
	}
	return k;
}