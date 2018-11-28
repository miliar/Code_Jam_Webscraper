#include<bits/stdc++.h>

using namespace std;

bool digito[10];
int cont = 0;
void verifica(long long int N)
{
    while(N > 0)
    {
        int k = N % 10;
        N /= 10;
        if(!digito[k])
            cont++;
        digito[k] = 1;
    }
}
int main()
{
    int T;
    long long int N;
    scanf("%d", &T);
    for(int l = 1; l <= T; l++)
    {
        cont = 0;
        printf("Case #%d: ", l);
        scanf("%lld", &N);
        long long int A = N;
        if(N == 0){
            printf("INSOMNIA\n");
            continue;
        }

        for(int i = 0; i < 10; i++)
            digito[i] = 0;
        verifica(A);
        while(cont < 10)
        {
            A += N;
            verifica(A);
        }

        printf("%lld\n", A);
    }

    return 0;
}
