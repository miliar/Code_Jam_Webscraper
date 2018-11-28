#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;

int T, C=1;
char s[200020];
int n;
stack<char> S;

int calc(int ini, int fim) {
    int resp = 0;
    while (!S.empty()) S.pop();
    for (int i=0;i<n;i++) {
        if (!S.empty() and S.top()==s[i]) {
            resp += 10;
            S.pop();
        } else
            S.push(s[i]);
    }
    return resp;
}

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%s",s);
        n = strlen(s);
        int r = calc(0,n-1);
        r += (S.size()/2)*5;
        printf("%d\n",r);
    }

    return 0;
}
