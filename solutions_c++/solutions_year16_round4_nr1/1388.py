#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>

using namespace std;

int t, n, a, b, c, r, p, s, dwa[18], x, tab[300];
string w, w2;
vector<int> v, u;

void foo() {
    for (int i = 0; i < n; ++i) {
        int a1 = a + c;
        int b1 = b + a;
        int c1 = c + b;
        a = a1;
        b = b1;
        c = c1;
    }
}

string best(int l, char z) {
    //cout<<"    dewiodjewiodewo"<<endl;
    if (l == 0) {
        string s1;
        s1+=(char)z;
        return s1;
    }
    string s1 = best(l-1, z);
    string s2 = best(l-1, tab[z]);
    if (s1 < s2) {
        return s1+s2;
    }
    return s2+s1;
}

int main() {
    int i, j;
    tab['P'] = 'R';
    tab['R'] = 'S';
    tab['S'] = 'P';
    scanf("%d", &t);
    for (j=0; j<t; ++j) {
        printf("Case #%d: ", j+1);
        w="";
        x=0;
        scanf("%d %d %d %d", &n, &r, &p, &s);
        a = 1; b = 0; c = 0;
        foo();
        if (a == p && b == r && c == s) {
            x = 1;
        }
        a = 0; b = 1; c = 0;
        foo();
        if (a == p && b == r && c == s) {
            x = 2;
        }
        a = 0; b = 0; c = 1;
        foo();
        if (a == p && b == r && c == s) {
            x = 3;
        }
        if (x == 0) {
            printf("IMPOSSIBLE\n");
        } else {
            if (x == 1) {
                w = best(n, 'P');
            }
            if (x == 2) {
                w = best(n, 'R');
            }
            if (x == 3) {
                w = best(n, 'S');
            }
            /*
            for (i = n; i > 0; --i) {
                for (x = 0; x < w.length(); ++x) {
                    if (w[x] == 'p') {
                        if (i > 4) {
                            w1 += "rp";
                        } else {
                            w1 += "pr";
                        }
                    }
                    if (w[x] == 'r') {
                        if (i > )
                    }
                }
            }
            */
            cout<<w<<endl;
        }
    }
    return 0;
}
