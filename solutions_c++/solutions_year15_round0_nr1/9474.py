#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
    int T, t, Max, App, N, P;
    string S;

    cin >> T;

    for(t = 0; t < T; t++)
    {
        App = 0;
        N = 0;
        cin >> Max >> S;
        int Vet[Max+1];

        for(int i = 0; i <= Max; i++)
        {
            Vet[i] = S[i] - '0';
            if(i <= App)
                App += Vet[i];
            else if(Vet[i] != 0)
            {
                P = i - App;
                App += P + Vet[i];
                N += P;
            }
        }

        printf("Case #%d: %d\n", t+1, N);
    }

    return 0;
}

