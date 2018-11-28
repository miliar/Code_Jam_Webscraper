#include <algorithm>
#include <iostream>
#include <utility>

using namespace std;

enum { I = 2, J, K};

const int multable[4][4] = {{ 1,  I,  J,  K},
                            { I, -1,  K, -J},
                            { J, -K, -1,  I},
                            { K,  J, -I, -1}};

inline int sign(int x)
{
    return (x > 0) - (x < 0);
}

void print(int a)
{
    if (sign(a) == -1) {
        cout << "-";
    }
    switch(abs(a)) {
        case 1:
            cout << 1;
            break;
        case I:
            cout << "I";
            break;
        case J:
            cout << "J";
            break;
        case K:
            cout << "K";
            break;
        default:
            cout << "WTF(" << a << ")";
    }
}

int mul(int a, int b)
{
    int sgn = sign(a) * sign(b);
    return sgn * multable[abs(a) - 1][abs(b) - 1];
}

int from_char(char c)
{
    switch (c) {
        case 'i': return I;
        case 'j': return J;
        case 'k': return K;
        default: exit(-1);
    }
}

bool solve(long long l, long long x, std::vector<int> &s)
{
    vector<int> rem(4 * l + 1);
    rem[4 * l] = 1;
    for (int i = 4 * l - 1; i >= 0; --i) {
        rem[i] = mul(s[i % l], rem[i + 1]);
    }
    int start = 1;
    for (int fst = 0; fst < 4 * l && fst < x * l; ++fst) {
        start = mul(start, s[fst % l]);
        if (start != I) {
            continue;
        }
        int mid = 1;
        for (int snd = fst + 1; snd < fst + 4 * l && snd < x * l; ++snd) {
            mid = mul(mid, s[snd % l]);
            if (mid != J) {
                continue;
            }
            long long to_end = x * l - (snd + 1);
            to_end = to_end % (4 * l);
            if (to_end == 0) {
                to_end = 4 * l;
            }
            if (rem[4 * l - to_end] == K) {
                return true;
            }
        }
    }
    return false;
}

int main()
{
    int t;
    cin >> t;
    for (int tcur = 0; tcur < t; ++tcur) {
        long long l, x;
        std::string s;
        cin >> l >> x;
        cin >> s;
        vector<int> nums(l);
        transform(begin(s), end(s), begin(nums), from_char);
        cout << "Case #" << tcur + 1 << ": ";
        cout << (solve(l, x, nums) ? "YES" : "NO") << endl;
    }
    return 0;
}
