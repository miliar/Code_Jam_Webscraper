#pragma comment(linker, ”/STACK:36777216“)
#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int inf = 2000000000;
const int N = 10000;

int t[4 * N];
char ans[4 * N];

/*
P = 0
R = 1
S = 2
*/

char tochar(int x){
    if(x == 0)return 'P';
    if(x == 1)return 'R';
    if(x == 2)return 'S';
}

int a[3], n, H;

string can(int v, int col, int h = 1){
    if(h == H){
        a[col]--;
        string s;
        s += tochar(col);
        return s;
    }

    if(col == 0){
        string s1 = can(v + v, 0, h + 1);
        string s2 = can(v + v + 1, 1, h + 1);
        return min(s1 + s2, s2 + s1);
    } else
    if(col == 1){
        string s1 = can(v + v, 1, h + 1);
        string s2 = can(v + v + 1, 2, h + 1);
        return min(s1 + s2, s2 + s1);
    } else
    if(col == 2){
        string s1 = can(v + v, 0, h + 1);
        string s2 = can(v + v + 1, 2, h + 1);
        return min(s1 + s2, s2 + s1);
    }
}

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    int num = 0;
    while(T--){
        num++;
        cout << "Case #" << num << ": ";
        int r, p, s;
        cin >> n >> r >> p >> s;

        H = n + 1;
        n = (1 << n);

        string mn = "Z";
        for(int i = 0; i < 3; i++){
            a[0] = p;
            a[1] = r;
            a[2] = s;
            string S = can(1, i);
            if(a[0] == 0 && a[1] == 0 && a[2] == 0){
                mn = min(mn, S);
            }
        }
        if(mn != "Z"){
            cout << mn;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << "\n";
    }
}
