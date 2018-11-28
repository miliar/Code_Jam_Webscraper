/*****************************************************************************************/
/*																		     			 */
/*  					Adarsh Pugalia 										 			 */
/*																			 			 */
/*****************************************************************************************/
 
#include <bits/stdc++.h>

/* Data types and structures. */
#define ll long long int
#define llu long long int unsigned
#define vi vector <int>
#define vl vector <ll> 
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vpii vector <pii >
#define vpll vector <pll >
 
/* Data structure helpers. */ 
#define f first
#define s second
#define pb push_back
#define pob pop_back
#define mp make_pair
#define sz(n) (int)n.size()-1
#define all(n) n.begin(), n.end()
#define has(it,s) if(it!=s.end())
 
/* Input output defines. */
#define sd(n) scanf("%d", &n)
#define sl(n) scanf("%lld", &n)
#define slf(n) scanf("%lf", &n) 
#define pd(n) printf("%d", n);
#define pl(n) printf("%lld", n);
#define plf(n) printf("%0.9lf", n);
#define ps printf(" ")
#define pe printf("\n")

/* loops */
#define rep(i,j,k) for(int i=j; i<=k; i++)
#define repd(i,j,k) for(int i=j; i>=k; i--)
#define iter(it, s) for(auto it=s.begin(); it!=s.end(); it++)

/* constraints. */ 
#define max_size 105
#define max_sieve_size 100000000
#define max_sieve_size3 43046721
#define max_sieve_size2 65536
#define max_matrix_size 100
#define max_log 17
#define INF 1000000000000000000
#define MOD 1000000007
#define EPS 0.0000000001
#define GCD_EPS 0.0001
#define PI 3.14159265358979323846
#define mod(a) ((a)%MOD)

#define bcnt __builtin_popcount 

ll ciel(double a) { ll ret = a; if(a-ret>EPS) ret++; return ret; }
ll gcd(ll a, ll b) { if(a<b)return gcd(b, a); if(a%b==0)return b; return gcd(b, a%b); }
ll pow(ll n, ll p) {if(p==0)return 1; if(n<=1)return n;ll res = 1;while(p){if(p&1) res = mod(res*n);n = mod(n*n);p /= 2;} return res;}

double fgcd(double a, double b) { if(fabs(a)<fabs(b)) return fgcd(b, a); if(fabs(b)<GCD_EPS) return a; return fgcd(b, fmod(a,b)); }

bool db_db_cmp(double a, double b) { return (a+EPS>b && a-EPS<b); }
bool db_ll_cmp(double a, ll b) { bool ret = (a+EPS>b && a-EPS<b); if(ret) return ret; b++; return (a+EPS>b && a-EPS<b); }
 
using namespace std;

/* This function calculates primes upto the given max_sieve_size. */
int sieve[max_sieve_size];
vector<ll> primes;
void calc_sieve()
{
    for(int i=0; i<max_sieve_size; i++)
        sieve[i] = 0;
 
    sieve[0] = sieve[1] = -1;
 
    for(int i=2; i<max_sieve_size; i++)
    {
        if(sieve[i]==0)
        {
        	primes.pb(i);
            for(int j=i+i; j<max_sieve_size; j=j+i)
            {
                sieve[j] = i;
            }
        }
    }
}

void preprocess() {
	calc_sieve();
}

ll bin[16];
vector<ll> v;

void init() {
}

void solve(int test_case) {
	init();
	cout<<"Case #"<<test_case<<":\n";

	int total = 0, total2 = 0;
	for(int i=32769; i<max_sieve_size2; i+=2) {
		//cout<<i<<" "<<total<<endl;
		v.clear();
		if(sieve[i]) {
			//cout<<"here0\n";
			v.pb(sieve[i]);

			int pos = 15;
			ll temp = i;
			while(pos>=0) {
				bin[pos] = temp%2;
				temp /= 2;
				pos--;
			}

			//cout<<"here1\n";

			int flag = 0;
			rep(j,3,10) {
				ll cur = 0;
				ll mul = 1;
				repd(k,15,0) {
					cur += mul*bin[k];
					mul *= j;
				}

				if(cur<max_sieve_size) {
					if(sieve[cur])
						v.pb(sieve[cur]);
					else {
						flag = 1;
						break;
					}
				}
				else {
					int flag2 = 1;
					for(int k=0; primes[k]*primes[k]<=cur && k<primes.size(); k++) {
						if(cur%primes[k]==0) {
							flag2 = 0;
							v.pb(primes[k]);
							break;
						}
					}

					if(flag2) {
						flag = 1;
						break;
					}
				}
			}

			//cout<<"here2\n";

			if(!flag) {
				total++;
				rep(i,0,15)
					cout<<bin[i];

				cout<<" ";
				rep(i,0,sz(v)) {
					cout<<v[i]<<" ";
				}
				cout<<endl;
			}

			if(total==50)
				break;
		}
	}
}

int main() {
	preprocess();
	int t = 1;
	//sd(t);
	ll n, j;
	cin>>n>>j;
 
	rep(i,1,t) {
		solve(i);
	}
	return 0;
}
