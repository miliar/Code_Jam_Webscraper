#include<iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int iit=1; iit<=t; iit++){
		string n;
		cin>>n;
		int l = n.length();
		char prev = n[0];
		int changes = 0;
		for(int i=1; i<l; i++){
			if(n[i] != prev) changes++;
			prev = n[i];
		}
		if(n[l-1] == '-') changes++;
		cout<<"Case #"<<iit<<": "<<changes<<endl;
	}
	
	return 0;
}
