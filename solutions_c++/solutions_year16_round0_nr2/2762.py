#include<bits/stdc++.h>
using namespace std;

int main(){
	int Test;
	cin>>Test;
	string cad;
	for(int test=1; test<=Test; test++){
		cin>>cad;
		cad+='+';
		int cnt=0;
		for(int i=1; i<cad.size(); i++){
			if(cad[i-1]!=cad[i]) cnt++;
		}
		cout<<"Case #"<<test<<": "<<cnt<<"\n";
	}
	return 0;
}
