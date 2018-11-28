#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>

#define REP(a, n) for (int a = 0; a<(n); ++a)

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<int, int> pii;

template<class T> inline int size(const T &t) { return t.size(); }

#define INF 1000000000

//////////////////////////////////////////


void licz() {
    char buf[200];
    scanf("%s", buf);
    int ile = 0;
    int len = strlen(buf);
    REP(a, len)
        if (!a || buf[a]!=buf[a-1])
            ++ile;
    if (buf[len-1]=='+')
        --ile;
    printf("%d\n", ile);
}

int main() {
    int T;
    scanf("%d", &T);
    REP(t, T) {
        printf("Case #%d: ", t+1);
        licz();
    }
}
