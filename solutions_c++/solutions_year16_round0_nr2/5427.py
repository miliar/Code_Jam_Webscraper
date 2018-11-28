#include <iostream>
using namespace std;
int main(){
	int num_cases;
	cin>>num_cases;
	for(int i=1;i<=num_cases;i++){
		string s;
		cin>>s;
		int count = 0;
		char curr = s[0];
		for(int j=1;j<s.length();j++){
			if(s[j-1]!=s[j]){
				count++;
				curr=s[j];
			}
		}
		if(curr=='-'){
			count++;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}