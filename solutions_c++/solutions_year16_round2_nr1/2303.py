#include <bits/stdc++.h>

using namespace std;

int main() {
    //freopen("1.i", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.ou", "w", stdout);

    int ts;
    cin >> ts;
    string s;
    int d[10];
    int a[100];
    for (int t = 1; t <= ts; t++) {

        cin >> s;
        
        memset(d, 0, sizeof(d));       
        memset(a, 0, sizeof(a));

        for (int i = 0; i < s.length(); i++)
          a[s[i]]++;
//cout  << s << endl;
       // for (int i = 65; i <= 65+26-1; i++) cout << a[i];
       // cout << endl;
        if (a['Z'] > 0) {
          d[0] = a['Z'];
          a['E'] -= a['Z'];
          a['R'] -= a['Z'];
          a['O'] -= a['Z'];
        }

        if (a['W'] > 0) {
          d[2] = a['W'];
          a['T'] -= a['W'];
          a['O'] -= a['W'];
        }

        if (a['U'] > 0) {
          d[4] = a['U'];
          a['F'] -= a['U'];
          a['O'] -= a['U'];
          a['R'] -= a['U'];
        }

        if (a['X'] > 0) {
          d[6] = a['X'];
          a['S'] -= a['X'];
          a['I'] -= a['X'];
        }

        if (a['G'] > 0) {
          d[8] = a['G'];
          a['E'] -= a['G'];
          a['I'] -= a['G'];
          a['H'] -= a['G'];
          a['T'] -= a['G'];
        }

        if (a['O'] > 0) {
          d[1] = a['O'];
          a['N'] -= a['O'];
          a['E'] -= a['O'];
        }

        if (a['T'] > 0) {
          d[3] = a['T'];
          a['H'] -= a['T'];
          a['R'] -= a['T'];
          a['E'] -= a['T'] * 2;
        }

        if (a['F'] > 0) {
          d[5] = a['F'];
          a['I'] -= a['F'];
          a['V'] -= a['F'];
          a['E'] -= a['F'];
        }

        if (a['S'] > 0) {
          d[7] = a['S'];
          a['E'] -= a['S'] * 2;
          a['V'] -= a['S'];
          a['N'] -= a['S'];
        }

        if (a['I'] > 0) {
          d[9] = a['I'];
        }

        cout << "Case #" << t << ": "; 
        for (int i = 0; i < 10; i++)
          if (d[i] > 0)
            for (int j = 0; j < d[i]; j++) cout << i;
        cout << endl;
    }
}
