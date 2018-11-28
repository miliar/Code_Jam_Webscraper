#include <iostream>
#include <set>
#include <cstdlib>
#include <string>
#include <vector>

//#define __OJ__
using namespace std;

string simplifyString(string S) {
    string s = "";
    s += S[0];
    for (int i = 1; i < S.size(); i++) {
        if (S[i] != S[i - 1])
            s += S[i];
    }
    return s;
}

int pancakes(string S) {
    string s = simplifyString(S);
    int n = s.size();
    if (s[n - 1] == '+')
        return n - 1;
    else
        return n;
}

int main() {
#ifdef __OJ__
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//Pancakes//B-large.in", "r", stdin);
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//Pancakes//B-large.out", "w", stdout);
    //freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//Pancakes//B-small-attempt0.in", "r", stdin);
    //freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//Pancakes//B-small-attempt0.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    char s[101];
    for (int i = 0; i < T; i++) {
        scanf("%100s\n", s);
        string S = s;
        printf("Case #%d: %d\r\n", i + 1, pancakes(S));
    }
}

