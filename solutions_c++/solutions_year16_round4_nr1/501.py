#include <iostream>
#include <cstdio>
#include <bitset>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long ll;

string grow(string s, int n) {
    //cout << "growing " << s << endl;
    if (n == 0) return s;
    string t;
    for (char c : s) {
        if (c == 'R') t += "RS";
        if (c == 'P') t += "PR";
        if (c == 'S') t += "SP";
    }
    return grow(t, n-1);
}

string mysort(string s) {
    //cout << "sorting " << s << endl;
    for (int len = 1; len < (int)s.size(); len *= 2) {
        //cout << "len=" << len << endl;
        string t;
        for (int i=0; i<(int)s.size(); i += len*2) {
            string left = s.substr(i, len), right = s.substr(i+len, len);
            if (left <= right) t += left + right;
            else t += right + left;
        }
        s = t;
        //cout << "new s: " << s << endl;
    }
    return s;
}

int main()
{
    int nt;
    cin >> nt;
    for (int t=1; t<=nt; t++) {
        int n,r,p,s;
        cin >> n >> r >> p >> s;
        printf("Case #%d: ", t);
        int a=1, b=0, c=0;
        for (int i=0; i<n; i++) {
            int d=a+b, e=b+c, f=c+a;
            a=d; b=e; c=f;
        }
        if (r == a && p == b && s == c)
            cout << mysort(grow("R", n));
        else if (r == c && p == a && s == b)
            cout << mysort(grow("P", n));
        else if (r == b && p == c && s == a)
            cout << mysort(grow("S", n));
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
}
