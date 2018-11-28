//Krzysztof Pieprzak
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef pair<long long, long long> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

#define Size(x) (int)x.size()
#define VAR(v,n) typeof(n)v = (n)
#define FOR(i,a,b) for(VAR(i,a); i < (b); ++i)
#define FORE(i,a,b) for(VAR(i,a); i <= (b); ++i)
#define FORREV(i,a,b) for(VAR(i,b); i >= (a); --i)
#define FORSTEP(i,a,b,step) for(VAR(i,a); i < (b); i += (step))
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define FOREACHS(i,c,n) for(VAR(i,&(c)[0]); i-(c)<(n); ++i)
#define ALL(x) x.begin(),x.end()
#define CLEAR(t) memset(t, 0, sizeof(t))
#define F first
#define S second
#define MP make_pair
#define PUB push_back
#define POB pop_back
#define pieprzu ios_base::sync_with_stdio(0);

const int    INF = 1000000001;
const double EPS = 10e-9;

void rob(int test)
{
    int x,r,c;
    scanf("%d %d %d", &x, &r, &c);

    printf("Case #%d: ", test);
    if (x == 1)
    {
        printf("GABRIEL");
    }
    else if (x == 2)
    {
        if ((r*c)%2 == 0)
            printf("GABRIEL");
        else
            printf("RICHARD");
    }
    else if (x == 3)
    {
        //2x3, 3x2, 3x3, 3x4, 4x3
        if (r > c) swap(r,c);
        if ((r == 2 && c == 3) || (r == 3 && c == 3) || (r == 3 && c == 4))
            printf("GABRIEL");
        else
            printf("RICHARD");
    }
    else if (x == 4)
    {
        //3x4, 4x3, 4x4
        if (r > c) swap(r,c);
        if ((r == 3 || r == 4) && c == 4)
            printf("GABRIEL");
        else
            printf("RICHARD");
    }

    printf("\n");
}

int main()
{
    int test = 1;
    scanf("%d", &test);

    FORE (i, 1, test) rob(i);

    return 0;
}
