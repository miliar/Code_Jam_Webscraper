#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<ll> vi;
typedef vector<pii> vii;
#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << endl
#define ALL(x) x.begin(), x.end()
#define INF (1 << 30)
#define pb push_back
#define lend '\n'


int occur[30];
string ZERO = "ZERO", ONE = "ONE", TWO = "TWO", THREE = "THREE", FOUR  = "FOUR",
    FIVE = "FIVE", SIX = "SIX", SEVEN = "SEVEN", EIGHT = "EIGHT", NINE = "NINE";

string digits[] = {ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE};
stack<int> ans2;

bool has(int d) {
    string &digit = digits[d];
    int this_one[30];
    memset(this_one, 0, sizeof(this_one));
    for (int i = 0; i < digit.size(); ++i) {
        int idx = digit[i] - 'A';
        ++this_one[idx];
    }
    for (char ch = 'A'; ch <= 'Z'; ++ch) {
        int idx = ch - 'A';
        if (this_one[idx] == 0) continue;
        if (occur[idx] < this_one[idx])
            return false;
    }
    return true;
}

void reduce(int d) {
    string &digit = digits[d];
    for (int i = 0; i < digit.size(); ++i) {
        int idx = digit[i] - 'A';
        --occur[idx];
    }
}
void readd(int d) {
    string &digit = digits[d];
    for (int i = 0; i < digit.size(); ++i) {
        int idx = digit[i] - 'A';
        ++occur[idx];
    }
}
bool empty() {
    for (char ch = 'A'; ch <= 'Z'; ++ch) {
        int idx = ch - 'A';
        if (occur[idx] > 0) return false;
    }
    return true;
}

bool backtrack() {
    if (empty())
        return true;
    for (int i = 1; i <= 9; ++i) {
        if (has(i)) {
            reduce(i);
            ans2.push(i);
            if (backtrack())
                return true;
            else {
                readd(i);
                ans2.pop();
            }
        }
    }
    return false;
}

string doit() {
    string letters, ans = "";
    cin >> letters;
    for (int i = 0; i < letters.size(); ++i) {
        char ch = letters[i];
        ++occur[ch - 'A'];
    }
    int zIndex = 'Z' - 'A';
    while (occur[zIndex] > 0) {
        ans = ans + "0";
        reduce(0);
    }
    backtrack();
    string new_str = "";
    while (!ans2.empty()) {
        int dig = ans2.top(); ans2.pop();
        new_str += to_string(dig);
    }
    reverse(new_str.begin(), new_str.end());
    ans = ans + new_str;

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    int T; cin >> T;
    for (int i = 1; i <= T; ++i) {
        memset(occur, 0, sizeof occur);
        string ans = doit();
        cout << "Case #" << i << ": " << ans << lend;
    }
}
