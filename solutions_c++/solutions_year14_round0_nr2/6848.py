#include <iostream>

#define fo(a,b,c) for(a = (b); a < (c); a++)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))

using namespace std;

double do_thing(double c, double f, double x, double rate, double limit)
{
    int i;
    double time = 0;
    fi(limit+1)
    {
        double norm_time = x/rate;
        double castle_time = c/rate;
        double hosa_rate = rate + f;
        double hosa_time = x/hosa_rate;

        if(castle_time + hosa_time >= norm_time)
            return norm_time+time;
        
        time += castle_time;
        rate += f;
    }
}

int main()
{
    int i, j, k, t, tt;
    double c, f, x, p;
    double rate, time;

    cin >> tt;

    for(t=1; t<=tt; t++)
    {
        p = 2;
        time = 0;
        rate = p;
        cin >> c >> f >> x;
        float worst = x/p;
        float limit = 2*worst/c+1;

        printf("Case #%d: ", t);
        printf("%.7f", do_thing(c, f, x, rate, limit));
        printf("\n");

    }

    return 0;
}
