#include <iostream>
using namespace std;

int main() {
	
	int test,smax;
	string s;
	
	cin>>test;
	
	for(int t=1;t<=test;t++){
		
		cin>>smax;
		cin>>s;
		
		int aud = s[0] - 48;
		int friends = 0;
		for(int i=1;i<=smax;i++){
			
			if( (s[i] - 48) == 0 ){
				continue;
			}	
			
			if(aud >= i){
				aud += (s[i] - 48);
				continue;
			}
					
			
			
			
			friends += (i - aud);
			aud += s[i] - 48 + i - aud;
			
		}
		cout<<"Case #"<<t<<": "<<friends<<"\n";
	}
	
	return 0;
}