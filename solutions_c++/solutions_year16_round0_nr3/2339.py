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

int result[10];

string conv2(long long n) {
    string ret = "";
    while (n > 0) {
        ret.append(1, '0' + n % 2);
        n /= 2;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}


long long convert(long long n, long long b) {

    string t = conv2(n);
    long long ret = 0, exp = 1;
    for (int i = t.size() - 1; i >= 0; i --) {
        ret += (t[i] - '0') * exp;
        n /= b;
        exp *= b;
    }
    return ret;
}

bool solve(long long n) {
    long long base;
    for (int i = 2; i <= 10; i ++) {
        base = convert(n, i);
        bool flag = 0;
        for (long long j = 2; j * j <= base; j ++) {
            if (base % j == 0) {
                flag = true;
                result[i - 2] = j;
                break;
            }
        }
        if (!flag)
            return false;
    }
    return true;
}

vector<vector<LL> > ans;


int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);

    // for (int i = 1; i <= 1000000; i ++) {
    //     solve(i);
    // }

    int cas = 1, id;
    for (cin >> id; id --; cas ++) {
        cout << "Case #" << cas << ": ";
        cin >> n >> m;
        long long j = ( 1LL << (n - 1) )+ 1;

        for (int i = 0; i < m; i ++) {
            bool flag = false;
            while (!flag) {
                flag |= solve(j);
                j += 2;
            }
            vector<LL> res;
            res.push_back(j - 2);
            for (int i = 0; i < 9; i ++)
                res.push_back(result[i]);
            ans.push_back(res);
        }
        cout << endl;
        for (int i = 0; i < m; i ++) {
            cout << conv2(ans[i][0]) << ' ';
            for (int j = 1; j < ans[i].size(); j ++)
                cout << ans[i][j] << ((j == ans[i].size() - 1) ? "\n" : " ");
        }
    }


    //fclose(stdin); fclose(stdout);
}
