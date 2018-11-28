#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool can_fail(vector<string>& workers, const vector<int>& seq, int i, vector<bool>& taken) {
    if(i >= seq.size())
        return false;
    
    int w = seq[i];
    int c = 0;
    for(int m = 0; m < workers.size(); ++m) {
        if(workers[w][m] == '1' && !taken[m]) {
            c++;
            taken[m] = true;
            bool r = can_fail(workers, seq, i+1, taken);
            taken[m] = false;
            if(r)
                return true;
            
        }
    }
    
    if(c == 0)
        return true;
    
    return false;
}

void solve() {
    int N;
    cin >> N;
    vector<string> workers(N);
    for(int i = 0; i < N; ++i) {
        cin >> workers[i];
    }
    
    /*for(int i = 0; i < workers.size(); ++i) {
        cout << workers[i] << endl;
    }*/
    
    int best = 10000000;
    
    int training = 0;
    while(training < (1 << (N*N))) {
        vector<string> tmp = workers;
        
        bool valid = true;
        int dollars = 0;
        for(int i = 0; i < N*N; ++i) {
            if(training & (1 << i)) {
                int w = i % N;
                int m = i / N;
                
                if(workers[w][m] == '0') {
                    workers[w][m] = '1';
                    dollars++;
                }
                else {
                    valid = false;
                    break;
                }
            }
        }
        
        if(valid) {
            vector<int> seq;
            vector<bool> taken(N, false);
            for(int i = 0; i < N; ++i) seq.push_back(i);
            
            do {
                if(can_fail(workers, seq, 0, taken)) {
                    valid = false;
                    break;
                }
            } while(next_permutation(seq.begin(), seq.end()));
        }
        
        if(valid) {
            best = min(best, dollars);
        }
        
        workers = tmp;
        training++;
    }
    
    cout << best << endl;
}

int main() {
    
    int c = 1;
    int T;
    cin >> T;
    while(T --> 0) {
        cout << "Case #" << c++ << ": ";
        solve();
    }
    
    return 0;
}
