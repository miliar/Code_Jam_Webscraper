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
#include <unordered_map>

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
    int T, N;
    int A[1010], aux[1010];
    int inv1[1010], inv2[1010];
    cin >> T;
    FOR(caso, 1, T+1) {
        cin >> N;
        unordered_map<int, int> index;
        REP(i, N) {
            cin >> A[i];
            index.insert(MP(A[i], i));
        }
        int best=100000000;
        
        sort(A, A+N);
        
        do {
            // check
            int i=0;
            while(i < N-1 and A[i] < A[i+1]) i++;
            while(i < N-1 and A[i] > A[i+1]) i++;
            // cout << i << endl;
            if(i < N-1) continue;
            
            int invs=0;
            REP(i, N) FOR(j, i+1, N) {
                if(index[A[i]] > index[A[j]]) invs++;
            }
            best = min(best, invs);
            
        } while(next_permutation(A, A+N));
        
        
        cout << "Case #" << caso << ": " << best << endl;
    
    }    
    return 0;
}
