#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int f(vector<int>& x){
    int n = int(x.size());
    int sol = 0;
    for(int i = n - 1; i >= 0; i--){
        if(x[i] == 0){
            if(x[0] == 1){
                for(int j = 0; j < i and x[j] == 1; j++) x[j] = 0;
                sol++;
            }
            for(int j = 0; j <= i; j++) x[j] = 1 - x[j];
            reverse(x.begin(), x.begin() + i + 1);
            sol++;
        }
    }
    return sol;
}

int main(){
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        string s;
        cin >> s;
        vector<int> x;
        for(auto& c : s) x.push_back(c == '+' ? 1 : 0);
        cout << "Case #" << tc << ": " << f(x) << '\n';
    }
}
