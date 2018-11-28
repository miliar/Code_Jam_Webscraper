#include <iostream>
#include <vector>
#include <iterator>
using namespace std;

int main(){
	int T;
	string S;
	cin >> T;
	int I = T;
	while(T--){
		cin >> S;
		cout << "Case #" << I-T << ": ";

		vector<char> v;
		v.push_back(S[0]);
		for(int i=1;i<S.length();i++){
			if(S[i]<v[0])
				v.push_back(S[i]);
			else{
				v.insert(v.begin(),S[i]);
			}
		}

		for(int i=0;i<S.length();i++)
			cout << v[i];

		cout << endl;
	}
}