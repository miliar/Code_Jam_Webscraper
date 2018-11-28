/* Author: Ankit Sultana
 * Comment: All hail my template. Some of the code inspired from:
 *          https://www.hackerrank.com/contests/codeagon2015/challenges/mulseg/editorial
 * * * * * * * * * * * * * */
#include <iostream>
#include <cassert>
#define LL long long
#define MAXN 16
#define MAXJ 50
#define IS_64BIT_ARCH (sizeof(unsigned long) == sizeof(LL))

using namespace std;

/* Miller Rabbin,
 * Complexity: O(k * log2^3(n))
 * * * * * * * * * * * */
inline LL multiply(LL a, LL b, const LL &m)
{
	a %= m, b %= m;
	long double res = a;res *= b;
	LL c = (LL)(res/m);
	a *= b, a -= c*m, a %= m;
	if(a < 0)
		a += m;
	return a;
}

inline LL power(LL a, LL b, const LL &m)
{
	LL ans = 1;
	while(b) {
		if(b & 1) {
			ans = multiply(ans, a, m);
		}
		a = multiply(a, a, m);
		b >>= 1;
	}
	return ans;
}

// Returns true if p is prime
inline bool Miller(LL p) {
	int b[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
	if(p < 2)	return false;
	if(p != 2 && !(p&1))	return false;
	for(int i = 0; i < 25; i++) {
		if(p == b[i])	return true;
		else if(p % b[i] == 0)	return false;
	}
	int cnt = 0;
	LL s = p-1;
	while(!(s&1)) {
		s /= 2;
		cnt++;
	}
	LL accuracy = 2, m;
	for(int i = 0; i < accuracy; i++) {
		LL a = rand() % (p-1) + 1;
		m = p;
		LL x = power(a, s, m);
		if(x == 1 || x == p-1)	continue;
		int flag = 0;
		for(int i = 1; i < cnt; i++) {
			x = multiply(x, x, m);
			if(x == 1)	return false;
			if(x == p-1) {
				flag = 1;
				break;
			}
		}
		if(flag)	continue;
		return false;
	}
	return true;
}
/* End Miller Rabbin
 * * * * * * * * * */

inline LL mod_mul(const LL a, const LL b, const LL MOD) {
    LL rx;
    __asm__(
            "mulq   %%rdx               \n\t"
            "divq   %%rbx               \n\t"
            : "=d" (rx)
            : "a" (a), "b" (MOD), "d" (b)
    );
    return rx;
}
inline LL safe_mull(const LL a, const LL b, const LL MOD) {
    if (IS_64BIT_ARCH) return mod_mul(a, b, MOD);
    LL rx = 0, tmpx = 0;
    for (int bx = 0; b >> bx; ++bx) {
        tmpx += bx ? tmpx : a;
        if (tmpx >= MOD)
            tmpx -= MOD;
        if ((b >> bx) & 1) {
            rx += tmpx;
            if (rx >= MOD)
                rx -= MOD;
        }
    }
    return rx;
}
LL gcd(LL u, LL v) {
    int shift;
    LL diff;
    if (u == 0 || v == 0)
        return u | v;
    for (shift = 0; ((u | v) & 1) == 0; ++shift)
        u >>= 1, v >>= 1;
    while ((u & 1) == 0)
        u >>= 1;
    do {
        while ((v & 1) == 0)
            v >>= 1;
        if (u < v)
            v -= u;
        else
            diff = u - v, u = v, v = diff;
        v >>= 1;
    } while (v != 0);
    return u << shift;
}

LL brent(const LL n) {
    if (!(n & 1)) return 2;
    srand(time(0));
    LL y = 1 + (((LL)rand() << 32) | rand()) % (n - 1);
    LL c = 1 + (((LL)rand() << 32) | rand()) % (n - 1);
    LL m = 1 + (((LL)rand() << 32) | rand()) % (n - 1);
    LL g = 1, r = 1, q = 1, x, iter, ys, k, minx;
    while (g == 1) {
        x = y, iter = 0;
        while (iter++ < r){
            y = safe_mull(y, y, n);
            y += c;
            if (y >= n) y -= n;
        }
        k = 0;
        while (k < r && g == 1) {
            ys = y, minx = min(m, r - k), iter = 0;
            while (iter++ < minx) {
                y = safe_mull(y, y, n);
                y += c;
                if (y >= n) y -= n;
                q = safe_mull(q, x > y ? x - y : y - x, n);
            }
            g = gcd(q, n);
            k += m;
        }
        r <<= 1;
    }
    if (g == n)
        while (1) {
            ys = safe_mull(ys, ys, n);
            ys += c;
            if (ys >= n) ys -= n;
            g = gcd(x > ys ? x - ys : ys - x, n);
            if (g > 1) break;
        }
    return g;
}
LL generate(LL permut, LL b) {
    LL temp = 1, res = 0;
    while(permut > 0) {
        res += (permut % 10) * temp;
        permut /= 10;
        temp = temp * b;
    }
    return res;
}

bool checker(LL permut) {
    for(LL i = 2; i <= 10; i++) {
        if(Miller(generate(permut, i)))
            return false;
    }
    return true;
}

// don't trust popcount
int onbitcount(LL x) {
    int res = 0;
    while(x) {
        if(x % 2)   res++;
        x /= 2;
    }
    return res;
}
int numdgts(LL x) {
    int res = 0;
    while(x) {
        res++;
        x /= 10;
    }
    return res;
}
void printer(LL permut) {
    for(LL b = 2; b <= 10; b++) {
        LL x = generate(permut, b), ans = brent(x);
        cout << ans;
        assert(ans != x);
        if(b != 10)
            cout << ' ';
    }
}

int main() {
    LL iter = 1ll<<(MAXN-1), found = 0;
    iter += 1;
    cout << "Case #1:\n";
    while(found < MAXJ) {
        LL permut = 0, temp = 1, anothertemp = iter;
        if(onbitcount(iter) < 2 || iter % 2 == 0) {
            iter++;
            continue;
        }
        while(anothertemp) {  // create permut which is decimal of binary rep of iter
            permut += (anothertemp % 2) * temp;
            temp *= 10;
            anothertemp /= 2;
        }
        if(checker(permut)) {
            found++;
            // cout << found << ' ' << permut << endl;
            cout << permut << ' ';
            printer(permut);
            cout << '\n';
        }
        iter++;
    }
    return 0;
}
