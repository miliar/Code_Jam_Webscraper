#include <bits/stdc++.h>
using namespace std;

ifstream IN;
ofstream OUT;

int T,N,R;
string S;

int main() {
    IN.open("A.in");
    OUT.open("A.out");

    IN >> T;

    for(int k=0;k<T;k++){
        IN >> N >> S;
        int ACUMULADO = 0;
        R=0;

        for(int i=0;i<=N;i++) {
            int ACT = S[i]-'0';

            if(ACUMULADO < i && ACT){
                R+=i-ACUMULADO;
                ACUMULADO=i;
            }
            ACUMULADO+=ACT;
        }
        OUT << "Case #" << k + 1 << ": " << R << "\n";
    }

    return 0;
}
