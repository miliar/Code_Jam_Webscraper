#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <deque>
#include <stdlib.h>

using namespace std;

typedef long long int ll;

int main(){
	ll num;
	string n;
	string line;
	getline(cin,line);
	istringstream ss(line);
	ss >> num;

	for (int i = 0; i <= num-1; i++){
		getline(cin,line);
		istringstream ss(line);
		ss >> n;

		string last_word = n.substr(0,1);
		for (int j = 1; j <= n.size()-1; j++){
			string s0,s1,s2;

			s0 = last_word;
			s1 = s0 + n.substr(j,1);
			s2 = n.substr(j,1) + s0;

			if (s1 > s2){
				last_word = s1;
			}
			else{
				last_word = s2;
			}
		}

		cout << "CASE #" << i+1 << ": " << last_word << endl;
	}
}