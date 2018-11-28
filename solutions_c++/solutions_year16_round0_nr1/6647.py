#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    unsigned int n;
    ios::sync_with_stdio(false);
    
    cin >> n;
    for (int i = 0; i < n; i++) {
	unsigned int k;
	unsigned int flg = 0;
	unsigned int last;
	
        cin >> k;
	if (k == 0) {
	    cout << "Case #" << i+1 << ": INSOMNIA" << endl;
	    continue;
	}
	
	last = k;
	do {
	    unsigned int tmp = last;
	    do {
		flg |= 1 << (tmp % 10);
		tmp /= 10;
	    } while (tmp != 0); 
	    last += k;
	} while (flg != 1023);
	last -= k;
        cout << "Case #" << i+1 << ": " << last << endl;
    }
    return 0;
}