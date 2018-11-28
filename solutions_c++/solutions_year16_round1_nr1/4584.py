#include <iostream>
#include <vector>

using namespace std;

int main(){
	string input;
	int T;
	vector<char> newString;
	cin>>T;
	for(int z=0; z<T; z++){
		cin>>input;
		newString.push_back(input[0]);
		for(int i=1; i<input.length(); i++){
			if((int)newString[0] <= (int)input[i]){
				newString.insert(newString.begin(), input[i]);
			}
			else
				newString.push_back(input[i]);
		}
		cout<<"Case #"<<z+1<<": ";
		for(int p=0; p<newString.size(); p++){
			cout<<newString[p];
		}
		cout<<endl;
		newString.clear();
	}
	return 0;
}
