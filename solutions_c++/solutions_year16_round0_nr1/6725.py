#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large_output.txt", "w", stdout);
    int t;
    cin >> t;
    int tc = 1;
    while(t--) {
        int n;
        cin >> n;
        set<int> s;
        for(int i = 1; i <= 1000000; i++) {
            int temp = i*n;
            while(temp != 0) {
                s.insert(temp%10);
                temp = temp/10;
            }
            if(s.size() == 10) {
                cout << "Case #"<<tc<<": " << (i *n) << endl;
                break;
            }

        }
        if(s.size() < 10) {
            cout << "Case #"<<tc<<": " << "INSOMNIA" << endl;
        }
        s.clear();
        tc++;
    }

    return 0;

}
