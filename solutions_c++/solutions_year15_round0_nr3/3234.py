#include <iostream>
#include <string>
#include <cstring>

using namespace std;

class Q 
{
    public:
    int sign;
    char val; 
};

Q multiply(Q a, Q b)
{
    Q r;
    r.sign = a.sign * b.sign;
    if (a.val == '1') {
        r.val = b.val;
    }
    else if (a.val == 'i') {
        if (b.val == '1')
            r.val = 'i';
        else if (b.val == 'i') {
            r.val = '1';
            r.sign *= -1;
        }
        else if (b.val == 'j')
            r.val = 'k';
        else if (b.val == 'k') {
            r.val = 'j';
            r.sign *= -1;
        }
    }
    else if (a.val == 'j') {
        if (b.val == '1')
            r.val = 'j';
        else if (b.val == 'i') {
            r.val = 'k';
            r.sign *= -1;
        }
        else if (b.val == 'j') {
            r.val = '1';
            r.sign *= -1;
        }
        else if (b.val == 'k') {
            r.val = 'i';
        }
    }
    else if (a.val == 'k') {
        if (b.val == '1')
            r.val = 'k';
        else if (b.val == 'i')
            r.val = 'j';
        else if (b.val == 'j') {
            r.val = 'i';
            r.sign *= -1;
        }
        else if (b.val == 'k') {
            r.val = '1';
            r.sign *= -1;
        }

    }
    return r;
}

bool check(const char *data, int len, int repeats)
{
    static char full[100000];
    int full_len = len * repeats;
    int c = 0;
    for (int i = 0; i < repeats; ++i)
        for (int j = 0; j < len; ++j)
            full[c++] = data[j];
    static Q map[2 * 10000][2 * 10000];
    for (int i = 0; i < full_len; ++i) {
        map[i][i].sign = 1;
        map[i][i].val = full[i];
        for (int j = i + 1; j < full_len; ++j) {
            Q t;
            t.sign = 1;
            t.val = full[j];
            map[i][j] = multiply(map[i][j - 1], t); 
        }
    }
    for (int i = 1; i < full_len; ++i) {
        if (map[0][i - 1].sign == 1 && map[0][i - 1].val == 'i')
            for (int j = i + 1; j < full_len; ++j) {
                if (map[i][j - 1].sign == 1 && map[i][j - 1].val == 'j'
                    && map[j][full_len - 1].sign == 1 && map[j][full_len - 1].val == 'k')
                    return true;
            }
    }
    return false;
}

int main() {
    int T;
    int len, repeats;
    string data;
    cin >> T;
    for (int num_case = 1; num_case <= T; ++num_case) {
        cin >> len;
        cin >> repeats;
        cin >> data; 
        cout << "Case #" << num_case << ": ";
        if (check(data.c_str(), len, repeats))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
