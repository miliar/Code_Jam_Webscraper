#include <bits/stdc++.h>

using namespace std;

bool checkAll(int arr [],int size){
	for(int i = 0 ; i < size; i ++){
		if(arr[i] == 0){
			return false;
		}
	}
	return true;
}

int main(){

	int t;
	string  stack;
	cin >> t;
	for(int j = 1; j <= t ; j++){
		cin >> stack;
		char face = stack.at(0);
		unsigned long long count = 0;
		for(int i = 1; i < stack.length(); i++){
			if(stack.at(i) != face){
				face =  stack.at(i);
				count++;
			}
		}
		if(face == '+'){
			cout<<"Case #"<<j<<": "<<count<<endl;
		}
		else{
			cout<<"Case #"<<j<<": "<<count+1<<endl;
		}
	}
	return 0;
}