#include <iostream>
#include <string>
#include <algorithm>
typedef long long LL;
using namespace std;

const int MAXN = 10000 + 10;

int main () {
	int cases;
	cin >> cases;

	for (int tc = 1; tc <= cases; tc ++) {
	    cout << "Case #" << tc << ": ";
        string pancakes;
        cin >> pancakes;
        int flips = 0;
        for (int j = pancakes.size() - 1; j >= 0; --j) {
            if (pancakes[j] == '-') {
                flips += 1;
                for (int k = 0; k <= j; k ++) 
                    pancakes[k] = pancakes[k] == '-' ? '+' : '-';
            }
        }
        cout << flips << endl;
    }
}
