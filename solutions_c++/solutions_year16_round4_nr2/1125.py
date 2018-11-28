#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <map>
#include <stdint.h>
#include <climits>
#include <queue>
#include <iostream>


using namespace std;

char ism[300][500];
double memo[300][500];

int N;
double prob[300];

double dp(int at, int diff) {
    if(at == N) {
        if(diff == 0) {
            return 1.0;
        }
        else {
            return 0.0;
        }
    }
    if(abs(diff) > N-at){return 0.0;}
    const int adiff = diff + 250;
    if(ism[at][adiff]) {
        return memo[at][adiff];
    }
    double out =  0;
    if(1) {
        double dd = prob[at] * dp(at+1,diff+1);
        dd += (1.0 - prob[at]) * dp(at+1, diff-1);
        out = max(out, dd);
    }
    ism[at][adiff] = 1;
    memo[at][adiff] = out;
    return out;
}

int bc(int x) {
    int out =0;
    while(x) {
        out += 1;
        x &= x-1;
    }
    return out;
}



int main(int argc, char **argv) {
    int T;
    cin >> T;
    double ppp[400];
    for(int _cn = 1;_cn <= T;++_cn) {
        memset(ism, 0, sizeof(ism));
        int K;
        int NN;
        cin >> NN >> K;
        for(int i=0;i<NN;++i) {
            cin >> ppp[i];
        }
        sort(ppp, ppp + NN);
        double out = 0.0;
        ::N = K;
        for(int i=0;i<(1<<NN);++i) {
            if(bc(i) != K){continue;}
            memset(ism, 0, sizeof(ism));
            for(int ct=0,j=0;j<NN;++j) {
                if(i & (1<<j)) {
                    prob[ct++] = ppp[j];
                }
            }
            double xx = dp(0, 0);
            out = max(out, xx);
        }
        printf("Case #%d: %.12lf\n", _cn, out);
    }

    return 0;
}

