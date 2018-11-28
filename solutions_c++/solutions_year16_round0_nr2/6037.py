#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int q2(string str){
	int i = 1;
	int ans = 0;
	while(i < str.length()){
		if(str[i-1] != str[i]){
			++ans;
		}
		i++;
	}
	if(str[str.length()-1] == '-'){
		ans ++;
	}

	return ans;
}

int main() {
  int t;
  string str;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> str;
    cout << "Case #" << i << ": " << q2(str) << endl;
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

}
