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

int seen[10];
int seen_count;

void mark(int d) {
    if(!seen[d]) seen_count++;
    seen[d]=1;
}

void readnum(int n) {
    while(n) {
        int d = n%10;
        n /= 10;
        mark(d);
    }
}

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        int N;
        cin >> N;
        CLEAR(seen);
        seen_count=0;

        cout << "Case #" << caso+1 << ": ";
        if(N) {
            int curr = 0;
            while(seen_count < 10) {
                curr += N;
                readnum(curr);
            }
            cout << curr;
        } else {
            cout << "INSOMNIA";
        }
        cout << endl;
    }
}







