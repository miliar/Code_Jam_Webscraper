#include<iostream>
#include<string.h>
#include<stdio.h>
#include<string>
#include<cmath>
#include<algorithm>
#include <iomanip>

using namespace std;

#define in() ({ int x; scanf("%d", &x); x; })
#define fr(i,n) for(i = 0; i < n; i++)

void INPUT_FROM_FILE()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    #endif
}

int main()
{
    //INPUT_FROM_FILE();
    double C, F, X;
    int T, i;
    double cps, answer, Xs, Cs, nextXs;
    cin >> T;
    for (i=0; i<T; i++) {
        cin >> C >> F >> X;
        answer = 0;
        cps = 2.0;
        Xs = X / cps;
        Cs = C / cps;
        cps += F;
        nextXs = X / cps;
        while (Cs + nextXs < Xs) {
            answer += Cs;
            Xs = X / cps;
            Cs = C / cps;
            cps += F;
            nextXs = X / cps;
        }
        answer += Xs;
        cout << "Case #" << i+1 << ": "<< fixed << std::setprecision(7)<< answer << endl;
    }
    return 0;
}
