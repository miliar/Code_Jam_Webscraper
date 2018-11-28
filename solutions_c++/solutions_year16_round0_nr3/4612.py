#include <iostream>
#include <map>
#include <stdio.h>
#include <cstddef>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <fstream>
#include <queue>

using namespace std;

long long to_pw(vector <bool> &v, long long pw)
{
    long long ans = 0;
    for (long long i = 0; i < (long long)v.size(); i++) {
        ans = (ans * pw) + v[i];
    }
    return ans;
}

long long is_prime(long long n)
{
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return i;
        }
    }
    return 0;
}

bool check(vector <bool> &v)
{
    if (v[0] == false || v[(long long)v.size() - 1] == false) {
        return false;
    }
    vector <long long> ans;
    for (long long pw = 2; pw <= 10; pw++) {
        long long q = to_pw(v, pw);
        // cout << pw << " " << q << endl;
        long long pm = is_prime(q);
        if (pm) {
            ans.push_back(pm);
        } else {
            return false;
        }
    }
    for (long long i = 0; i < (long long)v.size(); i++) {
        cout << v[i];
    }
    cout << " ";
    for (auto &el : ans) {
        cout << el << " ";
    }
    cout << endl;
    return true;
}

int main()
{
    cout << "Case #1:\n";
    long long need = 50;
    for (long long i = 0; i < (1 << 16) && need; i++) {
        vector <bool> v;
        for (long long j = 0; j < 16; j++) {
            v.push_back((bool)(i & (1 << j)));
        }
        reverse(v.begin(), v.end());
        if (check(v)) {
            need--;
        }
    }
    return 0;
}
