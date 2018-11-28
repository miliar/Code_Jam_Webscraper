#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector<int> VI;

const LL MAX_VAL = 100000000000000L;

bool stackOk(VI& stack) {
    bool ok = true;
    for (auto v : stack) ok &= v > 0;
    return ok;
}

void reverseStack(VI& stack, int lastIdx) {
    VI nstack(stack);
    for (int i = 0; i <= lastIdx; ++i) nstack.at(i) = -stack.at(lastIdx - i);
    swap(stack, nstack);
}

int main() {
	int count;
	cin >> count;
    
	//process test cases
	for (int tc = 1; tc <= count; ++tc) {
        int result = 0;
        
        string pancakes;
        cin >> pancakes;
        
        VI stack;
        stack.reserve(pancakes.size());
        for (auto p : pancakes) stack.push_back( p == '+' ? 1 : -1 );
        
        while ( !stackOk(stack) ) {
            int lastMinusIdx = -1;
            for (int i = 0; i < stack.size(); ++i) if (stack.at(i) < 0) lastMinusIdx = i;
            int longestPlusIdx = -1;
            for (int i = 0; i < lastMinusIdx && stack.at(i) > 0; ++i) longestPlusIdx = i;
            
            if (lastMinusIdx > -1) {
                if (longestPlusIdx > -1) {
                    ++result;
                    reverseStack(stack, longestPlusIdx);
                }
                ++result;
                reverseStack(stack, lastMinusIdx);
            }
        }
        
        cout << "Case #" << tc << ": " << result << endl;
	}

	return 0;
}
