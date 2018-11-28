#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define PRIME_MAX 100000L
#define MOD 1000002013

using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;

int abs(int i)
{
    if(i<0) return -i;
    else return i;
}
int gcd(int a, int b)
{
    if(b==0) return a;
    else return gcd(b, a%b);
}
vector<int> primes;
void genPrimes()
{
    for(int i=2; i<PRIME_MAX; i++)
    {
        bool prime(true);
        for(int j=0; j<primes.size(); j++)
        {
            if(i % primes[j] == 0)
            {
                prime = false;
                break;
            }
        }
        if(prime)
            primes.push_back(i);
    }
}
bool isPrime(int n)
{
    assert(n <= PRIME_MAX*PRIME_MAX && primes.size() > 0);
    if(n < 2)
        return false;
    for(int i=0; i<primes.size() && primes[i]*primes[i] <= n; i++)
        if(n % primes[i] == 0)
            return false;
    return true;
}
void printCase(int t, ll answer)
{
    cout << "Case #" << t << ": " << answer << endl;
}
int cost(ll o, ll e, ll p, ll N)
{
    ll d = e-o;
    ll unitCost = d*(2*N+1-d)/2;
    ll weighedCost = unitCost%MOD * p;
    //cout << "Distance " << d << " cost " << weighedCost << endl;
    return weighedCost%MOD;
}
// --------------------------------
int main()
{
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        ll N,M;
        cin >> N >> M;
        ll o[1000], e[1000], p[1000];
        ll normalCost(0), betterCost(0);
        set<ll> pos_set;
        for(int i=0; i<M; i++)
        {
            cin >> o[i] >> e[i] >> p[i];
            o[i]--; e[i]--;
            normalCost += cost(o[i], e[i], p[i], N);
            normalCost %= MOD;
            pos_set.insert(o[i]);
            pos_set.insert(e[i]);
        }
        
        ll entered[2000], left[2000], pos[2000];
        map<ll,int> index_pos;
        set<ll>::iterator it;
        int num_pos=0;
        for(it=pos_set.begin(); it!=pos_set.end(); it++)
        {
            index_pos[*it] = num_pos;
            pos[num_pos] = *it;
            num_pos++;
        }
        for(int i=0; i<num_pos; i++)
        {
            entered[i] = left[i] = 0;
        }
        for(int i=0; i<M; i++)
        {
            entered[index_pos[o[i]]] += p[i];
            left[index_pos[e[i]]] += p[i];
        }
        for(int i=0; i<num_pos; i++)
        {
            // We just compensate the leaving ones with previous entered ones.
            for(int j = i; j>=0 && left[i]>0; j--)
            {
                ll pass = min(entered[j], left[i]);
                if(pass>0)
                {
                    //cout << "Buying tickets on " << pos[j] << pos[i] << endl;
                    betterCost += cost(pos[j], pos[i], pass, N);
                    betterCost %= MOD;
                    entered[j] -= pass;
                    left[i] -= pass;
                }
            }
            assert(left[i] == 0);
        }
        //cout << normalCost << " " << betterCost << endl;
        printCase(t,(normalCost+MOD-betterCost)%MOD);
    }
}
