#include <iostream>
#include <string>
#include <vector>
using namespace std;
void flip(string &store,int l){
	char temp;
	for(int i=0;i<l;i++){
		if(store[i]=='+'){
			store[i]='-';
		}
		else{
			store[i]='+';
		}
	}
	for(int i=0;i<l/2;i++){
		temp=store[i];
		store[i]=store[l-i-1];
		store[l-1-i]=temp;
	}
}
int main(){
	int t,right,counter,j,left,k;
	string store;
	cin>>t;
	for(int i=0;i<t;i++){
		counter=0;
		cin>>store;
		while(1){
				left=0;
				right=store.size();
				j=0;k=0;
				while(store[k]=='+' && k<store.size()){
					left++;
					k++;
				}
				if(left==store.size()){
					cout<<"Case #"<<i+1<<": "<<counter<<endl;
					break;
				}
				flip(store,left);
				if(left>0){	
					counter++;
				}
				while(store[store.size()-j-1]=='+' && j<store.size()){
					right--;
					j++;
				}
				if(right==0){
					cout<<"Case #"<<i+1<<": "<<counter<<endl;
					break;
				}
				flip(store,right);
				if(right>0){
					counter++;
				}
		}
	}
}
