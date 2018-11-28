#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
#define loop(i,n) for(int i=0;i<n;i++)
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;


int solve(string fst, string snd) {
    char f[101];
    char s[101];
    string a;
    string b;
    strcpy(f, fst.c_str());
    strcpy(s, snd.c_str());
    int size = snd.size();
    int fsize = fst.size();
    int fc = 0;
    int sc = 0;
    char fp = -1;
    char sp = -1;
    int move = 0;

//    printf("%d: %d\n", sc, size);
    while (sc < size) {
//        printf("%d:%d %c:%c %c:%c\n", sc,fc,s[sc], f[fc], fp,sp);
        if (s[sc] == f[fc]) {
            a.append(1,s[sc]);
            b.append(1,s[sc]);
            fp = sp = s[sc];
            sc++;
            fc++;
        } else {
            if (fp != -1 &&  fc != fsize && fp == f[fc]) {
//                printf("fmove++ %c\n", f[fc]);
                a.append(1,f[fc]);
                b.append(1,f[fc]);
                move++;
                fc++;
            } else if (sp != -1 && sc != size && sp == s[sc]) {
                //printf("smove++ %c\n", s[sc]);
                a.append(1,s[sc]);
                b.append(1,s[sc]);
                move++;
                sc++;
            }else {
                return -1;
            }
        }
    }
    if (fc != fsize) {
        if (fp != -1 && fp == f[fc]) {
            while (fp == f[fc]) {
                move++;
                fc++;
            }
            if (fc != fsize) {
                return -1;
            }
        } else {
            return -1;
        }
    }
    //cout << fst << endl;
    //cout << snd << endl;
    //cout << a << endl;
    return move;
}

int main() {
    int t, n;
    cin >> t;
    int count = 1;
    while (count <= t) {
        string fst, snd;
        cin >> n;
        cin >> fst;
        cin >> snd;
        if (fst.size() > snd.size()) {
            swap(fst, snd);
        }
        int ans = solve(fst, snd);
        if (ans == -1) {
            cout << "Case #" << count << ": Fegla Won" << endl;
        } else {
            cout << "Case #" << count << ": " << ans << endl;
        }
        count++;
    }
}
