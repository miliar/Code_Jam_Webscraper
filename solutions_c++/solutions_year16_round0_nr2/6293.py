#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int i=0; i<T; i++) {
        cout << "Case #" + to_string(i+1) + ": ";
        
        string pancakes;
        cin >> pancakes;
        vector<char> indicator;
        copy(pancakes.begin(), pancakes.end(), back_inserter(indicator));
        
        int flips = 0;
        bool keepGoing = true;
        
        while (keepGoing) {
            int negativePos = find(indicator.begin(), indicator.end(), '-') - indicator.begin();
            if (negativePos >= indicator.size()) {
                keepGoing = false;
            } else {
                for (int z=indicator.size()-1; z>=0; z--) {
                    if (indicator[z] == '-') {
                        for (int x=0; x<=z; x++) {
                            if (indicator[x] == '-') {
                                indicator[x] = '+';
                            } else {
                                indicator[x] = '-';
                            }
                        }
                        
                        flips++;
                        break;
                    }
                }
            }
        }
        
        cout << to_string(flips) << endl;
    }
    
    return 0;
}