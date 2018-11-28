#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <vector>

#define M 1000000

using namespace std;

int primes[1000001];

int main(){
    int T, P, Q;

    int i, j, k, t;

    vector<int> pvec;

    for(i=0; i<=M; i++)
        primes[i] = 1;

    for(i=2; i<=M; i++)
        if(primes[i]){
            for(j=2*i; j<=M; j+=i)
                primes[j] = 0;
            pvec.push_back(i);
            //printf("%d ", i);
        }

    cin >> T;

    for(t=0; t<T; t++){
        scanf("%d/%d", &P, &Q);

        //printf("T %d %d %d\n", P, Q, Q & -Q);

        for(i=0; i<pvec.size(); i++){
            while(P % pvec[i] == 0 && Q % pvec[i] == 0){
                P /= pvec[i];
                Q /= pvec[i];
            }
        }

        //printf("T %d %d %d\n", P, Q, Q & -Q);

        if(Q == (Q & -Q)){
            int gen = 1;
            while(P < (Q >> 1)){
                gen++;
                Q = Q >> 1;
            }

            printf("Case %d: %d\n", t+1, gen);
        }else{
            printf("Case %d: impossible\n", t+1);
        }
    }

    return 0;
}
