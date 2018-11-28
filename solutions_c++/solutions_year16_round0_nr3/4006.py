#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <unordered_map>
#include <cmath>

using namespace std;


vector< string > ans;
vector< vector<long long> > fac;

int vec[17];

long long  isPrime(long long x) {

    long long N = sqrt(x);
    for (long long i = 2; i <= N; i++)
        if (x % i == 0) return i;
    return -1;

}

void dfs(int idx, int N, int J) {

    if (ans.size() >= J) return;
    if (idx == N - 1) {
        vector< long long > facc;
        string res = "";
        for (int i = 2; i <= 10; i++) {
            long long num = 0, tmp;
            for (int j = 0; j < N; j++)
                num = num * i + vec[j];
            tmp = isPrime(num);
            if (tmp == -1)
                return;
            facc.push_back( tmp );
        }
        for (int j = 0; j < N; j++)
            res = res + static_cast<char>('0' + vec[j]);
        ans.push_back(res);
        fac.push_back(facc);
    } else {

        vec[idx] = 0;
        dfs(idx + 1, N, J);
        vec[idx] = 1;
        dfs(idx + 1, N, J);

    }
}


int main() {
    int T;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("csmall.out","w",stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d:\n", t);
        int N, J;
        scanf("%d%d", &N, &J);
        vec[0] = 1, vec[N - 1] = 1;
        dfs(1, N , J);
        for (int i = 0; i < J; i++) {
            printf("%s", ans[i].c_str());
            for (int j = 0; j < 9; j++)
                printf(" %lld", fac[i][j]);
            printf("\n");
        }
    }
    return 0;
}
