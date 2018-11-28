#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int N;
    cin >> N;
    
    vector<int> senators(N, 0);
    for(int i = 0; i < N; ++i)
        cin >> senators[i];
    
    if(N == 2) {
        while(senators[0] != senators[1]) {
            if(senators[0] > senators[1]) {
                cout << " A";
                senators[0]--;
            }
            else {
                cout << " B";
                senators[0]--;
            }
        }
        while(senators[0] > 0) {
            cout << " AB";
            senators[0]--;
            senators[1]--;
        }
    }
    else {
        int s = 0;
        for(int i = 0; i < N; ++i)
            s += senators[i];
        
        while(s > 2) {
            int most = 0;
            for(int i = 1; i < N; ++i) {
                if(senators[i] > senators[most])
                    most = i;
            }
            
            cout << " " << static_cast<char>('A' + most);
            senators[most]--;
            s--;
        }
        cout << " " << static_cast<char>('A' + N - 2) << static_cast<char>('A' + N - 1);
    }
    
    cout << endl;
}

int main() {
    
    int c = 1;
    int T;
    cin >> T;
    while(T --> 0) {
        cout << "Case #" << c++ << ":";
        solve();
    }
    
    return 0;
}
