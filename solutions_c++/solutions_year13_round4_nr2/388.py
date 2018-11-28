#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;
string P;

int binP[50];

int binAns[50];

int decAns[50];

void normalize() {
    int rest = 0;
    for (int i = 0; i < 49; i++) {
        decAns[i] += rest;
        rest = decAns[i] / 10;
        decAns[i] %= 10;
    }
}

void buildDec() {
    /*
for (int i = 0; i < N; i++)
    cout << binAns[i];
cout << endl;
*/
    memset(decAns, 0, sizeof(decAns));
    decAns[0] = binAns[N-1];
    for (int i = N - 2; i >= 0; i--) {
        for (int j = 0; j < 50; j++)
            decAns[j] *= 2;
        if (binAns[i] == 1)
            decAns[0]++;
        normalize();
    }

    bool flag = false;
    for (int i = 49; i >= 0; i--) {
        if (decAns[i] > 0)
            flag = true;
        if (flag)
            printf("%c", decAns[i] + '0');
    }
    if (!flag)
        printf("0");
}

void output() {
    buildDec();
}

void solve() {
    for (int i = 0; i < N; i++) {
        int rest = 0;
        for (int j = 0; j < P.size(); j++) {
            int d = P[j] - '0';
            int newd = (d + rest*10) / 2;
            rest = (d + rest*10) % 2;
            P[j] = newd + '0';
        }
        binP[i] = rest;
    }

    bool outputed = false;
    // P--;
    for (int i = 0; i < N; i++) {
        binP[i] = 1 - binP[i];
        if (binP[i] == 0) {
            break;
        }
        if (i == N - 1) {
            for (int j = 0; j < N; j++)
                binAns[j] = 1;
            output();
            outputed = true;
        }
    }

    if (!outputed) {
        for (int i = 0; i < N; i++)
            binAns[i] = 0;
        for (int i = 0; i < N; i++) {
            if (binP[N - i - 1] == 0) break;
            binAns[(i + 1) % N] = 1;
        }
        output();
    }

    printf(" ");

    outputed = false;
    // P--;
    for (int i = 0; i < N; i++) {
        binP[i] = 1 - binP[i];
        if (binP[i] == 1) {
            break;
        }
        if (i == N - 1) {
            for (int j = 0; j < N; j++)
                binAns[j] = 1;
            output();
            outputed = true;
        }
    }

    if (!outputed) {
        for (int i = 0; i < N; i++)
            binAns[i] = 1;
        binAns[0] = 0;
        for (int i = 0; i < N; i++) {
            if (binP[N - i - 1] == 1) break;
            binAns[i+1] = 0;
        }
        output();
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++) {
        cin >> N >> P;
        
        printf("Case #%d: ", testcase);
        solve();
        printf("\n");
    }
    return 0;
}
