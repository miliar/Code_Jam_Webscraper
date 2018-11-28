#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <deque>


using namespace std;
#define ll long long

int N, J;

#define TOTRY 50

int ld[11][TOTRY][32];

int lastdig(ll base, ll exp, ll base2) {
    ll v = 1;
    for (int i=0;i<exp;++i) {
        v = (v * base) % base2;
    }
    return v;
}

ll num(ll v, ll base) {
    ll out = 0;
    ll m = 1;
    while (v) {
        if (v & 1LL) {
            out += m;
        }
        m *= base;
        v /= 2LL;
    }
    return out;
}

int isgood(ll a, ll base) {
        for (int v=2;v<TOTRY;++v) {
            int d = 0;
            for (int i=0;i<N;++i) {
                if (a & (1<<i)) {
                    d += ld[base][v][i];
                }
            }

            //printf("%lld is %d in base %d\n", a, d%v, base);

            if (d%v == 0) {
                return v;
            }
        }
        return -1;
}

vector<int> isgood(ll a) {
    vector<int> out;
    for (int base=2;base<=10;++base) {
        int v = isgood(a, base);
        if (v == -1) {
            //printf("%lld failed at base %d\n", num(a, 10), base);
            return vector<int>();
        }
        out.push_back(v);
    }
    return out;
}


string tob(ll v) {
    string out = "";
    ll m = 1;
    while (v) {
        if (v & 1) {
            out = ("1" + out);
        } else {
            out = ("0" + out);
        }
        m*=10;
        v/=2;
    }
    return out;
}


int main() {
    int T;
    cin>>T;

    for (int base=2;base<=10;++base) {
        for (int v=2;v<TOTRY;++v) {
        for (int i=0;i<32;++i) {
            ld[base][v][i] = lastdig(base, i, v);
        }
        }
    }

    for (int t=1;t<=T;++t) {
        cin>>N>>J;

        ll a = (1LL<<(N - 1LL)) + 1;

        vector<ll> out;
        vector<vector<int>> outd;

        while (a < (1LL<<(N)) && out.size() < J) {
            
            vector<int> divs = isgood(a);
            if (!divs.empty()) {
                out.push_back(a);
                outd.push_back(divs);
            }

            a += 2;
        }


        printf("Case #%d:\n", t);
        for (int i=0;i<out.size();++i) {
            printf("%s", tob(out[i]).c_str());
            for (int j = 0; j < outd[i].size(); ++j) {
                printf(" %d", outd[i][j]);
                //printf("(%lld/%lld=%lld+%lld)", num(out[i], j+2), outd[i][j], num(out[i], j+2)/outd[i][j], num(out[i], j+2)%outd[i][j]);
            }
            printf("\n");
        }
    }
}
