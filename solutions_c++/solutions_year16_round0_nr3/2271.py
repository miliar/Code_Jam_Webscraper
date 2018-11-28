#include <bits/stdc++.h>
using namespace std;

string bin(int x){
    char _tmp[65], *tmp = _tmp + 64;
    *tmp = 0;
    do{
        *--tmp = (x & 1) + '0';
        x >>= 1;
    }while(x);
    return tmp;
}

int Itoa(const string& s, int base){
    int r = 0;
    for(size_t i = 0; i < s.size(); ++i) r = r * base + s[i] - '0';
    return r;
}

int getDiv(int x){
    for(int i = 2; i * i <= x; ++i) if(x % i == 0) return i;
    return 0;
}

int d[11];

bool judge(int x){
    string s = bin(x);
    for(int b = 2; b <= 10; ++b){
        d[b] = getDiv(Itoa(s, b));
        if(d[b] == 0) return false;
    }
    return true;
}

int find(int n, int coin[], int divisor[][11], string bit[]){
    int cnt = 0;
    for(int s = (1 << (n - 1)) + 1; s < (1 << n); s += 2){
        if(judge(s)){
            coin[cnt] = s;
            memcpy(divisor[cnt], d, sizeof d);
            bit[cnt] = bin(s);
            ++cnt;
            // cout << bin(s);
            // for(int i = 2; i < 11; ++i) cout << ' ' << d[i];
            // cout << endl;
        }
    }
    return cnt;
}

string s4[1 << 4], s8[1 << 8];
int c4[1 << 4], d4[1 << 4][11], n4;
int c8[1 << 8], d8[1 << 8][11], n8;

// void solve(int n, int j){
//     n4 = find(4, c4, d4, s4);
//     n8 = find(8, c8, d8, s8);
//     // cout << n4 << ' ' << n8 << endl; //2 32

//     int m = n / 4;
//     for(int i = 0; j && i < n4; ++i){
//         for(int s = (1 << (m - 1)) + 1; j && s < (1 << m); s += 2){
//             for(int k = 0; k < m; ++k) {
//                 if(s & (1 << k)) cout << s4[i];
//                 else cout << "0000";
//             }
//             for(int k = 2; k <= 10; ++k) cout << ' ' << d4[i][k];
//             cout << endl;
//             --j;
//         }
//     }


//     m = n / 8;
//     for(int i = 0; j && i < n8; ++i){
//         bool flag = true;
//         for(int k = 0; k < n4; ++k){
//             if(s4[k] + s4[k] == s8[i]) flag = false;
//         }
//         if(!flag) continue;
//         for(int s = (1 << (m - 1)) + 1; j && s < (1 << m); s += 2){
//             for(int k = 0; k < m; ++k) {
//                 if(s & (1 << k)) cout << s8[i];
//                 else cout << "00000000";
//             }
//             for(int k = 2; k <= 10; ++k) cout << ' ' << d8[i][k];
//             cout << endl;
//             --j;
//         }
//     }

//     //total 8 + 30 = 38 when n = 16
// }

void solve_2(int n, int j){
    const int t[] = {0, 0, 3, 2, 3, 2, 7, 2, 3, 2, 3};
    int cnt = 0;
    string s[100];
    n8 = find(8, c8, d8, s8);
    for(int i = 0; i < n8; ++i){
        int j;
        for(j = 2; j <= 10; ++j) if(d8[i][j] != t[j]) break;
        if(j <= 10) continue;
        s[cnt++] = s8[i];
    }
    //assert(cnt == 9);
    int m = n / 8;
    for(int a = 0; j && a < 9 * 9; ++a){
        for(int b = 0; j && b < pow(10.0, m - 2); ++b){
            cout << s[a / 9];
            for(int i = 0, bb = b; i < m - 2; ++i, bb /= 10 ){
                if(bb % 10 == 9) cout << "00000000";
                else cout << s[bb % 10];
            }
            cout << s[a % 9];
            for(int i = 2; i <= 10; ++i) cout << ' ' << d[i];
            cout << endl;
            --j;
        }
    }
}

int main(){
    int T, n, j;
    cin >> T >> n >> j;
    cout << "Case #1:" << endl;
    solve_2(n, j);
    return 0;
}