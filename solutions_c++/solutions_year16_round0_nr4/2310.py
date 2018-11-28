#include <iostream>

using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ":";
		int k, c, s;
		cin>> k>> c>> s;
		for(int j=0;j<k;j++) cout<< " "<< j+1;
		cout<< endl;
	}
}
