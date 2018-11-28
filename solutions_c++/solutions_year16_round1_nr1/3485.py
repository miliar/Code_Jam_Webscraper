#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solve(){

}

int main(){
	int R;
	cin >> R;
	string input;
	getline(cin, input);
	for(int i = 0; i < R; i++){
		string output = "";
		getline(cin, input);
		output += input[0];
		for(int j = 1; j < input.length(); j++){
			if(input[j] >= output[0]){
				output.insert(output.begin(), input[j]);
			}
			else{
				output.push_back(input[j]);
			}
		}
		cout << "Case #" << i+1 << ": " << output << endl;
	}

	return 0;
}
