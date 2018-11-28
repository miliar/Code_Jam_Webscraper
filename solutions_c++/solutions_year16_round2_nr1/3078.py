#include <iostream>
#include <ios>
#include <iterator>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

int main(void) {
  ios_base::sync_with_stdio(false);
  //cin.tie(NULL);
  int t, n;
  cin >> t;
  for(int i=1;i<=t;i++) {
  	cout << "Case #" << i << ": ";
  	string anagramm;
  	cin >> anagramm;
  	multiset<char> nagmaram(anagramm.begin(),anagramm.end());
  	multiset<int> digits;
  	while(nagmaram.find('Z')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('Z'));
  		nagmaram.erase(nagmaram.find('E'));
  		nagmaram.erase(nagmaram.find('R'));
  		nagmaram.erase(nagmaram.find('O'));
  		digits.insert(0);
  	}
  	while(nagmaram.find('W')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('T'));
  		nagmaram.erase(nagmaram.find('W'));
  		nagmaram.erase(nagmaram.find('O'));
  		digits.insert(2);
  	}
  	while(nagmaram.find('U')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('F'));
  		nagmaram.erase(nagmaram.find('O'));
  		nagmaram.erase(nagmaram.find('U'));
  		nagmaram.erase(nagmaram.find('R'));
  		digits.insert(4);
  	}
  	while(nagmaram.find('X')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('S'));
  		nagmaram.erase(nagmaram.find('I'));
  		nagmaram.erase(nagmaram.find('X'));
  		digits.insert(6);
  	}
  	while(nagmaram.find('G')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('E'));
  		nagmaram.erase(nagmaram.find('I'));
  		nagmaram.erase(nagmaram.find('G'));
  		nagmaram.erase(nagmaram.find('H'));
  		nagmaram.erase(nagmaram.find('T'));
  		digits.insert(8);
  	}
  	while(nagmaram.find('O')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('O'));
  		nagmaram.erase(nagmaram.find('N'));
  		nagmaram.erase(nagmaram.find('E'));
  		digits.insert(1);
  	}
  	while(nagmaram.find('H')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('T'));
  		nagmaram.erase(nagmaram.find('H'));
  		nagmaram.erase(nagmaram.find('R'));
  		nagmaram.erase(nagmaram.find('E'));
  		nagmaram.erase(nagmaram.find('E'));
  		digits.insert(3);
  	}
  	while(nagmaram.find('F')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('F'));
  		nagmaram.erase(nagmaram.find('I'));
  		nagmaram.erase(nagmaram.find('V'));
  		nagmaram.erase(nagmaram.find('E'));
  		digits.insert(5);
  	}
  	while(nagmaram.find('S')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('S'));
  		nagmaram.erase(nagmaram.find('E'));
  		nagmaram.erase(nagmaram.find('V'));
  		nagmaram.erase(nagmaram.find('E'));
  		nagmaram.erase(nagmaram.find('N'));
  		digits.insert(7);
  	}
  	while(nagmaram.find('N')!=nagmaram.end()) {
  		nagmaram.erase(nagmaram.find('N'));
  		nagmaram.erase(nagmaram.find('I'));
  		nagmaram.erase(nagmaram.find('N'));
  		nagmaram.erase(nagmaram.find('E'));
  		digits.insert(9);
  	}
  	ostream_iterator<int> output(cout,"");
  	copy(digits.begin(),digits.end(),output);
  	cout << endl;
  }
}
