#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(string& seq, int S){
    int n = seq.size();
    vector<int> flips(n+1);
    int flip = 0;
    int cnt = 0;
    for(int i = 0; i < n; ++i){
        flip ^= flips[i];
        int need = (seq[i] == '-')? 1: 0;
        if(need != flip){
            if(i + S <= n){
                cnt += 1;
                flip ^= 1;
                flips[i+S] = 1;
            }else{
                return -1;
            }
        }
    }
    return cnt;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        int S;
        string seq;
        cin >> seq >> S;
        int res = solve(seq, S);
        if(res >= 0){
            cout << "Case #" << t << ": " << res << endl;
        }else{
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

