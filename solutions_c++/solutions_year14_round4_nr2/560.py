#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int iabs(int n){
    if(n < 0) return -n;
    return n;
}

int solve(vector<int>& seq, int N){
    int res = 0;
    for(int i = 0; i < N; i++){
        int pos = min_element(seq.begin(), seq.end()) - seq.begin();
        res += min<int>(pos, seq.size() - pos - 1);
        seq.erase(seq.begin() + pos);
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N;
        cin >> N;
        vector<int> seq(N);
        for(int i = 0; i < N; i++){
            cin >> seq[i];
        }
        int res = solve(seq, N);
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}

