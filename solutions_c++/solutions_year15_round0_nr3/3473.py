#include <cstdio>
#include <cassert>
#include <algorithm>

#include <vector>
#include <string>

using namespace std;

enum quat_type { ONE = 0, I = 1, J = 2, K = 3 };
struct quat {
    unsigned char sign;
    quat_type type;
    quat(unsigned char sign, quat_type type) : sign(sign), type(type) {}
};

const quat POS_ONE(0, ONE);
const quat POS_I(0, I);
const quat POS_J(0, J);
const quat POS_K(0, K);
const quat NEG_ONE(1, ONE);
const quat NEG_I(1, I);
const quat NEG_J(1, J);
const quat NEG_K(1, K);

const quat mul_table[4][4] = {
    {POS_ONE, POS_I, POS_J, POS_K},
    {POS_I, NEG_ONE, POS_K, NEG_J},
    {POS_J, NEG_K, NEG_ONE, POS_I},
    {POS_K, POS_J, NEG_I, NEG_ONE}
};

quat operator*(const quat& a, const quat& b) {
    const quat& mul = mul_table[a.type][b.type];
    return quat(mul.sign ^ a.sign ^ b.sign, mul.type);
}

bool operator==(const quat& a, const quat& b) {
    return (a.sign == b.sign) && (a.type == b.type);
}

const quat& fromChar(char c) {
    switch(c) {
    case 'i': return POS_I;
    case 'j': return POS_J;
    case 'k': return POS_K;
    }
}

const quat div_table[4][4] = {
    {POS_ONE, NEG_I, NEG_J, NEG_K},
    {POS_I, POS_ONE, POS_K, NEG_J},
    {POS_J, NEG_K, POS_ONE, POS_I},
    {POS_K, POS_J, NEG_I, POS_ONE}
};

quat operator/(const quat& a, const quat& b) {
    const quat& div = div_table[a.type][b.type];
    return quat(div.sign ^ a.sign ^ b.sign, div.type);
}

char s[10000];

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int l, x;
        scanf("%d%d", &l, &x);
        scanf("%s", s);
        string str;
        for (int j = 0; j < x; j++) str += s;
        int len = str.length();
        quat total = POS_ONE;
        for (int j = 0; j < len; j++) {
            total = total * fromChar(str[j]);
        }
        bool found = false;
        quat i_buf = POS_ONE;
        for (int j = 1; j < len - 1; j++) {
            i_buf = i_buf * fromChar(str[j - 1]);
            if (!(i_buf == POS_I)) continue;
            quat j_buf = POS_ONE;
            for (int k = j + 1; k < len; k++) {
                j_buf = j_buf * fromChar(str[k - 1]);
                if (!(j_buf == POS_J)) continue;
                
                quat front = i_buf * j_buf;
                quat k_buf = total / front;
                if (k_buf == POS_K) {
                    found = true;
                    printf("Case #%d: YES\n", i);
                    break;
                }
            }
            if (found) break;
        }
        if (!found) printf("Case #%d: NO\n", i);
    }
}