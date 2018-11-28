#include <iostream>
#include <string>
using namespace std;

int main(){
	int ntest;
	cin>>ntest;
	for (int i=1; i<=ntest; i++){
		int n;
		cin>>n;
		int standing = 0;
		int friends = 0;
		string str;
		cin>>str;
		for(int j=0; j<str.length(); j++){
			int s;
			s = str[j]-'0';
			if (standing>=j){
				standing += s;
			}
			else if(s>0){
				int extra = j-standing;
				friends += extra;
				standing += s + extra;
			}
		}
		cout<<"Case #"<<i<<": "<<friends<<endl;
	}
}
