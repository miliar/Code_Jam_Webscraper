#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip> 
#include <unordered_set>
using namespace std;

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (auto i = 0; i < T; i ++) {
	int n;
	cin >> n;
	if (n == 0) {
	  cout << "Case #" << i + 1 << ": INSOMNIA\n";
	  continue;
	}
	unordered_set<int> s;
	int cn = n;
	while (1) {
	    // add all the digits of n to set s
	    int t = n;
	    while (t) {
	      s.insert(t % 10);
	      t /= 10;
	    }
	    
	    // if the set is full, print n and jump out of the loop
	    
	    if (s.size() == 10) {
		cout << "Case #" << i + 1 << ": " << n << endl;
		break;
	    }
	    else {
		// otherwise, increase n and repeat
		n += cn;
	    }
	}
    }
}
