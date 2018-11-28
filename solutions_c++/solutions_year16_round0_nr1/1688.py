#include <iostream>
using namespace std;
int last_number(int n,int index);
int update_arr(int arr[],int n,int index);
int main(){
	int n;
	cin >> n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin >> arr[i];
	}
	for(int j=0;j<n;j++){
		if(arr[j]==0){
			cout << "Case #" << j+1 <<  ": " << "INSOMNIA" << endl;
		}
		else{
			cout << "Case #" << j+1 <<  ": " << last_number(arr[j],1) << endl;
		}
	}
	return 0;
}
int last_number(int n,int index){
	int arr[10],arr_sum=0;
	for(int i=0;i<10;i++){
		arr[i]=0;
	}
	while(arr_sum!=10){
		arr_sum+=update_arr(arr,n,index);
		index++;
	}
	return n*(index-1);
}
int update_arr(int arr[],int n,int index){
	int x=n*index;
	int i=0;
	while(x!=0){
		if(arr[x%10]!=1){
			arr[x%10]=1;
			i++;
		}
		x/=10;
	}
	return i;
}