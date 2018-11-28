#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool UpdateHSBasedOnNAndCheckIfFull(long N, vector<bool>& hs){
	while(N!=0){
		hs[N%10] = true;
		N/=10;
	}
	for(int i=0;i<hs.size();i++){
		if(hs[i] == false)
			return true;
	}
	return false;
}

int main() {
	// your code goes here
	
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		long N, orig_N, old_N;
		cin>>N;
		orig_N = N;
		cout<<"Case #"<<t+1<<": ";
		if(N==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		vector<bool> hs(10,false);
		bool awake = true;
		while(awake){
			awake = UpdateHSBasedOnNAndCheckIfFull(N, hs);
			old_N = N;
			N+=orig_N;
		}
		cout<<old_N<<endl;
		
	}
	
	return 0;
}
