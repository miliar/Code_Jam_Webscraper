//
// Created by Xuren Zhou on 8/4/2017.
//

#include <iostream>
#include <vector>

using namespace std;


int oversizedPancake(string s, int k) {
    int res = 0;
    vector<int> v(s.length());

    for(int i=0; i < v.size(); i++) {
        if(s[i] == '-')
            v[i] = 1;
        else
            v[i] = 0;
    }

    for(int i=0; i <= s.length() - k; i++) {
        if(v[i] == 1) {
            res ++;
            for(int j=0; j < k; j++) {
                v[i+j] = (v[i+j]+1)%2;
            }
        }
    }

    for(int i=s.length() - k +1; i < s.length(); i++) {
        if (v[i] == 1) {
            res = -1;
            break;
        }
    }

    return res;

}

int main() {
    int t;
    cin >> t;
    for(int i=1; i <= t; i++) {
        string s;
        int k;
        cin >> s >> k;
        int res = oversizedPancake(s, k);
        cout << "Case #" << i << ": ";
        if(res >= 0)
            cout << res;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}
