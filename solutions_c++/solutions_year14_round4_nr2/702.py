/*
 * Template for code jam - different includes and templates
 * Real task code is in the end
 * Mikhail Dektyarow <mihail.dektyarow@gmail.com>, 2009
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <sstream>
#include <numeric>
#include <stack>
#include <bitset>
#include <iostream>
#include <string>
using namespace std;

/*
 * DEFINES
 */
#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

/*
 * Types
 */
typedef pair<int,int> ipair;
typedef long long int int64;
typedef unsigned long long uint64;

/*
 * Different useful templates
 */
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<class T1, class T2>inline istream& operator>> (istream& s, pair<T1, T2> &p) {	return s >> p.first >> p.second;}
template<class T1, class T2>inline ostream& operator<< (ostream& s, const pair<T1, T2>p) {	return s << "(" << p.first << " " << p.second << ")";}
template<class T1>inline ostream& operator<< (ostream& s, const vector<T1> container) {
	for (typename vector<T1>::const_iterator i = container.begin(); i != container.end(); i++) s << *i << " ";
	return s;
}
template<class T1>inline istream& operator>> (istream&s, vector<T1> &container) {
	for (typename vector<T1>::iterator i = container.begin(); i != container.end(); i++) s >> *i;
	return s;
}
/*
 * Euclide's algorithm
 */
template<class T> inline T euclide(T a,T b,T &x,T &y)
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
/*
 * Factorizing a number
 */
template<class T> inline vector<pair<T,int> > factorize(T n)
{vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline bool isPrimeNumber(T n)
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
//Searching prime numbers
//Using Sieve of Atkin (http://en.wikipedia.org/wiki/Sieve_of_Atkin)
vector<int> gen_primes(int limit) {
	int sqr_lim;
	int x2, y2;
	int n;
	vector<bool> is_prime(limit+1, false);
	sqr_lim = (int)sqrt((long double)limit);
	is_prime[2] = true;
	is_prime[3] = true;
	x2 = 0;
	for (int i = 1; i <= sqr_lim; i++) {
		x2 += 2 * i - 1;
		y2 = 0;
		for (int j = 1; j <= sqr_lim; j++) {
			y2 += 2 * j - 1;
			n = 4 * x2 + y2;
			if ((n <= limit) && (n % 12 == 1 || n % 12 == 5))
				is_prime[n] = !is_prime[n];
			n -= x2;
			if ((n <= limit) && (n % 12 == 7))
				is_prime[n] = !is_prime[n];
			n -= 2 * y2;
			if ((i > j) && (n <= limit) && (n % 12 == 11))
				is_prime[n] = !is_prime[n];
		}
	}
	for (int i = 5; i <= sqr_lim; i++) {
		if (is_prime[i]) {
			n = i * i;
			for (int j = n; j <= limit; j += n) {
				is_prime[j] = false;
			}
		}
	}
	int primes_count = 0;
	for (int i = 2; i < limit; i++) primes_count += is_prime[i];
	vector<int> primes;
	primes.reserve(primes_count);
	for (int i=2; i < limit; i++) if (is_prime[i]) primes.push_back(i);
	return primes;
}
//Translating string to different types
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt(
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt64(
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(

/*
 * Real code
 */

int test_perm(vector<int> A, vector<int> M) {
    vector<int> nv;
    REP(i, A.size()) {
        nv.push_back(A[M[i]]);
    }
    bool was_c = false;
    int prev = -100;
    /*if (nv[0] == 1 && nv[1] == 8 && nv[2] == 10) {
        cout << nv << '\n';
    }*/
    int ind, kk(0);
    for (int a : nv) {

        if (was_c && a < prev || !was_c && a > prev) {
            prev = a;
        }
        else {
            if (was_c) {
                return 99999;
            }
            was_c = true;
            ind = kk;
        }
        prev = a;
        ++kk;
    }
    int r = 0;
    REP(i, M.size()) {
        FOR(j, i + 1, M.size() - 1) {
            r += M[i] > M[j];
        }
    }
    /*REP(i, M.size()) {
        FOR(j, i, M.size() - 1) {
            if (M[j] == i) {
                r += (j - i);
                FORD(k, j, i + 1) {
                    M[k] = M[k-1];
                }
            }
        }
    }*/
    /*if (nv[0] == 1 && nv[1] == 8 && nv[2] == 10) {
        cout << r << '\n';
    }*/
    return r;
}

int perm_pos(vector<int> A, int m) {
    int max_pos = 0;
    REP(i, A.size()) {
        if (A[i] > A[max_pos])
            max_pos = i;
    }
    int step = m > max_pos ? 1 : -1;
    for (int i = max_pos; i != m; i += step) {
        swap(A[i], A[i+step]);
    }
    int r((m - max_pos) * step);
    for (int i = 0; i < m; ++i) {
        for (int j = i + 1; j < m; ++j)
            r += A[i] > A[j];
    }
    for (int i = m + 1; i < A.size(); ++i)
        for (int j = i + 1; j < A.size(); ++j)
            r += A[i] < A[j];
    return r;
}

int solve1(vector<int> A) {
    int cleft = 0, cright = A.size() - 1;
    int r = 0;
    while (cleft != cright) {
        int min_pos = cleft;
        FOR(i, cleft, cright) {
            if (A[i] < A[min_pos]) {
                min_pos = i;
            }
        }
        int dir_left = min_pos - cleft < cright - min_pos ? -1 : 1;
        r += min(min_pos - cleft, cright - min_pos);
        for (int i = min_pos; i != cleft && i != cright; i += dir_left)
            swap(A[i], A[i + dir_left]);
        if (dir_left == -1)
            cleft++;
        else
            cright--;
    }
    return r;
}

int main(void) {
	int __number_of_cases;
	cin >> __number_of_cases;
	REP(__number_of_case, __number_of_cases) {
        int N;
        cin >> N;
        vector<int> A(N);
        cin >> A;
        //vector<int> M(N);
        //REP(i, N) {
            //M[i] = i;
        //}
        /*int ans = 99999;
        vector<int> best_perm;
        do {
            int a = test_perm(A, M);
            if (a < ans) {
                best_perm = M;
            }
            ans = min(ans, test_perm(A, M));
        } while (next_permutation(M.begin(), M.end()));
        cout << best_perm << '\n';*/
        /*REP(m, N)
            ans = min(ans, perm_pos(A, m));*/
		//cout << "Case #" << __number_of_case+1 << ": " << ans << '\n';
        cout << "Case #" << __number_of_case+1 << ": " << solve1(A) << '\n';
	}
}
