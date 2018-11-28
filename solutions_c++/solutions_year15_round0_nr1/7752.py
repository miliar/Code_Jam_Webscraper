#include<iostream>
#include<string>

using namespace std;

int main(){
	string S;
	
	int T;
	
	cin>>T;
	
	for (int l = 0; l<T; l++){
		
		int Sh;
		cin >> Sh;
		
		cin>> S;
		int count = 0;
		int sum = 0;int k =0;
		for(int i = 0; i< S.length(); i++){
			
			if(S[i] != '0'){
				if(sum < i){
					k = i-sum;
					count = count +k;
					sum = sum +k;
				}
				
				sum = sum +  S[i] - '0';
			}
			
		}
		
		cout<<"Case #"<<l+1<<": "<<count<<"\n";
		
	}
	return 0;
}
