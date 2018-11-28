/* Author : 헤이그
      날짜 : 2014-04-13-03.17.42 Sunday */
#include <bits/stdc++.h>
using namespace std;
const int MAX = 51;

int A[MAX][MAX];
int N,M,K,R;

void print(){
    for(int x = 1; x <= N; ++x){
        for(int y = 1; y <= M; ++y){
            if (A[x][y] == 1) cout << ".";
            else if (A[x][y] == 2) cout << "c";
            else cout << "*";
        }
        cout << endl;
    }
}

void solve(){
    memset(A,0,sizeof(A));
    cin >> N >> M >> K;
    R = N*M-K;

    if (R == 1){
        A[N][M] = 2;
        print();
        return;
    }

    if (N == 1){
        for(int i = 0; i < K; ++i) cout << "*";
        for(int i = K; i < M-1; ++i) cout << ".";
        cout << "c\n";
        return;
    }

    if (M == 1){
        for(int i = 0; i < K; ++i) cout << "*\n";
        for(int i = K; i < N-1; ++i) cout << ".\n";
        cout << "c\n";
        return;
    }

    for(int i = 3; i <= M; ++i){
        int rem = R/i + (R%i != 0);
        if (rem == 1) continue;
        if (rem == 2 && R%i != 0) continue;
        if (rem == 3 && R%i == 1) continue;
        if (rem > N) continue;

        int k = 0;
        for(; k < rem-2; ++k)
            for(int j = 0; j < i; ++j)
                A[N-k][M-j] = 1;
        int cnt = i - (R%i == 1);
        for(int j = 0; j < cnt; ++j)
            A[N-k][M-j] = 1;
        ++k;
        cnt = (R%i == 0) ? i : (R%i == 1) ? 2 : R%i;
        for(int j = 0; j < cnt; ++j)
            A[N-k][M-j] = 1;
        A[N][M] = 2;
        print();
        return;
    }

    int rem = R/2;
    if (M >= 2 && R%2 == 0 && rem <= N && rem > 1){
        for(int i = 0; i < rem; ++i)
            A[N-i][M] = A[N-i][M-1] = 1;
        A[N][M] = 2;
        print();
        return;
    }

    puts("Impossible");
}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t; cin >> t;
    for(int i = 1; i <= t; ++i)
        cout << "Case #" << i << ":\n", solve();
    return 0;
}
