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
    int T, N, X;
    int S[10100];
    cin >> T;
    FOR(caso, 1, T+1) {
        cin >> N >> X;
        REP(i, N) cin >> S[i];
        sort(S, S+N);
        int tot=0;
        int i=0; int j=N-1;
        while(i<=j) {
            if(i==j) {
                tot++;
                break;
            }
            while(j>i and S[j]+S[i]>X) j--, tot++;
            i++; j--;
            tot++;
        }
        
        cout << "Case #" << caso << ": " << tot << endl;
    }    
    return 0;
}
