#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <typeinfo>

using namespace std;

int main(){
	freopen("A-small-attempt3.in", "r", stdin);
  	freopen("out.txt", "w", stdout);
	int cases;
	int count = 0;
	int curr = 1;
	int currLen = 0;
	int people = 0;
	int length; 
	string mystr;
	string dummy;

	cin >> cases;
	getline(cin, dummy);
	
	for(int i = 0; i < cases; i++){
		getline (cin, mystr);
		//cout << mystr << endl;
		//length = mystr.length() - 2;
		for(int j = 2; j < mystr.length(); j++){
			people += mystr[j] - '0';
			currLen +=1;
			if(people + count < currLen){
				count++;
				//people +=1;
			}
		}
		
		cout << "Case #" << curr << ": " << count << endl;
   	    currLen = 0;
   	    curr++;
   	    people = 0;
   	    count = 0;
	}
	return 0;
}
