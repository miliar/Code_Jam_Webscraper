#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <map>
#include <set>

using namespace std;

int N;
long long P;

long long calc(long long q)
{
    long long left = (1LL<<N) - q;
    long long place = (1LL<<N);

    while (left > 0) {
        left = (left-1) / 2;
        place /= 2;
    }

    return place;
}

void solve()
{
    long long L = 1, R = (1<<N);

    while (L < R) {
        long long M = (L+R+1)/2;
        if (calc((1<<N)-M+1) <= (1<<N)-P) R = M-1; else L = M;
    }

    cout << L-1;

    L = 1, R = (1<<N);

    while (L < R) {
        long long M = (L+R+1)/2;
        if (calc(M) <= P) L = M; else R = M-1;
    }

    cout << " " << L-1;
}

int main()
{
    int T; scanf("%d", &T);

    for (int t = 0; t < T; ++t) {
        cin >> N >> P;
        cout << "Case #" << t+1 << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
