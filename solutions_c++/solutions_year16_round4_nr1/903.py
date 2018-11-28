#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

string s[3];
bool F[3];
int n, P, R, S;

void get(int turn, char now, int idx) {
    if (turn==0) {
        s[idx].pb(now);
        return;
    }
    char x1, x2;
    if (now=='R') x1 = 'R', x2 = 'S';
    else if (now=='S') x1 = 'P', x2 = 'S';
    else x1 = 'P', x2 = 'R';
    get(turn-1,x1,idx); get(turn-1,x2,idx);
}

bool check(string s) {
    int n = s.length();
    int numP = 0, numR = 0, numS = 0;
    for (int i = 0; i < n; ++i) {
        numP += s[i]=='P';
        numR += s[i]=='R';
        numS += s[i]=='S';
    }
    return numP == P && numR == R && numS == S;
}

void change(string & s) {
    int dodai = 1<<n;
    for (int len = 1; len <= n; ++len) {
        int L = 1<<(len-1);
        for (int i = 0; i < dodai; ) {
            string s1 = "", s2 = "";
            for (int j = i; j < i+L; ++j)
                s1.pb(s[j]);
            for (int j = i+L; j < i+2*L; ++j)
                s2.pb(s[j]);
            if (s1 > s2) {
                for (int j = i; j < i+L; ++j)
                    swap(s[j],s[j+L]);
            }
            i += 2*L;
        }
    }
}

void solve() {
    for (int i = 0; i < 3; ++i)
        s[i].clear(), F[i] = true;
    get(n,'R',0);
    get(n,'P',1);
    get(n,'S',2);
    for (int i = 0; i < 3; ++i)
        F[i] = check(s[i]);
    if (!F[0] && !F[1] && !F[2]) {
        printf("IMPOSSIBLE\n");
        return;
    }
    for (int i = 0; i < 3; ++i)
        if (F[i]) change(s[i]);
    string res; int tmp = -1;
    for (int i = 0; i < 3; ++i)
    if (F[i]) {
        if (tmp==-1) res = s[i];
        else if (res>s[i]) res = s[i];
    }
    cout << res << "\n";
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int t; scanf("%d",&t); int tmp = t;
    while (t--) {
        scanf("%d%d%d%d",&n,&R,&P,&S);
        printf("Case #%d: ",tmp-t);
        solve();
    }
	return 0;
}
