#include<iostream>
#include<set>
using namespace std;

bool digits[10] = { false };
int res = 0;
int g_N;
int g_last = 0;

set<int> check_set;

bool check(int n, int prev_base) {
    //cout << "Check: " << n << endl;
    if (check_set.count(n) == 0) {
        check_set.insert(n);
    } else {
        if (res == 10)
            return true;
        else
            return false;
    }

    if (n == 0) {
        if (!digits[0]) {
            res++;
            digits[0] = true;
        }
    }
    int base = n > 0 ? 1 : 10;

    while (n / base > 0) {
        int x = (n / base) % 10;
        if (!digits[x]) {
            res++;
            digits[x] = true;
        }

        base = base * 10;
    }

    int now = n;
    while ((now + n) % (base*10) != n) {
        now += n;
        //cout << n <<' '<< now << endl;

        int temp = now;
        while (temp > 0) {
            int x = temp % 10;
            if (!digits[x]) {
                res++;
                digits[x] = true;
            }
            temp /= 10;
        }
        if (res == 10) {
            g_last = now * prev_base;
            return true;
        }
    }

    now /= (base * 10);
    if (now == g_N) {
        return false;
    }

    return check(now, base * 10);
}
int main() {

    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        cin >> g_N;
        for (int j = 0; j < 10; j++) {
            digits[j] = false;
        }
        res = 0;
        check_set.clear();

        if (!check(g_N, 1))
       {
           cout << "Case #" << i << ": INSOMNIA"<<endl;
       } 
       else
       {
           cout << "Case #" << i << ": " << g_last << endl;
       }
    }
    return 0;
}