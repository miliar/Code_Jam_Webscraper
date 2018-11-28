#include <iostream>
using namespace std;

int main(){
  int t;
  cin >> t;
  for (int c = 1; c <= t; c++){
	string s, word;
    cin >> s;
    word = s[0];
	for (int i = 1; i < s.length(); i++){
		if (s[i] >= word[0]){
			word = s[i] + word;
		}
		else{
			word = word + s[i];
		}
	}
	
	cout << "Case #" << c << ": " << (word) << endl;
  }
}
