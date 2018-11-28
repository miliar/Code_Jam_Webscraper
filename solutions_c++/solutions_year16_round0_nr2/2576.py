#include <iostream>
#include <string>

using namespace std;

int main(){
	int t, count=0; cin>>t;
	string S; 


	for (int q=1; q<=t; ++q){
		cin>>S; count = 0;

		for (int j=1; j<S.size(); ++j){
			if (S[j] != S[j-1]) ++count;
		}

		if (S[S.size()-1] == '-') ++count;

		cout<<"Case #"<<q<<": "<<count<<endl;
	}
	return 0;
}