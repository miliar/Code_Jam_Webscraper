#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

struct hiker
{
    long long pos, vel;
} ;
vector<hiker> a;

void load_group()
{
    int pos, d, m;
    scanf("%i %i %i", &pos, &d, &m);
    while(d--)
    {
        a.push_back({pos, m});
        m++;
    }
}

int main()
{
    freopen("C-small-1-attempt1.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int test;
    scanf("%i", &test);

    for(int tt = 1; tt <= test; tt++)
    {
        int n;
        scanf("%i", &n);
        a.clear();
        while(n--) load_group();

        int res;
        if(a.size() < 2) res = 0;
        else
        {
            long long t1 = (360LL - a[0].pos) * a[0].vel, t2 = (360LL - a[1].pos) * a[1].vel;
            if(t1 < t2) swap(a[0], a[1]);
            if((360LL - a[0].pos) * a[0].vel < (720LL - a[1].pos) * a[1].vel) res = 0;
            else res = 1;
        }
        printf("Case #%i: %i\n", tt, res);
    }

    return 0;
}
