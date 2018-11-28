#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#define ll long long int

using namespace std;


void revert(bool* a, int i){
	bool temp;
	for(int j=0; j<i/2; j++){
		temp = a[j];
		a[j] = !a[i-j-1];
		a[i-j-1] = !temp;
	}
	if(i%2==1)
		a[i/2] = !a[i/2];
}

void print(bool* a, int l){
	int i = 0;
	for(int i =0; i<l; i++){
		cout<<a[i];
	}
	cout<<endl;
}

void convertS(bool* a, string s){
	for(int i = 0; i< s.length(); i++){
		if(s[i] == '+')
			a[i] = 1;
		else
			a[i] = 0;
	}
}

int main(){
	int t,tt=0,r;
	ll count=0;
	cin>>t;
	string s;
	while(t--){
		count = 0;
		tt++;
		cin>>s;
		int l = s.length();
		bool a[s.length()];
		convertS(a, s);
		// print(a,l);
		for(int i=0; i<l; i++){
			while(a[i] && i<l)
				i++;
			int j = i;
			while(!a[i] && i<l)
				i++;
			if(j==l){
				
			}else if(!j){
				revert(a, i);
				// print(a,l);
				count++;
			}else{
				revert(a,j);
				// print(a,l);
				revert(a,i);
				// print(a,l);
				count+=2;
			}
		}


		// r=1;	
		// while(r){
		// 	cin>>r;
		// 	revert(a,r);
		// 	print(a,l);
		// }	
		cout<<"Case #"<<tt<<": "<<count<<endl;
	}
	return 0;
}