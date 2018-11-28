#include <iostream>
#include <string>

using namespace std;

typedef long long int ll;

int main(){
	int t,T;
	cin>>T;
	for(t=1;t<=T;t++){
		string S;
		ll i,flips = 0;
	
		cin>>S;
	
		for(i=S.length()-1;i>=0;i--){
			// if even flips till now and current pankake == - or
			// odd flips till now and current pancake == + 
			if((!(flips%2) && (S[i]=='-')) || ((flips%2) && (S[i]=='+')))
				flips++;
		}
		cout<<"Case #"<<t<<": "<<flips<<endl;
	
	}
return 0;
}
