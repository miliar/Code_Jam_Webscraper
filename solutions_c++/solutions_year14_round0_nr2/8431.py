#include <iostream>
#include <iomanip>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
typedef unsigned long long ui64;
const ui64 N_PRIMES = 10000;
vector<ui64> primes;

// For bit set iteration of all subsets or k-subsets for smaller numbers
vector<int> getElements(long long x)
{
    vector<int> v;
    while (x) {
    	int fsb = ffsll(x);
    	v.push_back(fsb);
    	x = x & ~(1 << (fsb-1));
    }
    return v;
}

void loop_through_exact_k_elements()
{
    int k = 3, N = 4; // k and N defined here
    int MX = 1ULL << N;
    int s = (1ULL << k) - 1;
    while (s <= MX)
    {
	// get indices of the set bits => elements of interest
	vector<int> vc = getElements(s);
	for (int i = 0; i < vc.size(); ++i) {
	    cout << vc[i] << ", ";
	}
	cout << endl;
    	long long fsb = ffsll(s);
    	long long fz_left_fsb =  (s + fsb) & ~s; 
    	long long fs_right_fz_left_fsb = fz_left_fsb >> 1;
    	s = s | fz_left_fsb;
    	s = s & ~fs_right_fz_left_fsb;
    }
}

void loop_through_all_elements()
{
    int N = 4;
    for (int s = 1; s <= 4; ++s) {
	vector<int> vc = getElements(s);
	for (int i = 0; i < vc.size(); ++i) {
	    cout << vc[i] << ", ";
	}
	cout << endl;
    }
}
// bit set manipulation functions end

// Number thoery related algorithms
ui64 gcd(ui64 a, ui64 b) {
    if (a < b) swap(a, b);
    if (b == 0)
	return a;
    return (b, a%b);
}

ui64 lcm(ui64 a, ui64 b) {
    return (a*b)/gcd(a, b);
}

bool isPrime(ui64 p) {
    ui64 root = (ui64)floor(sqrt(p));
    for (ui64 i = 0; i < primes.size(); ++i) {
    	if (p%primes[i] == 0) { 
	    return false;
    	}
	if (primes[i] > root) {
	    break;
	}
    }
    return true;
}

void populate_primes()
{
    primes.push_back(2);
    primes.push_back(3);
    ui64 last_checked = 3;
    // Fill all primes less than N 
    for (ui64 i = 5; i < N_PRIMES; i = i + 2) {
	if (isPrime(i)) {
	    // cout << i << endl;
	    primes.push_back(i);
	}
    }
}

// Compute x^n in log(n) complexiety
ui64 fast_exp(ui64 x, ui64 n)
{
    if (n == 0) return 1;
    if (n == 1) return x;
    if (n%2) return x*fast_exp(x*x, (n-1)/2);
    else return fast_exp(x*x, n/2);
}

int main()
{
    // loop_through_exact_k_elements();
    // loop_through_all_elements();
    // populate_primes();
    // cout << "Number of primes less than " << N_PRIMES << " with last prime as " << primes[primes.size()-1] << endl;
    // ui64 r = fast_exp(2, 63);
    freopen ("in", "r", stdin);
    freopen ("out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
	double C, F, X;
	cin >>  C >> F >> X;
	double p0 = X/2;
	double p1 = C/2 + X/(2+F);
	for (ui64 i = 1; ; ++i) {
	    if (p1 > p0) {
		cout << "Case #" << t << ": " << fixed << setprecision(9) << showpoint << p0 << endl;
		break;
	    }
	    p0 = p1;
	    p1 = p1 - X/(2+i*F) + C/(2+i*F) + X/(2+ (i+1)*F);
	    // cout << "i = " << i << " :: " << p0 << ", " << p1 << endl;
	}
    }
    return 0;
}
