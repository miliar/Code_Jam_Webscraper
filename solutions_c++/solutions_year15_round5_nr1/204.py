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
{vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);
    R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
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

vector<pair<uint64, uint64>> data;
vector<vector<uint64>> childs;
vector<bool> need_remove;
vector<bool> take_back;
vector<bool> removed;

size_t remove(size_t who) {
    queue<size_t> qq;
    qq.push(who);
    size_t r = 0;
    while (!qq.empty()) {
        size_t w = qq.front();
        qq.pop();
        if (!removed[w]) {
            removed[w] = true;
            r += 1;
            for (auto c : childs[w]) {
                qq.push(c);
            }
        }
    }
    return r;
}

size_t take(size_t who) {
    queue<size_t> qq;
    qq.push(who);
    size_t r = 0;
    while (!qq.empty()) {
        who = qq.fron();
        if (!removed[who] || need_remove[who] || removed[data[who].second]) {
            return 0;
        }
        removed[who] = false;
        size_t r = 1;
        for (auto c : childs[who]) {
            r += take(c);
        }
    }
    return r;
}

int main(void) {
	int __number_of_cases;
	cin >> __number_of_cases;
	REP(__number_of_case, __number_of_cases) {
        uint64 N, D;
        cin >> N >> D;
        uint64 S0, As, Cs, Rs, M0, Am, Cm, Rm;
        cin >> S0 >> As >> Cs >> Rs >> M0 >> Am >> Cm >> Rm;
        data.resize(N);
        childs.clear();
        childs.resize(N);
        need_remove.assign(N, false);
        take_back.assign(N, false);
        removed.assign(N, false);
        data[0].first = S0;
        data[0].second = M0;
        FOR(i, 1, N-1) {
            data[i].first = (data[i - 1].first * As + Cs) % Rs;
            data[i].second = (data[i - 1].second * Am + Cm) % Rm;
        }
        data[0].second = -1;
        //cerr << data << endl;
        FOR (i, 1, N - 1) {
            data[i].second %= i;
        }
        vector<int> by_salary(N);
        REP(i, N) {
            by_salary[i] = i;
        }
        //cerr << data << endl;
        sort(by_salary.begin(), by_salary.end(), [](int a, int b) -> bool {return data[a].first < data[b].first;});
        //cerr << by_salary << endl;
        //sort(data.begin(), data.end());
        uint64 ceo_id;
        REP(i, N) {
            if (data[i].second != (uint64)-1) {
                childs[data[i].second].push_back(i);
            }
            else {
                ceo_id = i;
            }
        }
        //cerr << childs << endl;
        size_t left = 0; size_t right = N - 1;
        size_t res = 0;
        size_t l, r;
        while (data[by_salary[left]].first + D < S0) {
            l = by_salary[left];
            need_remove[l] = true;
            res += remove(l);
            ++left;
        }
        while (data[by_salary[right]].first > data[by_salary[left]].first + D) {
            r = by_salary[right];
            need_remove[r] = true;
            res += remove(r);
            --right;
        }
        //cerr << "baseline: " << left << ' ' << right << ' ' << res << endl;
        size_t answer = res;
        while (data[by_salary[left]].second != (uint64)(-1)) {
            l = by_salary[left];
            need_remove[l] = true;
            res += remove(l);
            ++left;
            while (right < N && data[by_salary[right]].first <= data[by_salary[left]].first + D) {
                r = by_salary[right];
                need_remove[r] = false;
                take_back[r] = true;
                res -= take(r);
                ++right;
            }
            remin(answer, res);
        }
		cout << "Case #" << __number_of_case+1 << ": " << N - answer << endl;
	}
    return 0;
}
