#include <math.h>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <memory.h>
#define mp make_pair
#define pb push_back
#define forn(i,a,b) for( int (i) = a; (i) <= b; (i)+=1 )
#define forb(i,a,b) for( int (i) = a; (i) >= b; (i)-=1 )

using namespace std;

long long gcd(long long a, long long b)
{
    if(a%b == 0) return b;
    return gcd(b, a%b);
}

int main()
{
    freopen("out.txt", "w", stdout);
    int t, ca = 0;
    cin >> t;
    while(t--)
    {
        ca ++;
        char c;
        long long P, Q;
        cin >> P >> c >> Q;
        long long g = gcd(P,Q);
        P/=g;
        Q/=g;
        long long tmp = Q;
        while(tmp)
        {
            if(tmp % 2 && tmp != 1) {tmp = 3; break;}
            tmp/=2;
        }
        if(tmp != 0) { printf("Case #%d: impossible\n", ca); continue;}
        long long ans = 0;
        while(P < Q)
            Q /= 2,
            ans++;
        if(ans > 40)printf("Case #%d: impossible\n", ca);
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
