#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int T, N, M[1002], maxa, maxb, dif;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    optimizar_
    M[0]=0;
    fin>>T;
    for(int i = 1; i <= T; i++){
        fin>>N;
        maxa = 0;
        maxb = 0;
        dif = 0;
        for(int j = 1; j <= N; j++){
            fin>>M[j];
            maxa += max(0, M[j-1] - M[j]);
            dif = max(dif, M[j-1] - M[j]);
        }
        for(int k = 1; k < N; k++)
            maxb += min(dif, M[k]);
        fout<<"Case #"<<i<<": "<<maxa<<" "<<maxb<<"\n";
    }
    return 0;
}
