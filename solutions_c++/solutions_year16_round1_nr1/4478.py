#include <iostream>
#include <deque>
#include <vector>

//#define __OJ__
using namespace std;

string lastWord(char* S) {
    deque<char> Q;
    for (int i = 0; S[i] != '\0'; i++) {
        if (Q.empty()){
            Q.push_back(S[i]);
        }
        else if (Q.front() > S[i]) {
            Q.push_back(S[i]);
        }
        else {
            Q.push_front(S[i]);
        }
    }
    string word;
    while (!Q.empty()) {
        word += Q.front();
        Q.pop_front();
    }
    return word;
}

int main() {
#ifdef __OJ__
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//BFFs//A-large.in", "r", stdin);
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//BFFs//A-large.out", "w", stdout);
#endif
    int T;
    scanf ("%d", &T);
    char S[1001];
    for (int i = 0; i < T; i++) {
        scanf("%1000s\n", S);
        printf("Case #%d: %s\r\n", i + 1, lastWord(S).c_str());
    }
}