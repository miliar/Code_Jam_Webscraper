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

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    int num = 0;
    while(T--){
        num++;
        cout << "Case #" << num << ": ";

        string s;
        cin >> s;
        int n = s.length(), ans = 0;
        int r = n - 1;
        while(r >= 0 && s[r] == '+') r--;
        n = r + 1;
        if(n){
            int l = 0;
            while(l < n && s[l] == '-'){
                s[l] = '+';
                l++;
            }

            if(l == 0){
                ans = 0;
            } else {
                ans = 1;
            }

            l = 0;
            for(int i = 0; i < n; i++){
                if(s[i] == '-'){
                    ans += 1;
                    while(i < n && s[i] == '-'){
                        i++;
                    }
                    i--;
                    ans += 1;
                }
            }
        }
        cout << ans << "\n";
    }
}
