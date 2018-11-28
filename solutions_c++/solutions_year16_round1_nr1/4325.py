#include <iostream>
#include <string>
using namespace std;

string lastword(string& word){
	string  ret = "";
	if (word.size()==0) return "";
    if (word.size()==1) return word;
	if (word[1]>word[0]){
		ret += word[1];
		ret += word[0];
	}
	if (word[0]>=word[1]){
		ret += word[0];
		ret += word[1];
	}
	for(int i=1; i<word.size()-1; i++){
		if (word[i+1]>=ret[0]) {
			ret = word[i+1] + ret;
		}
		else {
			ret = ret + word[i+1];
		}		
	}

	return ret;
}
int main() {
  int numCase;
  cin >> numCase;
 string word;
  for (int i = 1; i <= numCase; ++i) {

	    cin >> word;  // read n.
		cout << "Case #" << i << ": " << lastword(word) << endl;
  }
 return 0;
}