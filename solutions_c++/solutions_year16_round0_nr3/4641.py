#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int N = 16;
const int J = 50;

long long nbs[(1<<(N-2))+1][N];

int curNb[N];

int cpt = 0;


void gen(int pos)
{
    if (pos == N-1)
    {
        for (int i = 0; i < N; i++)
            nbs[cpt][i] = curNb[i];
        cpt++;
    }
    else
    {
        curNb[pos] = 0;
        gen(pos+1);
        curNb[pos] = 1;
        gen(pos+1);
    }
}

const long long truc = 200000001;
std::vector<long long> primeList;
bool isNotPrime[truc];

long long certif[11];

int getFactor(int iNb, long long base)
{
    long long nb = 0;
    for (int i = 0; i < N; i++)
    {
        nb *= base;
        nb += nbs[iNb][i];
    }

    long long maxi = sqrt(nb+1)+1;

    for (long long x = 2; x <= maxi; x++)
        if (nb%x == 0)
            return x;
    return -1;
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    //freopen("tin", "r", stdin);
    freopen("t.out", "w", stdout);

    curNb[0] = 1;
    curNb[N-1] = 1;
    primeList.reserve(10000000);

    /*isNotPrime[0] = true;
    isNotPrime[1] = true;

    primeList.push_back(2);
    for (int i = 3; i < truc; i+=2)
    {
        if (!isNotPrime[i])
        {
            for (int j = 2*i; j < truc; j+=i)
                isNotPrime[j] = true;
            primeList.push_back(i);
        }

    }*/




    gen(1);

    int nbT = 1;

    int nbDone = 0;


    for (int t = 1; t <= nbT; t++)
    {

        cout << "Case #" << t << ":\n";


        for (int i = 0; i < cpt && nbDone < J; i++)
        {
            bool isOk = true;
            for (int base = 2; base <= 10; base++)
            {
                certif[base] = getFactor(i, base);
                if (certif[base] == -1)
                {
                    isOk = false;
                    break;
                    //cout << "LOL" << endl;
                }
            }
            if (isOk)
            {
                for (int j = 0; j < N; j++)
                    cout << nbs[i][j];
                for (int base = 2; base <= 10; base++)
                    cout << ' ' << certif[base];
                cout << endl;
                nbDone++;
                //cout << "LAL" << endl;
            }

        }


       // cout << rep << '\n';
    }


    return 0;
}
