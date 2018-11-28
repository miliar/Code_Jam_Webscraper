#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <map>
#include <cstring>
#include <queue>
#include <cmath>

using namespace std;

#define maxd 13
#define digit 9
#define base 1000000000
#define totaldigit (maxd-1)*digit
const int p[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
typedef long long ll;
struct bignum {
	inline static bignum tobignum (string a) {
	    bignum c;
	    c.reset();
	    for(int i = 0; i < a.length(); i++)
	        c = c*10 + (a[i]-'0');
	    return c;
	}

	inline static bignum tobignum (ll n) { 
	    bignum c;
	    c.reset();
	    return c+n;
	}

	ll a[maxd];
	inline void reset() { memset(a, 0, sizeof a); }
	inline int Digit(const int i) {
		if (1+i/digit >= maxd) return -1;
		return (a[1+i/digit] / p[digit-1-i%9]) % 10; 
	}
	inline ll &operator [](int i) { return a[i]; }
	inline friend bignum operator * (bignum a, bignum b) {
		bignum c;
		c.reset();
		for(int i = maxd-1; i >= 1; i--) {
			ll cr = 0;
			for(int j = maxd-1; j >= 1; j--) {
				if (i+j > maxd-1) {
					int k = i+j-(maxd-1);
					c[k] = c[k] + a[i]*b[j] + cr;
					cr = c[k] / base;
					c[k] = c[k] % base;
				}
			}
		}
		return c;
	}
	
	inline friend bignum operator * (bignum a,  ll b) {
		bignum c;
		ll cr = 0;
		for(int i = maxd-1; i >= 1; i--) {
			c[i] = (a[i]*b + cr) % base;
			cr = (a[i]*b + cr) / base;
		}
		return c;
	}
	
	inline friend bignum operator + (bignum a,  ll b) {
		bignum c;
		for(int i = maxd-1; i >= 1; i--) {
			c[i] = (a[i]+b) % base;
			b = (a[i]+b) / base;
		}
		return c;
	}
	
	inline friend bignum operator + (bignum a,  bignum b) {
		bignum c;
		ll cr = 0;
		for(int i = maxd-1; i >= 1; i--) {
			c[i] = (a[i] + b[i] + cr) % base;
			cr = (a[i] + b[i] + cr) / base;
		}
		return c;
	}
	
	inline friend bignum operator - (bignum a,  bignum b) {
		bignum c;
		ll cr = 0;
		for(int i = maxd-1; i >= 1; i--) {
			c[i] = a[i]-b[i]-cr;
			if (c[i] < 0) {
				c[i] += base;
				cr = 1;
			}
			else cr = 0;
		}
		return c;
	}
	
	inline friend bignum operator - (bignum a,  ll b) {
		bignum b1;
		b1.reset();
		b1 = b1+b;
		return a-b1;
	} 

	inline friend bignum operator / (bignum a, ll b) {
		bignum c; c.reset();
		ll t = 0;
		for(int i = 1; i < maxd; i++) {
			t = t*base + a[i];
			c[i] = t/b;
			t %= b;
		}			
		return c;
	}

	inline friend ll operator % (bignum &a, ll b) {
		bignum c = (a/b)*b;
		c = a-c;
		ll ret = 0;
		for(int i = 1; i < maxd; i++)
			ret = ret*base + c[i];
		return ret;
	}

	inline friend bignum operator ^ (bignum &a, ll b) {
		if (b == 0) return tobignum(1LL);
		if (b == 1) return a;
		bignum c = a^(b/2);
		c = c*c;
		// c = tobignum(c%modl); //<---
		if (b&1) c = c*a;
		return c;
	}
	
	inline void print() {
		for(int i = 1; i < maxd; i++) 
			if (a[i] > 0) {
				printf("%lld", a[i]);
				for(int j = i+1; j < maxd; j++)
					printf("%09lld", a[j]);
                printf("\n");
				return;
			}
		printf("0\n");		
	}
	
	inline friend bool operator < (bignum a, bignum b) {
	    for(int i = 1; i < maxd; i++)
            if (a[i] < b[i]) return 1;
            else if (a[i] > b[i]) return 0;
        return 0;
	}
	inline friend bool operator <= (bignum a, bignum b) {
	    for(int i = 1; i < maxd; i++)
            if (a[i] < b[i]) return 1;
            else if (a[i] > b[i]) return 0;
        return 1;
	}
};
inline static bignum tobignum (string a) {
    bignum c;
    c.reset();
    for(int i = 0; i < a.length(); i++)
        c = c*10 + (a[i]-'0');
    return c;
}
inline static bignum tobignum (ll n) { 
    bignum c;
    c.reset();
    return c+n;
}
inline bignum GCD(bignum a, ll b) {
	if (!b) return a;
	else return GCD(tobignum(b), a%b);
}

bignum a, b;
ll dp[totaldigit][11][3];
ll f[totaldigit];
bignum n1 = tobignum(1);
bignum n0 = tobignum(0);

ll CntPalin(const int shift, const int i, const int sumdigit, const int smaller, bignum& lim) {
    if (i > (totaldigit+1-shift)/2) return smaller > 0;
    
    if (dp[i][sumdigit][smaller] == -1) {
        dp[i][sumdigit][smaller] = 0;
        bool ismiddle = shift+i-1 == totaldigit-i;
        for(int cur = (i == 1); cur <= (ismiddle ? int(sqrt(sumdigit) + 1e-8) : int(sqrt(sumdigit/2) + 1e-8)); cur++) {
            if (cur < lim.Digit(shift + i-1)) 
            	dp[i][sumdigit][smaller] = dp[i][sumdigit][smaller] + CntPalin(shift, i+1, sumdigit-(ismiddle ? 1:2)*cur*cur, 2, lim);
            else if (cur == lim.Digit(shift + i-1)) 
                if (cur < lim.Digit(totaldigit-i)) 
                	dp[i][sumdigit][smaller] = dp[i][sumdigit][smaller] + CntPalin(shift, i+1, sumdigit-(ismiddle ? 1:2)*cur*cur, smaller == 0 ? 1 : smaller, lim);
                 else if (cur == lim.Digit(totaldigit-i)) 
                	dp[i][sumdigit][smaller] = dp[i][sumdigit][smaller] + CntPalin(shift, i+1, sumdigit-(ismiddle ? 1:2)*cur*cur, smaller, lim);
                else 
                	dp[i][sumdigit][smaller] = dp[i][sumdigit][smaller] + CntPalin(shift, i+1, sumdigit-(ismiddle ? 1:2)*cur*cur, smaller < 2 ? 0 : 2, lim);
            else if (smaller == 2) 
            	dp[i][sumdigit][smaller] = dp[i][sumdigit][smaller] + CntPalin(shift, i+1, sumdigit-(ismiddle ? 1:2)*cur*cur, 2, lim);
        }
    }
    return dp[i][sumdigit][smaller];
}

ll Count(const bignum lim) {
	if (n0 < lim) {
		bignum l = tobignum(1);
		bignum r = lim;
		while (l+1 < r) {
			bignum mid = (l+r)/2;
			if (mid*mid <= lim) l = mid;
			else r = mid;
		}
		if (r*r <= lim) l = r;
		ll ret = 0;
		for(int shift = 0; shift < totaldigit; shift++) {
			memset(dp, -1, sizeof dp);
			ret = ret + CntPalin(shift, 1, 9, 1, l);
			if (l.Digit(shift) > 0 && shift+1 < totaldigit) {
				ret = ret + f[shift+1];
				break;
			}
		}
		return ret;
	}
	else return 0;
}

void init() {
	for(int shift = totaldigit-1; shift >= 0; shift--) {
		memset(dp, -1, sizeof dp);
		f[shift] = CntPalin(shift, 1, 9, 2, n0);
		// if (totaldigit-shift <= 10) cout << totaldigit-shift << " " << f[shift] << endl;
		if (shift+1 < totaldigit) f[shift] += f[shift+1];
	}
}

int main() {
	freopen("C-large-1.in", "r", stdin);
	freopen("Fair and Square.out", "w", stdout);
	init();
	int test;
	cin >> test;	
	for(int tcase = 1; tcase <= test; tcase++) {
		printf("Case #%d: ", tcase);
		string A, B;
		cin >> A >> B;
		a = tobignum(A); b = tobignum(B);
		ll ret = Count(b) - Count(a-1);
		printf("%lld\n", ret);
	}
}