#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
#define N 310


void solve() {
    int n;
    cin >> n;
    int total = 0;
    vector<string> words(n);
    vector<int> ends(n, 0);
    vector<char> chs(110, ' ');
    int p = 0;
    for(int i=0;i<n;i++) {
        cin >> words[i];
    }
    chs[0]=words[0][0];
    for(int i=0;i<words[0].size();i++) {
        if(words[0][i]!=chs[p]){
            chs[++p]=words[0][i];
        }
    }
    int pt = 0;
    for(int i=1;i<n;i++) {
        pt = 0;
        if(words[i][0]!=chs[0]) {
                cout << "Fegla Won\n";
                return;
            }
        for(int pi=1;pi<words[i][pi];pi++) {
            if(words[i][pi]!=chs[pt]) {
                if(words[i][pi]==chs[pt+1])pt++;
                else {
                   cout << "Fegla Won\n";
                    return;
                }
            }
        }
        if(chs[pt+1]!= ' ') {
            cout << "Fegla Won\n";
            return;
        }
    }
    int ln = words[0].size();
    p=0;
    vector<int> times(n);
    while(true){
        char ch = words[0][p];
        int i=p;
        for(;i < ln && ch==words[0][i];i++);
        times[0] = i - p;
        p = i;
        for(int j=1;j<n;j++) {
            for(i=ends[j]; i < words[j].size() && ch == words[j][i]; i++);
            if(i==ends[j]) {
                cout << "Fegla Won\n";
                return;
            }
            times[j] = i - ends[j];
            ends[j] = i;
        }
        sort(times.begin(), times.end());
        int g = times[n>>1];
        for(int si=0;si<n;si++) {
            total += abs(times[si]-g);
        }
        if(p==words[0].size()) {
            cout << total << endl;
            return;
        }
    }
}

int main() {
    int T;
    cin >> T;
    for(int i=1;i<=T;i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}