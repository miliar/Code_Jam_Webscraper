#include <bits/stdc++.h>

using namespace std;

long long len(string a, string b)
{
    long long one, two;
    sscanf(a.c_str(), "%lld", &one);
    sscanf(b.c_str(), "%lld", &two);
    return abs(one - two);
}

long long sc(string a)
{
    long long one;
    sscanf(a.c_str(), "%lld", &one);
    return one;
}

int main()
{
    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        string a, b;
        cin >> a >> b;
        string besta, bestb;
        int i;

        for (i = 0; i < int(a.size()); i++) {
            if (a[i] != '?' && b[i] != '?' && a[i] == b[i]) {
                continue;
            }

            int lefta = 0, leftb = 0, righta = 9, rightb = 9;

            if (a[i] != '?') {
                lefta = righta = a[i] - '0';
            }
            if (b[i] != '?') {
                leftb = rightb = b[i] - '0';
            }
            string cpa = a, cpb = b;

            for (int nowa = lefta; nowa <= righta; nowa++) {
                for (int nowb = leftb; nowb <= rightb; nowb++) {
                    if (nowa != nowb) {
                        a[i] = char('0' + nowa);
                        b[i] = char('0' + nowb);

                        for (int j = i + 1; j < int(a.size()); j++) {
                            if (nowa < nowb) {
                                b[j] = (b[j] == '?' ? '0' : b[j]);
                                a[j] = (a[j] == '?' ? '9' : a[j]);
                            } else {
                                b[j] = (b[j] == '?' ? '9' : b[j]);
                                a[j] = (a[j] == '?' ? '0' : a[j]);
                            }
                        }
                        
                        if (len(besta, bestb) > len(a, b) || (len(besta, bestb) == len(a, b) && sc(a) < sc(besta)) ||
                        (len(besta, bestb) == len(a, b) && sc(besta) == sc(a) && sc(b) < sc(bestb))) {
                            besta = a, bestb = b;
                        }
                        a = cpa, b = cpb;
                    }
                }
            }

            if (a[i] != '?' && b[i] != '?' && a[i] != b[i]) {
                break;
            }

            if (a[i] != '?') {
                b[i] = a[i];
            } else if (b[i] != '?') {
                a[i] = b[i];
            } else {
                a[i] = b[i] = '0';
            }
        }
        cout << "Case #" << tst + 1 << ": ";

        if (i == int(a.size())) {
            cout << a << ' ' << b << '\n';
        } else {
            cout << besta << ' ' << bestb << '\n';
        }
    }
    return 0;
}
