#include <vector>
#include <iostream>
#include <unordered_map>
#include <cassert>
using namespace std;
int L, X, len;
string inp, S;
vector<string> suffix_sum;

string table(char a, char b) {
    if (a == '1') {
        return string(1, b);
    }

    if (b == '1') {
        return string(1, a);
    }

    if (a == 'i') {
        switch (b) {
            case 'i': return "-1";
            case 'j': return "k";
            case 'k': return "-j";
            default: assert(0);
        }
    }

    if (a == 'j') {
        switch (b) {
            case 'i': return "-k";
            case 'j': return "-1";
            case 'k': return "i";
            default: assert(0);
        }
    }
    if (a == 'k') {
        switch (b) {
            case 'i': return "j";
            case 'j': return "-i";
            case 'k': return "-1";
            default: assert(0);
        }
    }

    assert(0);
}

string mul(const string &a, const string &b) {
    int a_sign = a[0] == '-' ? -1 : 1;
    int b_sign = b[0] == '-' ? -1 : 1;
    string c = table(*a.rbegin(), *b.rbegin());
    int c_sign = c[0] == '-' ? -1 : 1;
    string suffix = string(1, *c.rbegin());
    if (a_sign * b_sign * c_sign == -1) {
        return "-" + suffix;
    }
    return suffix;
}

string solve() {
    string a1 = "1";
    for (int i=1;i<len;i++) {
        a1 = mul(a1, string(1, S[i-1]));
        if (a1 == "i") {
            string a2 = "1";
            for (int j=i+1; j<len;j++) {
                a2 = mul(a2, string(1, S[j-1]));
                if (a2 == "j" && suffix_sum[j] == "k") {
                        return "YES";
                }
            }
        }
    }
    return "NO";
}


int main() {
    int T;
    cin >> T;
    for (int i=1;i<=T;i++) {
        cin >> L >> X;
        len = L * X;
        cin >> inp;
        S = "";
        S.reserve(len);
        for (int i=0;i<X;i++) {
            S += inp;
        }
        suffix_sum.resize(len);
        suffix_sum[len - 1] = S[len - 1];
        for (int i = len - 2; i>=0; i--) {
            suffix_sum[i] = mul(string(1, S[i]), suffix_sum[i+1]);
        }
        string res = solve();
        cout << "Case #" << i << ": " << res << endl;
    }
}
