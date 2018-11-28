#include<iostream>
#include<list>
#include<string>
using namespace std;
string generateList(string &s){
	int len = s.length();
	list<char> result;
	for(int i=0;i<len;i++){
		if(result.empty() || result.front() <= s.at(i)){
			result.push_front(s.at(i));
		}else{
			result.push_back(s.at(i));
		}
	}

	string res;
	for(list<char>::iterator it = result.begin(); it != result.end(); it++){
		res.push_back(*it);
	}

	return res;
}


int main(void) {
    /* number of test cases */
    unsigned int t;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
	string s;
	cin>>s;
	cout << "Case #" << i << ": " << generateList(s) << endl;
    }

    return 0;
}