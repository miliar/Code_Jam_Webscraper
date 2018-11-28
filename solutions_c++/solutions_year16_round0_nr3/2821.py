#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

ll addOne(ll current){

    ll multiplier = 1;
    ll added = current + 1;

    while(((added/multiplier)%10)>1) {
        added -= multiplier * ((added/multiplier)%10);
        multiplier *= 10;
        added += multiplier;
    }
    return added;
}

ll valueinBase(ll current, int base){
    ll valu = 0;
    ll multiplier = 1;
    ll divisor = 1;

    while(current/divisor > 0){
        valu += ((current/divisor)%10) * multiplier;
        multiplier *= base;
        divisor *= 10;
    }
    return valu;
}

ll getDivisor(ll current, int primes[], int primeCount){
    ll ans = 0;

    for(int i=0;i<primeCount;i++){
        if(current%primes[i] == 0 && current!=primes[i]){
            ans = primes[i];
            break;
        }
    }

    return ans;
}

int main(void){
    freopen("D:/Code/C-small-attempt0.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    //Get Top 10k Prime is enough?
    int maxprimeCount = 10000;
    int primes[maxprimeCount];
    int primeCount = 0;

    int maxsieve = 1000000;
    bool sieve[maxsieve];
    reset(sieve,0);

    sieve[0] = sieve[1] = true;
    for(int i=2;i<maxsieve;i++){
        if(!sieve[i]) {
            primes[primeCount] = i;
            primeCount++;
            if(primeCount>maxprimeCount) break;
            for(int ii=0;ii<(maxsieve/i);ii++) {
                sieve[i*ii] = true;
            }
        }
    }

    FOR(i,tc)
    {
        int n,j;
        sci(n);
        sci(j);

        cout << "Case #" << i+1 << ": " << endl;

        ll start = 1;
        for(int ii=1;ii<n;ii++) {
            start *= 10;
        }
        ll finish = start * 10;
        start++;

        while(j>0 && start < finish) {

            bool allNonPrime = true;

            for(int ii=2;ii<=10;ii++) {
                ll divisor = getDivisor(valueinBase(start,ii),primes,maxprimeCount);
                if(divisor == 0){
                    allNonPrime = false;
                    break;
                }
            }

            if(allNonPrime) {
                cout << start;

                for(int ii=2;ii<=10;ii++) {
                    ll divisor = getDivisor(valueinBase(start,ii),primes,maxprimeCount);
                    cout << " " << divisor;
                }

                cout << endl;
                j--;
            }

            start = addOne(start);
            start = addOne(start);
        }
    }


    return 0;
}
