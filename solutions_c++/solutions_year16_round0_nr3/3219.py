#include <bits/stdc++.h>
using namespace std;
/*char line[200];
int main()
{
    int T;
    scanf("%d \n", &T);
    for(int t = 1; t<=T; t++)
    {
        gets(line);
        int n = strlen(line);
        int cont = 1;
        for(int i = 0; i<n-1; i++)
        {
            if(line[i]!=line[i+1]) cont++;
        }
        int solution = 0;
        if(cont==1)
        {
            if(line[0]=='+') solution = 0;
            else solution = 1;
        }
        else
        {
            if(line[n-1]=='+') cont--;
            solution = cont;
        }
        printf("Case #%d: %d\n", t, solution);
    }
}*//*
int main()
{
    int T;
    long long N;
    scanf("%d", &T);
    for(int t = 1; t<=T; t++)
    {
        scanf("%lld", &N);
        if(N==0) printf("Case #%d: INSOMNIA\n", t);
        else
        {
            bitset<10> visited;
            visited.reset();
            long long i = 1;
            while(true)
            {
                long long aux = i*N;
                while(aux!=0)
                {
                    visited[aux%10] = true;
                    aux/=10;
                }
                bool m_break = true;
                for(int i = 0; i<10 && m_break; i++) m_break = (m_break && visited[i]);
                if(m_break) break;
                i++;
            }
            printf("Case #%d: %lld\n", t, i*N);
        }
    }
}
*/
bitset<1000000> bs;
long long sieve_size;
vector<int> primes;

void sieve(long long upperbound)
{
    sieve_size = upperbound + 1;
    bs.set();
    bs[0] = false;
    bs[1] = true;
    for(long long i = 2; i<sieve_size; i++)
    {
        if(bs[i])
        {
            for(long long j = i*i; j<sieve_size; j+=i)
            {
                bs[j] = false;
            }
            primes.push_back((int)i);
        }
    }
}

int isPrime(long long n)
{
    for(int i = 0; i<(int)primes.size(); i++)
        if(n%primes[i]==0) return primes[i];
    return -1;
}
long long bitmask;
int N, J;
int cont;
long long base(int base)
{
    long long S = 0;
    long long aux = bitmask;
    long long pot = 1;
    while(aux!=0)
    {
        if(aux%2) S+=(pot);
        pot*=base;
        aux/=2;
    }
    return S;
}

vector<long long> bitmasks(1000);
vector<int> p[1000];
long long pows[50];
void init()
{
    for(int i = 0; i<1000; i++) p[i].resize(15);

    pows[0] = 1;
    for(int i = 1; i<35; i++) pows[i] = 2*pows[i-1];
}



int main()
{
    int T;
    sieve(150000);
    init();
    scanf("%d", &T);

    for(int t = 1; t<=T; t++)
    {
        cont = 0;
        scanf("%d %d", &N, &J);
        bitmask = 1;
        bitmask += (1<<(N-1));
        for(long long aux = 0; aux<=pows[N-2]-1; aux++)
        {
            long long aux2 = aux;
            bitmask = (1<<(N-1))+(aux2<<1)+1;

            int bases = 0;
            for(int i = 2; i<=10; i++)
            {
                long long number = base(i);
                long long m_p = (long long)isPrime(number);
                if(m_p==number) m_p = -1;
                if(m_p!=-1)
                {
                    p[cont][i] = (int)m_p;
                    bases++;
                }
                else break;
            }
            if(bases==9)
            {
                bitmasks[cont] = bitmask;
                cont++;
            }
            if(cont==J) break;
        }
        bool auxk[50];

        if(cont==J)
        {
            printf("Case #%d:\n", t);
            for(int i = 0; i<J; i++)
            {
                for(int j = 0; j<N; j++)
                {
                    if(bitmasks[i]%2==0) auxk[N-1-j] = false;
                    else auxk[N-1-j] = true;
                    bitmasks[i]/=2;
                }
                for(int j = 0; j<N; j++)
                {
                    if(auxk[j]==false) printf("0");
                    else printf("1");
                }
                for(int j = 2; j<=10; j++) printf(" %d", p[i][j]);
                printf("\n");
            }
        }
    }
}
