/// In the name of God

#include <bits/stdc++.h>

#define int long long

using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define X first
#define Y second
#define all(o) o.begin(), o.end()
const int maxn = 1e5 + 10;
int a[maxn], cnt[3], Cnt[3];
string dp[maxn];
string doo(){
    int n;
    cin >> n;
    cin >> cnt[1] >> cnt[0] >> cnt[2];
    for(int win = 0; win < 3; win++){
        a[1] = win;
        int cur = 2;
        for(int h=0; h<n; h++){
            memset(Cnt, 0, sizeof Cnt);
            for(int i=cur; i<(2*cur); i++){
                int p = i/2;
                if(i % 2 == 0) a[i] = a[p];
                else a[i] = (a[p] + 1) % 3;
                Cnt[a[i]]++;
            }
            cur *= 2;
        }
        cur /= 2;
        bool can = 1;
        for(int i=0; i<3; i++)
            if(Cnt[i] != cnt[i]) can = 0;
        if(!can) continue;
        for(int i=cur; i<(2*cur); i++){
            char os = char(a[i] + '0');
            string os2;
            os2 += os;
            dp[i] = os2;
        }
        cur /= 2;
        while(cur != 0){
            for(int i=cur; i<2*cur; i++){
                string t1 = dp[2 * i];
                string t2 = dp[2 * i + 1];
                string s1 = t1 + t2;
                string s2 = t2 + t1;
                dp[i] = min(s1, s2);
            }
            cur /= 2;
        }
        return dp[1];
    }
    return "IMPOSSIBLE";
}
string f(string s){
    if(s[0] == 'I') return s;
    string res;
    for(int i=0; i<s.size(); i++){
        int x =s[i] - '0';
        if(x == 0) res += 'P';
        if(x == 1) res += 'R';
        if(x == 2) res += 'S';
    }
    return res;
}
main(){
    freopen("ALi.in", "r", stdin);
    freopen("ALo.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i + 1 << ": ";
        cout << f(doo()) << endl;

    }
}
