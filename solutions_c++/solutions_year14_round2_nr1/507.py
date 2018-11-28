#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

string s[100500], a[100500];
int c[500][500];
int l[500], r[500];
int n;

#define abs(x) ((x) > 0 ? (x) : -(x))

string f (string s) {
    string t = "";
    t += s[0];
    for (int i = 1; i < s.size(); i++)
        if (s[i] != s[i-1]) t += s[i];
    return t;
}

int calc (int x) {
    int mn = 1<<30;
    int cur;
    for (int i = l[x]; i <= r[x]; i++) {
        cur = 0;
        for (int j = 0; j < n && cur <= mn; j++)
           cur += abs(c[j][x]-i); 
        mn = min(mn,cur);
    }
    return mn;
}

void solve (){
    cin >> n;
    for (int i = 0; i < n; i++) cin >> s[i];
    string t = f(s[0]);
    for (int i = 1; i < n; i++)
        if (t != f(s[i])) {
            cout << "Fegla Won\n";
            return;
        }
    int kk = 0, cnt = 0;
    memset(c,0,sizeof(c));
    memset(r,-1,sizeof(r));
    memset(l,77,sizeof(l));
    for (int i = 0; i < n; i++){
        kk = 0;
        cnt = 0;
        for (int j = 0; j < s[i].size(); j++) {
            if (t[kk] != s[i][j]){
                c[i][kk] += cnt;
                l[kk] = min(c[i][kk],l[kk]);
                r[kk] = max(c[i][kk],r[kk]);
                kk++,cnt=1;
            }
            else cnt++;
        }
        c[i][kk] += cnt;
        l[kk] = min(c[i][kk],l[kk]);
        r[kk] = max(c[i][kk],r[kk]);
    }
    int res = 0;
    for (int i = 0; i < t.size(); i++) res += calc(i);
    cout << res << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
