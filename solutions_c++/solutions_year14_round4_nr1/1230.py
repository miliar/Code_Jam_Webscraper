#include <iostream>
#include <set>

using namespace std;

int main() {
    int T; cin >> T;
    for(int t = 1; t <= T; ++t) {
        int nFiles, size;
        cin >> nFiles >> size;
        multiset<int> files;
        for(int f = 0; f < nFiles; ++f) {
            int file;
            cin >> file;
            files.insert(file);
        }
        
        int res = 0;
        while(!files.empty()) {
            /* take the largest */
            auto largest = files.end(); largest--;
            /* and the largest other file that fits */
            auto smallest = files.upper_bound(size - *largest);
            
            if (smallest == files.begin() || files.size() == 1) {
                /* not small file found */
            } else {
                /* if it suggest taking the biggest element,
                 * we need to take the one before */
                if (smallest == files.end()) {
                    smallest = largest;
                }
                smallest--;
                files.erase(smallest);
            }
            files.erase(largest);
            res++;
        }
        
        cout << "Case #" << t << ": " << res << endl;
    }
}