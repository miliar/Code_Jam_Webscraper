#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

typedef long long mlong;
int main(int argc, char **argv) {
    int T;
    cin >> T;
    string S;
    getline (cin, S);
    for (auto i = 0; i < T; i ++) {
	string w;
	getline (cin, S);
	for (char c:S) {
	  // if the character is smaller than current head, add to the tail
	  if (w.empty() || c < w.front()) w.push_back(c);
	  // otherwise, add to the head
	  else w.insert(0, 1, c);
	}
	cout << "Case #" << i + 1 << ": " << w << endl;
    }
}
