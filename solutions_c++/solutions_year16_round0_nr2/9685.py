#include <bits/stdc++.h>

using namespace std;

bool check (string &x){

	for (int i=0;i<x.size();++i){
		if (x[i]=='-') return true;
	}
	
	return false;
}

int main(){
	int t;
	cin>>t;
	int casos=1;
	while (t--){
	
		printf("Case #%d: ",casos++);
		string x;
		cin>>x;
		
		int flips=0;
		
		while (check(x)){
			flips++;
			
			char flipper;
			flipper=x[0];
			for (int i=0;i<x.size();++i){
				if (x[i]!=flipper) break;
				
				if (flipper=='+'){
					x[i]='-';
				}else{
					x[i]='+';
				}
			}
		}
		
		printf("%d\n",flips);
	}
	
	return 0;
}
