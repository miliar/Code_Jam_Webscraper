#include <bits/stdc++.h>
using namespace std;

int t, sol;
string s;

int main() {
    cin>>t;

    for(int test=1; test<=t; test++) {
        cin>>s;

        sol = 0;

        for(int i=0; i<s.size(); i++) {
            if(i == 0 || s[i] == s[i-1])
                continue;
            sol++;
        }
        sol += (s[s.size()-1] == '-');
        cout<<"Case #"<<test<<": "<<sol<<"\n";
    }

    return 0;
}
