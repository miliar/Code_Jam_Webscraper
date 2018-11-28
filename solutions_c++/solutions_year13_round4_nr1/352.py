#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#define MOD 1000002013LL

using namespace std;

class event {
public:
    char type; // 0 - ulazak, 1 - izlazak
    long long when;
    long long p;
    event () {}
    event (char t, long long w, long long _p) :
        type(t), when(w), p(_p) {}
};

bool operator < (const event &a, const event &b) {
    if (a.when != b.when) return a.when < b.when;
    return a.type < b.type;
}

long long N, M;
vector <event> E;
multiset <pair <long long, long long>, greater< pair <long long, long long> > > tickets; // (ulaz, broj_ljudi)

long long price(long long broj_stanica, long long p) {
    return (((broj_stanica*N - (broj_stanica*(broj_stanica-1))/2) % MOD) * p) % MOD;
}

void debug() {
    for (set <pair <long long, long long> >::iterator itr = tickets.begin(); itr != tickets.end(); ++itr) {
        printf("(%lld, %lld), ", itr->first, itr->second);
    }
    printf("\n");
}

int main() {
    int T;
    scanf("%d", &T);

    long long normal_price, reduced_price;

    for (int tt = 1; tt <= T; ++tt) {
        scanf("%lld%lld", &N, &M);
        E.clear();
        tickets.clear();
        normal_price = 0;
        reduced_price = 0;

        for (int i = 0; i < M; ++i) {
            long long a, b, c;
            scanf("%lld%lld%lld", &a, &b, &c);
            normal_price = (normal_price + price(b-a, c)) % MOD;

            E.push_back(event(0, a, c));
            E.push_back(event(1, b, c));
        }

        sort(E.begin(), E.end());

        long long unutra = 0;
        for (int i = 0; i < E.size(); ++i) {
            if (E[i].type == 0) { // ulaz
                tickets.insert(make_pair(E[i].when, E[i].p));
                unutra += E[i].p;
            } else {
                long long broj_ljudi = E[i].p;
                unutra -= broj_ljudi;

                while (broj_ljudi) {
                    pair <long long, long long> t = *tickets.begin();
                    tickets.erase(tickets.begin());
                    if (t.second >= broj_ljudi) {
                        reduced_price = (reduced_price + price(E[i].when - t.first, broj_ljudi)) % MOD;
                        t.second -= broj_ljudi;
                        tickets.insert(t);
                        broj_ljudi = 0;
                    } else {
                        reduced_price = (reduced_price + price(E[i].when - t.first, t.second)) % MOD;
                        broj_ljudi -= t.second;
                    }
                }
            }
        }

        long long sol = (normal_price + MOD - reduced_price) % MOD;
        printf("Case #%d: %lld\n", tt, sol);
    }
    return 0;
}
