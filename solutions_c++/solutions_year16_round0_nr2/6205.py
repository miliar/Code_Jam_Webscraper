#include <cstdio>
#include <iostream>

#define REP(i,a,b) for (int i = int(a); i < int(b); ++i)

using namespace std;

int main() {
    int numCases, caseNum = 1;
    int flips;
    string pancks;
    
    scanf("%d", &numCases);
    
    while (numCases--) {
        cin >> pancks;
        
        flips = 0;
        
        for (int i = pancks.size(); i >= 0; --i) {
            if (pancks[i] == '-') {
                ++flips;
                for (int j = i - 1; j >= 0; --j) {
                    if (pancks[j] == '-') {
                        pancks[j] = '+';
                    } else {
                        pancks[j] = '-';
                    }
                }
            }
        }
        
        printf("Case #%d: %d\n", caseNum++, flips);
    }
    
    return 0;
}
