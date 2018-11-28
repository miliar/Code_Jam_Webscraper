#include <iostream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;
int m, n;
string words[100];
vector<int> all[100];
int ans;
int hwm;
void compu() {
    //cout<<"compu------------------\n";
    int now = 0;
    for (int i = 0; i < n; i++) {
        //cout<<"poj\n";
        set<string> S;
        if (all[i].size() == 0) {
            return;
        }
        for (int pos : all[i]) {
            string s = words[pos];
            //cout<<s<<"\n";
            string pref = "";
            S.insert(pref);
            for (int k = 0; k < s.size(); k++) {
                pref += s[k];
                S.insert(pref);
            }
        }
        now += S.size();
    }

    if (now == ans) {
        hwm++;
    } else if (now > ans) {
        ans = now;
        hwm = 1;
    }
}

void recu(int idx) {
    if (idx == m) {
        compu();
        return;
    }
    for (int i = 0; i < n; i++) {
        all[i].push_back(idx);
        recu(idx + 1);
        all[i].pop_back();
    }
}
int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for (int test = 1; test <= t; test++) {
        cin>>m>>n;
        ans = 0;
        hwm = 0;
        for (int i = 0; i < m; i++) {
            cin>>words[i];
        }
        recu(0);
        cout<<"Case #"<<test<<": "<<ans<<" "<<hwm<<"\n";
    }
    return 0;
}

