
#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int k=0; k<t; ++k){
		string s;
		cin >> s;
		deque<char> nowy;
		char pierwszy;
		pierwszy = s[0];
		for(int i=0; i<s.size(); ++i){
			if(s[i]>=pierwszy){
				nowy.push_front(s[i]);
				pierwszy = s[i];
			}
			else{
				nowy.push_back(s[i]);
			}
		}
		string nowy_s;
		for(int i=0; i<s.size(); ++i){
			nowy_s += nowy[i];
		}

		cout << "Case #" << k+1 <<": " <<nowy_s << "\n";

	}


	return 0;
}
