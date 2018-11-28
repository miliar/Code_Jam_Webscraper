#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip> 
#include <unordered_map>
using namespace std;

char find_most(unordered_map<char, int> parties_count) {
    int max_count = 0;
    char max_char;
    for (auto i = parties_count.begin(); i != parties_count.end(); i ++) {
	if (i -> second > max_count) {
	    max_count = i -> second;
	    max_char = i -> first;
	 }
    }
    return max_char;
}

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (int i = 0; i < T; i ++) {
	int P;
	cin >> P;
	unordered_map<char, int> parties_count;
	for (int j = 0; j < P; j ++) {
	    int c;
	    cin >> c;
	    parties_count['A' + j] = c;
	}
	
	cout << "Case #" << i + 1 <<":";
	int k = 0; 
	while (parties_count.size() > 0) {
	    // check if there is only two parties with count 1 each
	    if (parties_count.size() == 2) {
	      auto it1 = parties_count.begin();
	      auto it2 = parties_count.begin(); it2 ++;
	      if (it1 -> second == it2 -> second) {
		cout << " " << it1 -> first << it2 -> first;
		it1 -> second --;
		it2 -> second --;
		if (it1 -> second == 0) { 
		  cout << endl;
		  break;
		}
	      }
	    }
	    else {
	      // find party with largest number of senators
	      char c = find_most(parties_count);
	      cout << " " << c;
	      parties_count[c] --;
	      if (parties_count[c] == 0) parties_count.erase(c);
	    }
	}
    }
    return 0;
}
