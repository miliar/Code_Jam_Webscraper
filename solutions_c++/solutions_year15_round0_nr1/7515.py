#include <iostream>
#include <string>

using namespace std;

int chToInt(char cc){
	return (int)cc - (int)('0');
}

int main(){
	int T;
	cin>>T;
	for(int i=0; i<T; i++){
		int s; string str;
		int counter = 0;
		int avail = 0;
		cin>>s>>str;
		for(int j=0; j<=str.length(); j++){
			//cout<<"bla "<<j<<endl;
			for(int k=0; k<chToInt(str[j]); k++){
				if(j > avail){ 
					int temp = j-avail;
					counter += temp; 
					avail+=temp + 1; 
				} else{
					avail++;
				}
				//cout<<j<<" "<<avail<<" "<<counter<<endl;
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<counter<<endl;
	}
	return 0;
}