#include <bits/stdc++.h>

using namespace std;

string s;

int main() {
    int t, t2;
    cin>>t;
    t2 = t;
    while(t--) {
        cout<<"Case #"<<t2-t<<": ";
        cin>>s;
        s+='+';
        int ile = 0;
        for(int i = s.size() - 1; i > 0; i--) {
            if (s[i - 1] != s[i]) {
                ile++;
            }
        }
        cout<<ile<<endl;
    }
    return 0;
}

