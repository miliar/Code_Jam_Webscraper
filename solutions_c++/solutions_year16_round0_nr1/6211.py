#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int i=1; i<=T; i++) {
        cout << "Case #" + to_string(i) + ": ";
        
        int N = 0;
        vector<char> seen;
        cin >> N;
        
        bool keepIterating = true;
        int Name = 1;

        if (N == 0) {
            cout << "INSOMNIA";
        } else {
            int count = 0;
            
            while (keepIterating) {
                count++;
                
                Name = count*N;
                string NString = to_string(Name);

                for (int x=0; x<NString.size(); x++) {
                    if (find(seen.begin(), seen.end(), NString[x]) == seen.end()) {
                        seen.push_back(NString[x]);
                    }
                }
                if (seen.size() == 10) {keepIterating = false;}
            }
            
            cout << Name;
        }
        
        cout << endl;
    }
    
    return 0;
}