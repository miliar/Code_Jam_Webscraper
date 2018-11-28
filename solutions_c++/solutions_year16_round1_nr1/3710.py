#include <iostream>
#include <sstream>
#include <string>
#include <list>
using namespace std;

int main(){
	int numTest;
	string s;
	getline(cin, s);
	stringstream ss(s);
	ss >> numTest;
	int testNum = 1;

	while(testNum <= numTest){
		getline(cin, s);
		
		cout << "Case #" << testNum << ": ";

		list<char> mylist;
		for(int i = 0; i < s.size(); i++){
			if(s[i] >= mylist.front()){
				mylist.push_front(s[i]);
			} else {
				mylist.push_back(s[i]);
			}
		}

		for(list<char>::iterator it = mylist.begin(); it != mylist.end(); it++){
			cout<<*it;
		}

		cout<<endl;

		testNum++;
	}
}