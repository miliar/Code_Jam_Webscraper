#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
#include <cassert>
#include <gmpxx.h>

using namespace std;

bool ispal(string n) {
    for(unsigned int j = 0; j < n.size(); j++)
        if(n[j] != n[n.size()-1-j])
            return false;

    return true;
}

vector<mpz_class> candidates;

bool test(string num) {
    mpz_class n(num);
    assert(ispal(n.get_str()));

    mpz_class nn = n*n;
    if(nn.get_str().size() < 100 && ispal(nn.get_str()))
        candidates.push_back(nn);
}

int main() {
    candidates.push_back(mpz_class("1"));
    candidates.push_back(mpz_class("4"));
    candidates.push_back(mpz_class("9"));


    for(int i = 1; i < (1<<25); i++) {
        if(__builtin_popcount(i) >= 5)
            continue;

        string cur;
        for(int j = 31-__builtin_clz(i); j >= 0; j--)
            cur.push_back((i & (1<<j)) ? '1' : '0');
        assert(cur.size() && cur[0] == '1');

        string rev = cur;
        reverse(rev.begin(), rev.end());

        test(cur + rev);
        test(cur + "0" + rev);
        test(cur + "1" + rev);
        test(cur + "2" + rev);
    }

    for(int i = 0; i < 50; i++) {
        string zeroes(i, '0');
        test("2" + zeroes + "2");
        test("2" + zeroes + "1" + zeroes + "2");
    }

    sort(candidates.begin(), candidates.end());

    int t;
    cin >> t;
    for(int z = 1; z <= t; z++) {
        mpz_class a, b;
        cin >> a >> b;
        cout << "Case #" << z << ": " <<
            upper_bound(candidates.begin(), candidates.end(), b) -
            lower_bound(candidates.begin(), candidates.end(), a) << endl;
    }
}
