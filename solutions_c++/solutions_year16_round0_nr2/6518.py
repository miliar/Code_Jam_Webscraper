#include "codejam.h"
#include "iostream"
#include "algorithm"
#include "cstring"

using namespace std;

typedef long long ll;

const size_t LIMIT = 800+5;
string pancakes;

bool read_input(/* arguments */) {
	/* code */
	if(cin >>pancakes) {
        return true;
    }
    return false;
}

string solve(/* arguments */) {
	/* code */
    int flip{0};
    char prev = '*';
    for(char cake : pancakes) {
        if(cake == '-' and cake != prev) {
            flip++;
            if(prev == '+') {
                flip++;
            }
        }
        prev = cake;
    }
	return to_string(flip);
}
