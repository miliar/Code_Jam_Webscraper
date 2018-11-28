#include <bits/stdc++.h>

#define cin fin
#define cout fout

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int T, N;

int mask(int x) {
    int retVal = 0;
    while (x > 0) {
        retVal |= (1 << (x%10));
        x /= 10;
    }
    return retVal;
}

int hasFinished(int now) {
    int yo = 0;
    int start = now;
    while (yo+1 < (1 << 10)) {
        yo |= mask(now);
        now += start;
    }
    return now-start;
}

int main()
{
    cin >> T;

    for (int t=1; t<=T; t++) {
        cin >> N;
        cout << "Case #" << t << ": ";
        if (N == 0) cout << "INSOMNIA\n";
        else cout << hasFinished(N) << endl;
    }

    return 0;
}
