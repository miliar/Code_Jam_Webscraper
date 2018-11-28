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
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    int num = 0;
    while(T--){
        num++;
        cout << "Case #" << num << ": ";
        int n;
        cin >> n;
        int ans = 0;
        if(n == 0){
            cout << "INSOMNIA\n";
            continue;
        }
        int x = 10;
        bool a[10] = {0};
        for(int i = 1; x; i++){
            int y = n * i;
            while(y){
                if(a[y % 10] == 0){
                    x--;
                    a[y % 10] = true;
                }
                y /= 10;
            }
            ans = i;
        }
        cout << n * ans << "\n";
    }
}
