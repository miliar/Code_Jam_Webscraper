#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <map>
#include <set>
using namespace std;

int main(){
	long t;
	cin >> t;
	string word;
	vector<char> out = vector<char>(0);

	for(int i = 0; i < t; i++){
		cin >> word;
		out.clear();
		for(int j = 0; j < word.size(); j++){
			if(out.size() == 0){
				out.push_back(word[j]);
			} else if(word[j] >= out[0]){
				out.insert(out.begin(), word[j]);
			} else {
				out.push_back(word[j]);
			}
		}



		cout << "Case #" << i+1 << ": ";
		for(int k = 0; k < out.size(); k++){
			cout << out[k];
		}
		cout << endl;
	}
	return 0;
}