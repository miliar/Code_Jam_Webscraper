#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#define INT long long int
using namespace std;
INT t, S[1<<15], C;

void gen(int x, INT N, INT V)
{
    if( x == N )
    {
        S[C++] = V;
        return;
    }
    if( x == 0 || x == N-1 ) gen(x+1, N, V*10+1);
    else gen(x+1, N, V*10), gen(x+1, N, V*10+1);
}

INT conv(INT x, int y)
{
    INT ret = 0, p = 1;
    while( x )
    {
        ret += (x%10)*p;
        x/=10;
        p*=y;
    }
    return ret;
}

bool isPrime(INT x)
{
    for(INT i = 2 ; i*i <= x ; i++ )
        if( x%i == 0 ) return false;
    return x!=1;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("res.txt","w",stdout);
    cin>>t;
    for(int no = 1 ; no <= t ; no++ )
    {
        INT N, J, ANS[11];
        cin>>N>>J;
        C = 0;
        gen(0, N, 0);
        printf("Case #%d:\n", no);
        for(int i = 0 ; i < C && J ; i++ )
        {
            bool flag = true;
            for(int j = 2 ; flag && j <= 10 ; j++ )
            {
                INT val = conv(S[i], j);
                if( isPrime(val) ) flag = false;
                ANS[j] = val;
            }
            if( flag == true )
            {
                cout<<S[i]<<" ";
                for(int j = 2 ; j <= 10 ; j++ )
                {
                    for(int k = 2 ; k*k <= ANS[j] ; k++ )
                        if( ANS[j]%k==0 )
                        {
                            cout<<k<<" ";
                            break;
                        }
                }
                puts("");
                J--;
            }
        }
    }
}




