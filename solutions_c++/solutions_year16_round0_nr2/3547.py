#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define CLEAR(v) memset((v), 0, sizeof(v))
#define MP make_pair
#define PB push_back
#define PII pair<int, int>
#define LL long long


int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        string S;
        cin >> S;
        int steps=0;
        FOR(i, 1, SZ(S)) {
            if(S[i] != S[i-1]) steps++;
        }
        if(S[SZ(S)-1] == '-') steps++;

        cout << "Case #" << caso+1 << ": " << steps << endl;
    }
}
