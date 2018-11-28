#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>
#include <map>
using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

typedef long long llong;

map<llong, llong> M;

void solve(int cs) {
    int p;
    M.clear();
    scanf("%d", &p);
    vector<llong> A(p);
    for (int i = 0; i < p; i++) {
        scanf("%lld", &A[i]);
    }
    for (int i = 0; i < p; i++) {
        llong x;
        scanf("%lld", &x);
        M[A[i]] = x;
    }
    int n0 = 0;
    llong q0 = M.begin()->second;
    assert(!(q0 & (q0 - 1)));
    while ((1LL << n0) < q0)
        n0++;
    for (map<llong, llong>::iterator it = M.begin(); it != M.end(); it++) {
        assert(it->second % (1LL << n0) == 0);
        it->second >>= n0;
    }
    llong sum = 0;
    for (map<llong, llong>::iterator it = M.begin(); it != M.end(); it++) {
        sum += it->second;
    }
    assert(!(sum & (sum - 1)));
    vector<llong> num;
    map<llong, llong> init = M;
    vector<llong> _num;
    for (int iter = 0; iter < 2; iter++) {
        if (iter == 1) {
            _num = num;
            eprintf("intermediate:");
            sort(_num.begin(), _num.end());
            for (int i = 0; i < _num.size(); i++)
                eprintf(" %lld", _num[i]);
            eprintf("\n");
            for (int i = 0; i < _num.size(); i++)
                _num[i] = abs(_num[i]);
            sort(_num.rbegin(), _num.rend());
            num.clear();
            M = init;
        }
        int pt = 0; 
        while (M.size() > 1) {
            map<llong, llong>::iterator it = M.begin();
            map<llong, llong>::iterator nit = ++M.begin();
            llong x;
            if (iter == 0) {
                x = nit->first - it->first;
                assert(x != 0);
            } else {
                x = _num[pt++]; 
            }
            map<llong, llong> _M = M;
            bool pos = false, neg = false;
            {
                // -x
                M = _M;
                map<llong, llong> Q;
                while (!M.empty()) {
                    it = M.begin();
                    if (it->second == 0) {
                        M.erase(it);
                        continue;
                    }
                    llong v = it->second;
                    Q[it->first + x] += v;
                    M[it->first + x] -= v;
                    assert(M[it->first] >= v);
                    M[it->first] -= v;
                }
                if (Q[0]) {
                    neg = true;
                    M.swap(Q);
                }
            }
            if (!neg)
            {
                // x
                M = _M;
                map<llong, llong> Q;
                while (!M.empty()) {
                    it = M.begin();
                    if (it->second == 0) {
                        M.erase(it);
                        continue;
                    }
                    llong v = it->second;
                    Q[it->first] += v;
                    M[it->first] -= v;
                    assert(M[it->first + x] >= v);
                    M[it->first + x] -= v;
                }
                if (Q[0])
                {
                    pos = true;
                    M.swap(Q);
                }
            }
            assert(pos || neg);
            if (pos)
                num.push_back(x);
            else
                num.push_back(-x);
        }
    }

    /*map<llong, llong> cur;
    for (int msk = 0; msk < (1 << num.size()); msk++) {
        llong sm = 0;
        for (int i = 0; i < num.size(); i++)
            if ((msk >> i) & 1)
                sm += num[i];
        cur[sm]++;
    }
    assert(cur == init);*/
  
    sort(num.begin(), num.end()); 
    eprintf("result:      ");
    for (int i = 0; i < num.size(); i++)
        eprintf(" %lld", num[i]);
    eprintf("\n");
    
    for (int i = 0; i < n0; i++)
        num.push_back(0);
    sort(num.begin(), num.end());
    printf("Case #%d:", cs);
    for (llong x : num)
        printf(" %lld", x);
    printf("\n");
}

int main() 
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        solve(i + 1);
        fflush(stdout);
    }
}
