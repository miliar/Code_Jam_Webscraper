#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    for(int T=1; T<=t; T++) {
        cout << "Case #" << T <<":";
        int N;
        cin >> N;
        if(N == 2) {
            int a, b;
            cin >> a >> b;
            while(a > b) {
                cout << " A";   a--;    }
            while(b > a) {
                cout << " B";   b--;    }
            while(a > 0 ){
                cout << " AB";  a--;    }
            cout << endl;
            continue;
        }
        vector< pair<int, int> > vec;
        int arr[N];
        for(int i=0; i<N; i++) {
            cin >> arr[i];
            vec.push_back(make_pair(arr[i], i));
        }

    }
}
