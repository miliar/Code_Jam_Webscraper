#include <iostream>
#include <string>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        int slevel;
        string ppl;
        cin >> slevel >> ppl;
        
        int pplSum = 0;
        int toInvite = 0;
        for (int x = 0; x <= slevel; x++) {
            int withLevel = ppl[x] - 48;
            if (withLevel > 0) {
                if (pplSum >= x)
                    pplSum += withLevel;
                else {
                    toInvite += (x - pplSum);
                    pplSum += withLevel + (x - pplSum);
                }
            }
        }
        
        cout << "Case #" << i << ": " << toInvite << endl;
    }
}
