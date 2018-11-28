#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

char per[1002];

int main()
{
    optimizar_
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T,S,cont,nec;
    fin>>T;
    for(int i=1; i <= T; i++){
        fin>>S;
        cont=0;
        nec=0;
        for(int k=0; k <= S; k++){
            fin>>per[k];
            if(cont < k){
                nec+=k-cont;
                cont=k;
            }
            cont+=per[k]-48;
        }
        fout<<"Case #"<<i<<": "<<nec<<"\n";
    }
    return 0;
}
