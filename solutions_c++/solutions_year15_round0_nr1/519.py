#include <bits/stdc++.h>
using namespace std;

int main() {
    
    ifstream cin("testA.in");
    ofstream cout("testA.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        int n; cin >> n; ++n;
        string A; cin >> A;
        vector<int> shyness(n, 0);
        for(int i = 0; i < n; ++i)
            shyness[i] = A[i] - '0';
        
        cout << "Case #" << t_case << ": ";

        for(int newComers = 0; newComers <= 1000; ++newComers) {
            vector<int> tmp = shyness;
            tmp[0] += newComers;
            bool ok = true;
            for(int i = 1; i < n; ++i)
                if(tmp[0] >= i) 
                    tmp[0] += tmp[i];
                else
                    ok = false;
            if(ok) {
                cout << newComers << "\n";
                break;
            }
        }
    }
}
