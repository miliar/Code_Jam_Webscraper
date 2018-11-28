#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


#define ll long long int


using namespace std;

void init(bool* arr){
	for(int i=0; i<10; i++)
		arr[i] = 0;
}

void update(bool* arr, ll n){
	ll m = n;
	while(m>9){
		arr[m%10] = 1;
		m = m/10;
	}
	arr[m] = 1;
}

void print(bool* arr){
	for(int i = 0; i < 10; i++){
		cout<<arr[i];
	}
	cout<<endl;
}

bool check(bool* arr){
	for(int i = 0; i < 10; i++){
		if(arr[i]==0)
			return false;
	}
	return true;
}

int main(){
	int t,tt=0;
	ll n;
	cin>>t;
	bool d[10];
	while(t--){
		tt++;
		init(d);
		cin>>n;
		if(n==0){
			cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
			continue;
		}
		ll i = 0;
		while(!check(d)){
			i++;
			update(d,i*n);
			// print(d);
		}
		cout<<"Case #"<<tt<<": "<<i*n<<endl;
	}
	return 0;
}
