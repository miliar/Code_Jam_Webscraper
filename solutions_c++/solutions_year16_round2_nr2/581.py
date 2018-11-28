#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <sstream>

using namespace std;

string a, b, reca, recb;
long long l, ansa, ansb;

long long val(string a){
    long long ret = 0;
    for (int i = 0; i < a.size(); ++ i){
        long long tmp = a[i] - '0';
        ret = ret * 10 + tmp;
    }
    return ret;
}

void work(string a, string b, int c, int d){
    if (c == l){
        long long tmpa = val(a), tmpb = val(b);
        if (abs(tmpa - tmpb) < abs(ansa - ansb)
            || (abs(tmpa - tmpb) == abs(ansa - ansb) && (tmpa < ansa || (tmpa == ansa && tmpb < ansb)))){
                ansa = tmpa;
                ansb = tmpb;
                reca = a;
                recb = b;
            }
        return;
    }
    if (d == 0){
        if (a[c] == b[c]){
            if (a[c] == '?'){
                a[c] = '0';
                b[c] = '0';
                work(a, b, c + 1, d);
                a[c] = '0';
                b[c] = '1';
                work(a, b, c + 1, -1);
                a[c] = '1';
                b[c] = '0';
                work(a, b, c + 1, 1);
            } else
            work(a, b, c + 1, d);
        }
        if (a[c] != '?' && b[c] != '?'){
            if (a[c] > b[c]) work(a, b, c + 1, 1);
                        else work(a, b, c + 1, -1);
        }
        if (a[c] == '?'){
            if (b[c] != '9'){
                a[c] = b[c] + 1;
                work(a, b, c + 1, 1);
            }
            a[c] = b[c];
            work(a, b, c + 1, 0);
            if (b[c] != '0'){
                a[c] = b[c] - 1;
                work(a, b, c + 1, -1);
            }
        }
        if (b[c] == '?'){
            if (a[c] != '9'){
                b[c] = a[c] + 1;
                work(a, b, c + 1, -1);
            }
            b[c] = a[c];
            work(a, b, c + 1, 0);
            if (a[c] != '0'){
                b[c] = a[c] - 1;
                work(a, b, c + 1, 1);
            }
        }
    }
    if (d == 1){
        if (a[c] == '?') a[c] = '0';
        if (b[c] == '?') b[c] = '9';
        work(a, b, c + 1, d);
    }
    if (d == -1){
        if (a[c] == '?') a[c] = '9';
        if (b[c] == '?') b[c] = '0';
        work(a, b, c + 1, d);
    }
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        cin >> a >> b;
        l = a.size();
        ansa = 0, ansb = pow(10, l);
        work(a, b, 0, 0);
        printf("Case #%d: ", cas);
        cout << reca << ' ' << recb << endl;
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
