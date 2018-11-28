#include <iostream>
#include <string>
using namespace std;
int pancakes_arr_func(string str,int size);
int find_min(int arr[],int size);
void reverse_and_toggle(int arr[],int last_index);
int main(){
	int n;
	cin >> n;
	string pancakes[n];
	for(int i=0;i<n;i++){
		cin >> pancakes[i];
	}
	int minimum_switches,size;
	for(int j=0;j<n;j++){
		size=pancakes[j].length();
		minimum_switches=pancakes_arr_func(pancakes[j],size);
		cout << "Case #" << j+1 << ": " << minimum_switches << endl;
	}
	return 0;
}
int pancakes_arr_func(string str,int size){
	int arr[size];
	for(int i=0;i<size;i++){
		if((int)str[i]==43){arr[i]=1;}
		else{arr[i]=0;}
	}
	return find_min(arr,size);
}
int find_min(int arr[],int size){
	int ptr_index=0;
	int switch_count=0;
	int arr_value=arr[0];
	for(int i=0;i<size;i++){
		if(arr_value!=arr[i]){
			ptr_index=i;
			arr_value=arr[i];
			++switch_count;
			reverse_and_toggle(arr,ptr_index);
		}
	}
	if(arr[size-1]==0){++switch_count;}
	return switch_count;
}
void reverse_and_toggle(int arr[],int last_index){
	int temp;
	if(last_index==1){
		arr[last_index-1] = arr[last_index-1]==1 ? 0 : 1;
	}
	else{
		for(int i=0;i<last_index/2;i++){
			arr[i] = arr[i]==1 ? 0 : 1;
			temp=arr[i];
			arr[last_index-1-i] = arr[last_index-1-i]==1 ? 0 : 1;
			arr[i]=arr[last_index-1-i];
			arr[last_index-1-i]=temp;
		}
	}
}