#include <iostream>
#include <algorithm>

using namespace std;

void solve(void){
    int N = 0;
    int P[26] = {};
    int sum = 0;
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> P[i];
        sum += P[i];
    }
    int max = (max_element(P,P+N) - P);
    int current = 0;
    //cout << max << *max_element(P,P+N) << endl;
    
    while (sum > 0){
        if(P[max]*2 <= sum){
            if(P[current] == 0 || current == max){
                current++;
                if(current == N) current = 0;
                continue;
            }
            
            cout.put('A' + current);
            P[current]--;
        } else {
            cout.put('A' + max);
            P[max]--;
        }
        if(sum % 2 == 1){
            cout << " ";
        }
        //cout << sum << " " << max << " " << current << " "<< P[current] << " "<< P[max];
        sum--;
    }
    return;
}

int main() {
    int T = 0;
    cin >> T;
    for(int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}