#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    string s;
    ios::sync_with_stdio(false);
    
    cin >> s;
    int n = atoi(s.c_str());
    for (int i = 0; i < n; i++) {
	string slm;
        cin >> slm >>  s;
	
	int lm = atoi(slm.c_str());
	int nadd = 0;
	int total = 0;
	for (int j = 0; j <= lm; j++) {
	    int numPeople = (int)(s[j] - '0'); 
	    if (total >= j) {
		total += numPeople;
	    }
	    else {
		nadd += j - total;
		total += numPeople + (j - total);
	    }
	}
      
        cout << "Case #" << i+1 << ": " << nadd << endl;
    }
    return 0;
}