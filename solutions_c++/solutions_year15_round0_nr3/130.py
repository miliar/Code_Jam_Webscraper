#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;

char b[4][4];
int q[4][4];
map <char, int> a;

pair<char,int> mpow(char c, long long n) {
    if (n == 0)
        return make_pair('1', 1);
    if (n % 2 == 1){
        pair<char ,int> tmp = mpow(c, n-1);
        return make_pair(b[a[tmp.first]][a[c]], tmp.second*q[a[tmp.first]][a[c]]);
    }
    else {
        char e = mpow(c, n/2).first;
        return make_pair(b[a[e]][a[e]], q[a[e]][a[e]]);
    }
}


int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    map <int, char> w;
    w[0] = '1';
    w[1] = 'i';
    w[2] = 'j';
    w[3] = 'k';
    a['1'] = 0;
    a['i'] = 1;
    a['j'] = 2;
    a['k'] = 3;
    for (int i=0;i<4;i++){
        q[0][i] = 1;
        q[i][0] = 1;
        b[0][i] = w[i];
        b[i][0] = w[i];
        b[i][i] = '1';
    }
    b[1][2] = 'k';
    b[1][3] = 'j';
    b[2][1] = 'k';
    b[2][3] = 'i';
    b[3][1] = 'j';
    b[3][2] = 'i';
    for (int i=1;i<4;i++)
        for (int j=1;j<4;j++)
            q[i][j] = -1;
    q[1][2] = 1;
    q[2][3] = 1;
    q[3][1] = 1;
    
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        long long l, x;
        string s;
        cin >> l >> x;
        cin >> s;
        if (l*x < 3){
            cout << "NO" << endl;
            continue;
        }
        char zz = 'a';
        int ssn = 1;
        char z = s[0];
        int sn = 1;
        bool f = false, f2 = false;
        for (int i=1;i<l*min(x, 64LL);i++){
            if ((z == 'i') && (sn == 1))
                f = true;
            if ((f) && (sn == 1) && (z == 'k'))
                f2 = true;
            char e = s[i%l];
            sn = sn * q[a[z]][a[e]];
            z = b[a[z]][a[e]];
            if (i+1 == l){
                zz = z;
                ssn = sn;
                //cerr << o+1 << ' ' << i << ' ' << zz << ' ' << ssn << ' ' <<f2 << endl;
            }
        }
        if ((ssn == 1) || ((x % 2) == 0))
            sn = 1;
        else
            sn = -1;
        pair<char, int> tmp = mpow(zz, x);
        z = tmp.first;
        sn *= tmp.second;
        //cerr << o+1 << ' ' << z << ' ' << sn << ' ' <<f2 << endl;
        if ((z != '1') || (sn != -1) || (!f2))
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
    
    return 0;
}