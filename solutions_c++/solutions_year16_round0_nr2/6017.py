#include <bits/stdc++.h>
using namespace std;

int PLUS = 0;
int MINUS = 1;

char ch[2] = {'+', '-'};

bool check(string st) {
    int cnt = 0;
    for(size_t i = 0; i < st.size(); i++) {
        if(st[i] == '+') cnt++;
    }
    if(cnt == int(st.size())) return true;
    else return false;
}

std::string flip(string st) {
    int ase, hobe;

    if(st[0] == ch[PLUS]) {
        ase = PLUS;
        hobe = (ase + 1) % 2;
    } else {
        ase = MINUS;
        hobe = (ase + 1) % 2;
    }

    for(size_t i = 0; i < st.size(); i++) {
        if(st[i] == ch[ase]) {
            st[i] = ch[hobe];
        } else {
            break;
        }
    }
    return st;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-out.txt", "w", stdout);
    ios_base::sync_with_stdio(false); cin.tie(0);
    int test;
    cin >> test;
    for(int tc = 1; tc <= test; tc++) {
        string st;
        cin >> st;
        //cout << st << endl;
        int cnt = 0;
        while(!check(st)) {
            st = flip(st);
            //cout << st << endl;
            cnt++;
        }
        cout << "Case #" << tc << ": " << cnt << "\n";
    }
    return 0;
}
