#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

string s, w;
int n;
long long ansx, ansy;
string resx, resy;

void trans(string &a, int f) {

    for (int i=0; i<n; i++) {

        if (a[i]=='?') {
            if (f) {
                a[i] = '9';
            }
            else {
                a[i] = '0';
            }
        }

    }

}

void doit(string a, string b, int f1, int f2) {

    trans(a, f1);
    trans(b, f2);

    long long x = atoll(a.c_str());
    long long y = atoll(b.c_str());

    if (abs(x-y) < abs(ansx-ansy)) {
        ansx = x;
        ansy = y;
        resx = a;
        resy = b;
    }
    else if (abs(x-y) == abs(ansx-ansy) && (x < ansx || (ansx==x && ansy>y))) {
        ansx = x;
        ansy = y;
        resx = a;
        resy = b;
    }

}

bool check(int x, string &a) {

    stringstream ss;
    ss<<x;
    string b;
    b = ss.str();

    while (b.length() < n) b = "0" + b;

    for (int i=0; i<n; i++) if (a[i]!='?' && a[i]!=b[i]) return false;

    return true;

}

int bestx, besty;
void bf() {

    int p = 1;
    for (int i=0; i<n; i++) p = 10*p;

    bestx = 10000;
    besty = -10000;

    for (int x=0; x<p; x++) {
        for (int y=0; y<p; y++) {

            if (check(x, s) && check(y, w)) {

                if (abs(x-y) < abs(bestx-besty)) {
                    bestx = x;
                    besty = y;
                }
                else if (abs(x-y) == abs(bestx-besty) && x < bestx || (bestx==x && besty>y)) {
                    bestx = x;
                    besty = y;
                }

            }

        }
    }

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int c=0; c<t; c++) {
        cin>>s>>w;

        n = s.length();

        ansx = -1LL<<60;
        ansy = 1LL<<60;

        //bf();

        for (int i=0; i<=n; i++) {

            if (i==n) {
                doit(s, w, 0, 0);
                break;
            }

            if (s[i]=='?') {

                if (w[i]=='?') {

                    s[i] = '0';
                    w[i] = '1';

                    doit(s, w, 1, 0);

                    s[i] = '1';
                    w[i] = '0';

                    doit(s, w, 0, 1);

                    s[i] = '0';
                    w[i] = '0';

                }
                else {

                    int p = w[i]-'0';
                    if (p>0) {
                        s[i] = char('0'+p-1);

                        doit(s, w, 1, 0);
                    }

                    if (p<9) {
                        s[i] = char('0'+p+1);

                        doit(s, w, 0, 1);
                    }

                    s[i] = char('0'+p);

                }

            }
            else {
                if (w[i]=='?') {

                    int p = s[i]-'0';
                    if (p<9) {
                        w[i] = char('0'+p+1);

                        doit(s, w, 1, 0);
                    }

                    if (p>0) {
                        w[i] = char('0'+p-1);

                        doit(s, w, 0, 1);
                    }

                    w[i] = char('0'+p);

                }
                else {

                    int p = w[i]-'0';
                    int q = s[i]-'0';

                    if (p>q) {

                        doit(s, w, 1, 0);
                        break;

                    }
                    else if (p<q) {

                        doit(s, w, 0, 1);
                        break;

                    }

                }
            }

        }


        printf("Case #%d: ", c+1);
        cout<<resx<<" "<<resy<<endl;
        //cout<<bestx<<" "<<besty<<endl;

    }

    return 0;

}
