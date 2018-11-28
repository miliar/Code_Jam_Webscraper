#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int N, K;
    cin >> N >> K;
    
    vector<double> p(N);
    for(int i = 0; i < N; ++i)
        cin >> p[i];
        
    vector<bool> choose(N, false);
    for(int i = 0; i < K; ++i)
        choose[i] = true;
    
    sort(choose.begin(), choose.end());
    
    double best = 0;
    do {
        double prob = 0;
        
        vector<int> chosen;
        for(int i = 0; i < N; ++i) {
            if(choose[i])
                chosen.push_back(i);
        }
        
        vector<bool> on(K, false);
        for(int i = 0; i < K/2; ++i) on[i] = true;
        sort(on.begin(), on.end());
        
        do {
            double m = 1;
            for(int i = 0; i < K; ++i) {
                if(on[i])
                    m *= p[chosen[i]];
                else
                    m *= 1 - p[chosen[i]];
            }
            prob += m;
        } while(next_permutation(on.begin(), on.end()));
        
        best = max(best, prob);
    } while(next_permutation(choose.begin(), choose.end()));
    
    cout << best << endl;
}

int main() {
    
    cout.precision(17);
    
    int c = 1;
    int T;
    cin >> T;
    while(T --> 0) {
        cout << "Case #" << c++ << ": ";
        solve();
    }
    
    return 0;
}
