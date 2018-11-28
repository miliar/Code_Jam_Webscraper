#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    string line;
    getline(cin, line);
    istringstream iss(line);
    
    int cases;
    iss >> cases;
    
    for (auto i = 1; i <= cases; ++i) {
        string line;
        getline(cin, line);
        istringstream iss(line);
        
        int n;
        iss >> n;
        
        map<int, size_t> heightOccurrence;
        for (auto j = 0; j < 2 * n - 1; ++j) {
            string line;
            getline(cin, line);
            istringstream iss(line);
            for (auto k = 0; k < n; ++k) {
                int h;
                iss >> h;
                heightOccurrence[h] += 1;
            }
        }
        
        std::vector<int> remainHeights;
        for (const auto& p : heightOccurrence) {
            if (p.second % 2 != 0)
                remainHeights.push_back(p.first);
        }
        
        sort(begin(remainHeights), end(remainHeights));
        
        cout << "Case #" << i << ":";
        for (auto h : remainHeights) {
            cout << " " << h;
        }
        cout << "\n";
    }
    
    return 0;
}
