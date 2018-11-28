#include <bits/stdc++.h>

using namespace std;

typedef double D;
typedef long double LD;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<LD,LD> PLD;

#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(x) (x).begin(), (x).end()

vector<bool> table(2501,false);

int main()
{  
    int T;
    scanf("%d",&T);
    for(int i = 1; i<=T; ++i)
    {
        int N;
        scanf("%d",&N);
        for(int j = 0; j<2*N-1; ++j)
        {
            for(int k = 0; k<N; ++k)
            {
                int x;
                scanf("%d",&x);
                table[x] = !table[x];
                //printf(" %d \n",x);
            }
        }
        printf("Case #%d:",i);
        for(int j = 0; j<2501; ++j)
        {
            if( table[j] ) printf(" %d", j), table[j] = false;
        }
        printf("\n");
    }  
}


