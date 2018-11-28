#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

#define ll long long

ll pow_mod(ll x,ll n,ll mod) {
    ll ret = 1;
    while (n) {
        if (n & 1) ret = ret * x % mod;
        x = x * x % mod;
        n >>= 1;
    }
    return ret;
}

int N=32;
int J=500;
map<string, vector<int> > ans;

void do_cal() {
    string vs;
    vs.resize(N);
    int curj = 0;
    while (curj < J) {
        vs[0] = vs[N - 1] = '1';
        for (int i = 1; i < N - 1; ++i) vs[i] = rand() % 2 == 0 ? '0' : '1';
        vector<int> tvec;
        for (int b = 2; b <= 10; ++b) {
            for (int k = 2; k <= 3000; ++k) {
                ll m = 0;
                for (int z = 0; z < N; ++z) {
                    if (vs[z] == '1') {
                        m = (m + pow_mod(b, z, k)) % k;
                    }
                }
                if (m == 0) {
                    tvec.push_back(k);
                    break;
                }
            }
        }
        reverse(vs.begin(), vs.end());
        if (tvec.size() == 9 && !ans.count(vs)) {
            ans[vs] = tvec;
            ++curj;
        }
    }
}

int main()
{
    freopen("C-large.out","w",stdout);
    srand(0);
    do_cal();
    map<string, vector<int> >::iterator it = ans.begin();
    printf("Case #1:\n");
    for(;it!=ans.end();++it){
        string value = (*it).first;
        vector<int> &vec = (*it).second;
        printf("%s",value.c_str());
        for(int i=0;i<vec.size();i++) {
            printf(" %d", vec[i]);
        }
        puts("");
    }
    return 0;
}