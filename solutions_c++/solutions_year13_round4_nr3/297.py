#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

bool visit[2050];
int mizq[2050];
int mder[2050];
int X[2050], A[2050], B[2050];

int aux[2050];
bool ok;
int n;

void intento(int val, int pos)
{
    // cout << val << " -- " << pos << endl;

    if ( val == n )
    {
        ok = true;
        return;
    }

    int ni, nd, k;
    int kizq, kder;

    ni = mizq[pos] + 1;
    nd = mder[pos] + 1;
    k = pos;

    while ( k < n && mizq[k] < ni )
    {
        mizq[k] = ni;
        if ( !visit[k] )
            A[k] --;
        k ++;
    }
    kizq = k;

    k = pos;

    while ( k >= 0 && mder[k] < nd )
    {
        mder[k] = nd;
        if ( !visit[k] )
            B[k] --;
        k --;
    }

    kder = k;

    X[pos] = val;
    visit[pos] = true;

    for ( int i = 0; i < n; i ++ )
    {
        if ( visit[i] ) continue;
        if ( A[i] == 0 && B[i] == 0 )
        {
            intento(val + 1, i);
            if ( ok ) return;
        }
    }

    visit[pos] = false;
    X[pos] = 0;

    ni = mizq[pos] - 1;
    nd = mder[pos] - 1;
    k = pos;

    while ( k < kizq )
    {
        mizq[k] = ni;
        if ( !visit[k] )
            A[k] ++;
        k ++;
    }

    k = pos;

    while ( k > kder )
    {
        mder[k] = nd;
        if ( !visit[k] )
            B[k] ++;
        k --;
    }
}

int main()
{
    freopen ( "c.in", "r", stdin );
    freopen ( "SmallC.out", "w", stdout );

    int ntc, tc = 0;

    cin >> ntc;

    while ( ntc -- )
    {
        tc ++;

        cin >> n;

        for ( int i = 0; i < n; i ++ )
        {
            cin >> A[i];
            A[i] --;
        }

        for ( int i = 0; i < n; i ++ )
        {
            cin >> B[i];
            B[i] --;
        }

        memset ( mizq, 0, sizeof(mizq) );
        memset ( mder, 0, sizeof(mder) );
        memset ( visit, false, sizeof(visit) );
        memset ( X, 0, sizeof(X) );
        memset ( aux, 0, sizeof(aux) );

        ok = false;

        for ( int j = 0; j < n; j ++ )
                if ( A[j] == 0 && B[j] == 0 )
                    intento(1, j);

        cout << "Case #" << tc << ":";

        for ( int i = 0; i < n; i ++ )
            cout << " " << (X[i]?X[i]:n);
        cout << endl;
    }
}
