#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        
        cout << "Case #" << tc + 1<< ": ";
        int n;
        cin >> n;
        bool failed = false;
        vector <string> a(n);
        vector <int> trk(n, 0);
        string proto;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        proto.push_back(a[0][0]);
        for (int i = 1; i < a[0].length(); i++)
            if (a[0][i] != a[0][i-1])
                proto.push_back(a[0][i]);
        int sol = 0;
        //cout << proto << " ";
        for (int i = 0; i < proto.length(); i++) {
            int count = 0;
            vector <int> cnt(n, 0);
            for (int j = 0; j < n; j++) {
                if (a[j][trk[j]] != proto[i]) {
                    failed = true;
                    break;
                }
                else {
                    
                    for ( ;a[j][trk[j]] == proto[i]; trk[j]++) {
                        cnt[j]++;
                        count++;
                    }
                }
            }
            if (failed)
                break;
            int avg = round((double)count / (double)n);
            for (int j = 0; j < n; j++) {
                sol += abs(cnt[j] - avg);
            }
        }
        for (int i = 0; i < n; i++)
            if(trk[i] != a[i].length())
                failed = true;
        if (!failed)
            cout << sol << endl;
        else
            cout << "Fegla Won" << endl;
    }
    return 0;
}