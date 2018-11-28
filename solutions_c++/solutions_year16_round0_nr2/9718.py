#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
	int numTest;
	string s;
	getline(cin,s);
	stringstream ss(s);
	ss >> numTest;
	int testNum = 1;

	while (testNum <= numTest){
		getline(cin, s);
		stringstream sss(s);
		string n;
		sss>>n;
		int flips;

		bool plus = false;
		if (n.at(0) == '-'){
			flips = 1;
		} else {
			flips = 0;
			plus = true;
		}

		cout << "Case #"<<testNum<<": ";
		for(int i = 1; i<n.length(); i++){
			char curchar = n.at(i);
			if (curchar == '-'){
				if (plus == true){
					flips = flips + 2;
					plus = false;
				}
			} else {
				plus = true;
			}
		}
		cout << flips << endl;
		testNum++;
	}
}