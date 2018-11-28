#include <cstdio>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <ctime>
//#include <cmath>
#include <vector>
#include <map>
using namespace std;
typedef long long LL;
typedef pair<int,int> pint;
typedef pair<LL,LL> pll;
#define fi first
#define se second
typedef map<int,int> mapint;
typedef vector<int> vint;
typedef vector<vint> vintp;
#define rep(i,j,k) for (int i = (j);i <= (k);i ++)
#define repd(i,j,k) for (int i = (j);i >= (k);i --)
#define ran2 (rand() % 32000 * 32000 + rand() % 32000)
#define pb push_back
#define mp make_pair
#define SIZE(i) ((int)(i.size()))
int m,n,j,k,l,i,o,p,__t;
char ch;
void read(int &a) {
    for (ch = getchar();(ch < '0' || ch > '9') && (ch != '-');ch = getchar());
    if (ch == '-') a = 0,__t = -1; else a = ch - '0',__t = 1;
    for (ch = getchar();ch >= '0' && ch <= '9';ch = getchar()) a = a * 10 + ch - '0';
    a *= __t;
}

bool digit[10];
int digit_cnt;

void putin(int i) {
    while (i > 0) {
        if (digit[i % 10] == 0)
            digit[i % 10 ] = 1, digit_cnt += 1;
        i /= 10;
    }
}

void solve(int i) {
    if (i == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    memset(digit, 0, sizeof digit);
    digit_cnt = 0;
    int n = i;
    while (digit_cnt != 10 && n <= 1e9) {
        putin(n);
        n += i;
    }
    // if (n > 1e9)
        // cout << "error" << endl;
    cout << n - i << endl;
}

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    // for (int i = 1; i <= 1000000; i ++) {
    //     solve(i);
    // }

    int cas = 1, id;
    for (cin >> id; id --; cas ++) {
        cout << "Case #" << cas << ": ";
        string s;
        cin >> s;
        int seg = 0, is_minus = -1;
        for (int i = 0; i < s.length(); i ++) {
            if (s[i] == '-') {
                if (is_minus != 1) {
                    is_minus = 1;
                    seg += 1;
                }
            } else {
                if (is_minus != 0)
                    seg += 1;
                is_minus = 0;
            }
        }
        int ret = seg;
        if (s[s.length() - 1] == '+')
            ret --;
        // if (s[0] == '-')
            // ret --;
        
        cout << ret << endl;
    }


    //fclose(stdin); fclose(stdout);
}
