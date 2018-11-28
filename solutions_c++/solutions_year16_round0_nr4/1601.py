#include <bits/stdc++.h>
#define MAXN 100002
#define INF 1000000
using namespace std;
typedef long long ll;
typedef int char_32;
int k = 1, deep = 2;
string s, to;
string f(string sn, int deep) {

    string new_s;

    for(int i = 0; i < sn.length(); ++i) {
        if(s[i] == '0') {
            new_s.append(to);
        }
        else new_s.append(s);
    }

    if(deep == 2) {
        return new_s;
    }
    else return f(new_s, deep - 1);

}

int main() {
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, k, c, s; cin >> t;
    for(int z = 1; z <= t; ++ z) {
    cin >> k >> c >> s;

    cout << "Case #" << z << ": ";
    if(k == 1) {
        cout << 1 << endl;
        continue;
    }
    for(int j = 0; j < s; ++j) {
        if(j) cout << " ";
        if(c == 1) cout << j + 1;
        else cout << j + 2;
    }
    cout << endl;
    }
    /*
    cin >> k >> deep;
    for(int i = 0; i < k; ++i) to.append("0");
    for(int mask = 0; mask < (1 << k); mask+=1) {
        s.clear();
        for(int i = 0; i < k; ++i) {

            if(mask & (1 << i)) s.append("1");
            else s.append("0");

        }
        //cout << s << ": ";
        if(deep == 1) cout << s << endl; else
        cout << f(s, deep) << endl;

    }
    */



}
