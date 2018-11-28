#include<bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    int cas = 1;
    while (t--) {
        cout << "Case #" << cas << ": ";
        cas++;
        string a;
        cin >> a;
        int in = (a[0] == '-');
        int no = 0;
        for (int i = 1; i < a.size(); ++i) {
            if (a[i] != a[i - 1]) ++no;
        }
        
        if ((no + in)%2) ++no;
        cout << no << endl;
    }
}