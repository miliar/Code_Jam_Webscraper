//
// Created by Santiago on 08/04/2016.
//

#include <bits/stdc++.h>

using namespace std;

string flip_string(string s, int n) {
    string ans = s;
    for (int i = 0; i <= n/2; ++i) {
        if (s[i] == '-')
            ans[n-i] = '+';
        else
            ans[n-i] = '-';
        if(s[n-i] == '-')
            ans[i] = '+';
        else
            ans[i] = '-';
    }
    return ans;
}

int get_target(string s, int target) {
    for (int i = target-1; i >= 0 ; i--) {
        if(s[i] == '+')
            return i;
    }
    return -1;
}

int get_target(string s) {
    for (int i = s.size()-1; i >= 0 ; i--) {
        if(s[i] == '-')
            return i;
    }
    return -1;
}

int min_flips(string s) {
    int flips = 0;
    int target = get_target(s);
    while (target >= 0) {
        //cout<<"current string"<<s<<endl;
        //cout<<"target "<<target<<endl;
        if(s[0] == s[target]) {
            s = flip_string(s, target);
            target = get_target(s);
        }
        else {
            int next_target = get_target(s, target);
            s = flip_string(s, next_target);
        }
        flips++;

    }
    //cout<<"final flips "<<flips<<endl;
    return flips;
}

int main() {
    freopen("pancakes.in", "r", stdin);
    freopen("pancakes.out", "w", stdout);
    int N;
    cin>>N;
    for (int z = 0; z < N; ++z) {
        string s;
        cin>>s;
        int ans = min_flips(s);
        printf("Case #%d: %d\n", z+1, ans); //Case #5: 3
    }
    return 0;
}