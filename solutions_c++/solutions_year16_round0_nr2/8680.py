#include <iostream>
#include <string>
using namespace std; 
int main() {
  int t, n, m;
  cin >> t; cin.ignore(INT_MAX,'\n');
  for (int i = 1; i <= t; ++i) {
  	string input;
    getline(cin, input);
    int minpos=0, minneg=0;
    for(char& ch:input){
    	if(ch=='+'){
    		minneg = minpos+1;
		}else{
			minpos = minneg+1;
		}
	}
    cout << "Case #" << i << ": " << minpos << endl;
  }
  return 0;
}
