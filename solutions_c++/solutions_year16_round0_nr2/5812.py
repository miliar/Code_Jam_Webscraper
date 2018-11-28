#include <bits/stdc++.h>

using namespace std;

map <string, int> cache;
map <int, string> seq;
map <string, int> id;
map <string, int> previ;

bool is_happy(string st) {
    for(int i=0;i<st.length();i++) {
        if(st[i] == '-') {
            return false;
        }
    }
    return true;
}

string flip (string st, int firstn) {
    string n = st;
    int k = 0;
    for(int i=firstn-1;i>=0;i--) {
        n[k] = (st[i] == '-') ? '+' : '-';
        k++;
    }
    for(int i=firstn;i<st.length();i++) {
        n[k] = st[i];
        k++;
    }
    return n;
}

int solve (string str) {
    int steps = 0;
    while(!is_happy(str)) {
        steps++;
        if(str[0] == '-') {
            int i=0;
            while(i<str.length() && str[i] == '-') {
                i++;
            }
            str = flip(str, i);
        }
        else {
            int i=0;
            while(i<str.length() && str[i] == '+') {
                i++;
            }
            str = flip(str, i);
        }
    }
    return steps;
}

int main()
{
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        string str;
        cin >> str;
        cache.clear();
        cout << "Case #" << t << ": " << solve(str) << endl;
        /*cout << "how it got solved: ";
        vector <string> steps;
        string p = str;
        for(int i=0;i<p.length();i++)
            p[i] = '+';
        while(p != str) {
            steps.push_back(p);
            int idd = previ[p];
            p = seq[idd];
        }
        reverse(steps.begin(),steps.end());
        for(int i=0;i<steps.size();i++) {
            cout << steps[i] << " / ";
        }
        cout << endl;*/
    }
    return 0;
}
