#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int per[1002];

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    optimizar_
    int T,D,cont,mint;
    fin>>T;
    for(int i = 1; i <= T; i++){
        fin>>D;
        for(int k=1; k <= D; k++)
            fin>>per[k];
        mint=1000;
        for(int j = 1; j <= 1000; j++){
            cont=0;
            for(int k = 1; k <= D; k++)
                cont += (per[k] - 1) / j;
            mint = min(mint, cont + j);
        }
        fout<<"Case #"<<i<<": "<<mint<<"\n";
    }
    return 0;
}
