#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

int R[100], C[100];
int law[100][100];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int i, j, T, N, M, cas = 1;
    cin>>T;
    while(T--)
    {
        cin>>N>>M;
        for(i = 0; i < N; i++)
            R[i] = 0;
        for(j = 0; j < M; j++)
            C[j] = 0;
        for(i = 0; i < N; i++)
            for(j = 0; j < M; j++)
                cin>>law[i][j];
        for(i = 0; i < N; i++)
            for(j = 0; j < M; j++)
                R[i] = max(R[i], law[i][j]),
                C[j] = max(C[j], law[i][j]);
        bool pos = true;
        for(i = 0; i < N; i++)
            for(j = 0; j < M; j++)
                pos &= (law[i][j] == R[i] || law[i][j] == C[j]);
        cout<<"Case #"<<cas++<<": "<<(pos ? "YES\n" : "NO\n");
    }
}
