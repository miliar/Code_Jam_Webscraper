#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>


using namespace std;

int main(){
	int Caso;

	string s;
	string s2;
	cin >> Caso;

	for (int c = 1; c <= Caso; c++){

		cin >> s;
		s2 = "";

		s2 += s[0];
		for (int i = 1; i < s.size(); i++){

			if (s2[0] <= s[i]){
				s2 = s[i] +s2;
			}
			else{
				s2 += s[i];
			}



		}



		cout << "Case #" << c << ": " << s2 << endl;

	}
}