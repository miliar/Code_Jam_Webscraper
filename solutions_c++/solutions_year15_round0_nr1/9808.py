#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
 
using namespace std;

int main(){
	int T;
	string S;
	int max;
	
	cin>>T;
	for(int t=1; t<=T; t++){
		int current=0;
		int ans=0;
		cin>>max;
		cin>>S;
		for(int i=0; i<=max; i++){
			int people=S[i]-'0'; //convert to integer
			if(current>=i){
				current+=people;
			}
			else{
				if(people!=0){
					ans+=i-current;
					current+=ans+people;
				}
			}
		}
	
		//output case
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}