#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int p[100000];

int tabl[4][4] = {{0, 1, 2, 3}, {1, 4, 3, 6}, {2, 7, 4, 1}, {3, 2, 5, 4}};

int calc(int l, int r)
{
    int s1 = (l >= 4);
    int s2 = (r >= 4);

    l -= s1 * 4;
    r -= s2 * 4;

    if (s1) {
        s1 = -1;
    } else {
        s1 = 1;
    }
    if (s2) {
        s2 = -1;
    } else {
        s2 = 1;
    }

    int res = tabl[l][r];

    int s3 = (res >= 4);

    res -= s3 * 4;

    if (s3) {
        s3 = -1;
    } else {
        s3 = 1;
    }
    int s = s1 * s2 * s3;
    if (s < 0) {
        res += 4;
    }
    return res;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o = 0; o < t; o++) {
        int x, l;
        cin >> x >> l;
        string s;
        cin >> s;
        string str;
        for (int i = 0; i < l; i++) {
            str += s;
        }
        int n = str.size();
        int k = (int)str.size() - 1;
        if (str[k] == 'i') {
            p[k] = 1;
        } else if (str[k] == 'j') {
            p[k] = 2;
        } else if (str[k] == 'k') {
            p[k] = 3;
        } else {
            assert(0);
        }

        for (int i = k - 1; i >= 0; i--) {
            if (str[i] == 'i') {
                p[i] = calc(1, p[i + 1]);
            } else if (str[i] == 'j') {
                p[i] = calc(2, p[i + 1]);
            } else if (str[i] == 'k') {
                p[i] = calc(3, p[i + 1]);
            } else {
                assert(0);
            }
        }
        int ok = 0;
        int curr = 0;
        for (int i = 0; i < n - 2; i++) {
            if (str[i] == 'i') {
                curr = calc(curr, 1);
            } else if (str[i] == 'j') {
                curr = calc(curr, 2);
            } else if (str[i] == 'k') {
                curr = calc(curr, 3);
            } else {
                assert(0);
            }
            int curr2 = 0;
            for (int j = i + 1; j < n - 1; j++) {
                if (str[j] == 'i') {
                    curr2 = calc(curr2, 1);
                } else if (str[j] == 'j') {
                    curr2 = calc(curr2, 2);
                } else if (str[j] == 'k') {
                    curr2 = calc(curr2, 3);
                } else {
                    assert(0);
                }
                if (curr == 1 && curr2 == 2 && p[j + 1] == 3) {
                    ok = 1;
                }
            }
        }

        if (ok) {
            cout << "Case #" << o + 1 << ": " << "YES" << endl;
        } else {
            cout << "Case #" << o + 1 << ": " << "NO" << endl;
        }


    }
    return 0;
}
