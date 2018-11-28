#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long long unsigned llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
int main() {
    int t;
    string s;
    cin>>t;
    for(int i = 1; i <= t; ++i) {
        cin>>s;
        int count = 0;
        char prev = s[0];
        if(s[0] == '-')
            ++count;
        for(int j = 1; j < s.length(); ++j) {
            if(s[j] == '-') {
                if(prev == '+')
                    count += 2;
            }
            prev = s[j];
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}

