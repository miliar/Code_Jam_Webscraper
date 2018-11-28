#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <cassert>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

typedef long long tint;

int main()
{
    int TT; scanf("%d", &TT);
    forn(tt,TT)
    {
        tint N, X; cin >> N >> X;
        multiset<tint> s;
        forn(i,N)
        {
            tint x; cin >> x;
            s.insert(x);
        }
        int ret = 0;
        while (!s.empty())
        {
            ret++;
            tint A = *s.begin(); s.erase(s.begin());
            if (!s.empty())
            {
                tint maxB = X - A;
                multiset<tint>::iterator it = s.upper_bound(maxB); // Primero que no sirve
                if (it != s.begin())
                {
                    it--;
                    assert(A + *it <= X);
                    s.erase(it);
                }
            }
        }
        printf("Case #%d: %d\n" , tt+1, ret);
    }
    return 0;
}

