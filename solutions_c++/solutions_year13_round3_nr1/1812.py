#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#define MAXN 500
#define FILE "A-small-attempt0"

using namespace std;
string l;
int n;
inline bool checkIf(char a) {
    if(a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u')
        return true;
    return false;
}

long long getN() {
    long long answer = 0ll;
    for(int i = 0; i < l.size(); ++i) {
        int pos, c = 0;
        for(pos = i; pos < l.size() && c < n; ++pos)
            if(!checkIf(l[pos]))
                ++c;
            else
                c = 0;

        if(c == n)
            answer += (long long) (l.size() - pos + 1);

    }

    return answer;

}

int main() {
    int t;

    ifstream fin(FILE".in");
    freopen(FILE".out", "w", stdout);

    fin >> t;

    for(int i = 1; i <= t; ++i) {

        fin >> l >> n;

        printf("Case #%d: %lld\n", i, getN());
    }

    fin.close();
    return 0;
}
