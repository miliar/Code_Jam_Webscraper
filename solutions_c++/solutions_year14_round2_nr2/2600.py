#include <bits/stdc++.h>

#define REP(i,a,t)           for (int i = (a) ;i <= (t) ;i++)
#define RREP(i,n,b)          for (int i = (n) ;i >= (b) ;i--)
#define TRvii(c, it)         for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define ull                  unsigned long long
#define ll                   long long
#define ld                   long double
#define pb                   push_back
#define szo(v)               sizeof(v)
#define all(c)               (c).begin(), (c).end()

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef map<int, int> mii;
typedef pair<int, int> ii;
typedef vector<ii> vii;

vector< pair<long, long> >ad;

int main(void) {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    long a, b, k;

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        set <pair<long, long> > newad;
        scanf("%ld %ld %ld", &a, &b, &k);
        for (long j = 0; j < a; j++) {
            for (long l = 0; l < b; l++) {
                long x = j&l;
                if (x < k)
                    newad.insert(pair<long, long>(j, l));
            }

        }
        printf("Case #%d: %ld\n", (i + 1), newad.size());
    }


    return 0;
}