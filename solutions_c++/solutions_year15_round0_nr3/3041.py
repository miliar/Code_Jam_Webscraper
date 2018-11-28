#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, char> quat;

string g, g1; int m = 1;

quat mult(quat a, quat b) {
    quat t = quat(1, 'x');
    t.first *= a.first*b.first;
    if (a.second == '1' || b.second == '1')
        t.second =  ((a.second == '1') ? b.second : a.second);
    else if (a.second == b.second) {
        t.first *= -1; t.second = '1';
    }
    else if (a.second == 'i' && b.second == 'j')
        t.second = 'k';
    else if (a.second == 'i' && b.second == 'k') {
        t.first *= -1; t.second = 'j';
    } else if (a.second == 'j' && b.second == 'i') {
        t.first *= -1; t.second = 'k';
    } else if (a.second == 'j' && b.second == 'k')
        t.second = 'i';
    else if (a.second == 'k' && b.second == 'i')
        t.second = 'j';
    else {
        t.first *= -1; t.second = 'i';
    }
    
    return t;
}

quat comp(int pos) {
    if (pos == g.length())
        return quat(1, '1');
    return mult(quat(1, g[pos]), comp(pos+1));
}

int main() {
    ifstream cin("stuff.in");
    ofstream cout("stuff.out");
    int min1 = 1000000, min2 = -5000; int t; cin >> t;
    for (int i = 0; i < t; ++i) {
        min1 = 1000000; min2 = -5000;
        int x, l; cin >> x >> l; cin >> g1; g = "";
        for (int j = 0; j < l; ++j)
            g += g1;
        quat t = comp(0);
        if (t != quat(-1, '1')) {
            cout << "Case #" << i+1 << ": NO\n"; continue;
        }
        
        quat t1 = quat(1, '1'), t2 = quat(1, '1');
        for (int i = 0; i < l*x; ++i) {
            t1 = mult(t1, quat(1, g[i]));
            // cout << t1.first << ' '  << t1.second << endl;
            if (t1 == quat(1, 'i')) {
                min1 = i; break;
            }
        }
        
        for (int i = l*x-1; i >= 0; --i) {
            t2 = mult(quat(1, g[i]), t2);
            if (t2 == quat(1, 'k')) {
                min2 = i; break;
            }
        }
        
        cout << "Case #" << i+1 << ((min1 < min2) ? ": YES\n" : ": NO\n");
    }
}
