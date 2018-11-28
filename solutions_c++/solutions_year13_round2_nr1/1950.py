#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<map>

using namespace std;
int N;
map<int, int> M[100];

int f(vector<int> va, int s, int A) {
    if(s == N) return 0;
    if(M[s].find(A) != M[s].end()) {
        return M[s][A];
    }
    if(va[s] < A) {
        return M[s][A] = f(va, s+1, A+va[s]);
    }
    int t = 0;
    int x = A;
    while(x <= va[s]) {
        x += x-1;
        ++t;
    }
    return M[s][A] = min(
        t + f(va, s+1, x + va[s]),
        1 + f(va, s+1, A));
}

int main() {
    int C, A, a;
    cin >> C;
    for(int cases = 1; cases <= C; ++cases) {
        vector<int> va;
        cin >> A >> N;
        for( int i = 0;  i< N; ++i) {
            cin >> a;
            va.push_back(a);
            M[i].clear();
        }
        sort(va.begin(), va.end());

        int ans = 0;
        if(A == 1) {
            ans = N;
        } else {
            ans = f(va, 0, A);
        }
        printf("Case #%d: %d\n", cases, ans); 
    }
    return 0;
}

