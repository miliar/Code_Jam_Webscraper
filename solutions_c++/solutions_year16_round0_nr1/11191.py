#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

void quicFunc(string n, int counter, int testCase, int numIndex[], string original);

int main() {
  int t, m;
  int numIndex[10] = {0,0,0,0,0,0,0,0,0,0};
  string n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
   	if(stoi(n) == 0){
   		cout << "Case #" << i << ": " << "INSOMNIA" << endl;
   	}else{
    	quicFunc(n, 1, i, numIndex, n);
    	for(int l=0; l < 10; l++)
    		numIndex[l] = 0;
    }
    //
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}

void quicFunc(string n, int counter, int testCase, int numIndex[], string original){
	bool keepGoing = false;
    for(int i= 0; i < n.length(); i++){
		numIndex[((int)n[i] - '0')] = 1;
		//cout << "found: " << ((int)n[i] - '0') << endl;
    }
/*    for(int k=0; k < 10; k++)
    	cout << numIndex[k] << endl;*/
	for(int j=0; j < 10; j++)
		if(numIndex[j] == 0)
			keepGoing = true;
	
	if(keepGoing){
		counter++;
		quicFunc(to_string(counter*stoi(original)), counter, testCase, numIndex, original);
	}else{
		cout << "Case #" << testCase << ": " << n << endl;
	}
	
}