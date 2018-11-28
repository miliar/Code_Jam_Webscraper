/*
	Bismillahir_Rahmanir_Rahim
	I have not failed, I have just found 10000 ways that won't work
*/

#include <bits/stdc++.h>
#define _ std::ios_base::Init i;std::ios_base::sync_with_stdio(false);std::cin.tie(0);
#define __ freopen("C:\\Users\\Jobayer\\Desktop\\output.txt","w+", stdout);
#define ___ freopen("C:\\Users\\Jobayer\\Desktop\\input.txt","r+", stdin);

using namespace std;

#define LL          long long
#define Max 		1000000 + 10
#define pi  		2*acos(0.0)
#define test(i) 	printf("Case #%d: ", ++ i)
#define angle(n)	n * (pi / 180)
#define mem(a, v)	memset(a, v, sizeof(a));
#define read(a)		scanf("%d", &a)
#define rep(i, s, e)for(int i = (s); i < (e); i++)
#define all(v)		v.begin(), v.end()

template <class T> inline pair <T, T> extendedEuclid(T a, T b) {
    if(b == 0)
        return pair<T, T>(1, 0);
    else {
        pair<T, T> d = extendedEuclid(b, a % b);
        return pair<T, T>(d.second, d.first - d.second * (a / b));
    }
    /// returns x, y where, ax + by = gcd(a,b)
}

template <class T> inline T modularInverse(T a, T M) {
    pair<T, T> ret = extendedEuclid(a, M);
    return ((ret.first % M) + M) % M;
    /// returns a^-1 % M modular Inverse
}

template <class T> inline T bigMod(T p,T e,T M) {
    LL ret = 1;
    while(e > 0) {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
        e >>= 1;
    }
    return (T)ret;
}
template <class T> inline T power(T p,T e) {
    LL ret = 1;
    while(e > 0) {
        if(e & 1) ret = (ret * p);
        p = (p * p);
        e >>= 1;
    }
    return (T)ret;
}
template<class T> inline string tostring( T n ) {
    stringstream ss;
    ss << n;
    return ss.str();
}
template<class T> inline T toint ( T n ) {
    T ret;
    stringstream s( n );
    s >> ret;
    return ret;
}

void nCr(vector <LL> &vc, int st, int ed, LL sum, LL A[]) {
    if(st == ed) {
        vc.push_back(sum);
        return;
    }
    for(LL i = 0; i <= 2; i++) {
        nCr(vc, st + 1, ed, sum + A[st] * i, A);
    }
}

struct SM {
    LL a, b, c, d;
    SM(LL _a = 0, LL _b = 0, LL _c = 0, LL _d = 0) {
        a = _a;
        b = _b;
        c = _c;
        d = _d;
    }
};
struct comp {
    bool operator()(const SM& u, const SM& v) {
        return u.a> v.a;
    }
};

struct com {
    bool operator()(const int& l, const int& r) {
        return l > r;
    }
};
priority_queue <SM, vector <SM>, comp > pq;







///*********************************** @ SOURCE_CODE_START_HERE @ **********************************

int A[100000 + 10], n;

int main() {
    //_
    //__
    //___
    int cas = 0, tc = 0;
    read(cas);
    while(cas --) {
        read(n);

        rep(i, 0, n + 1) {
            scanf("%1d", &A[i]);
        }
        int ans = 0, sum = 0;

        rep(i, 0, n + 1) {
            if(A[i] == 0)	continue;

            if(i == 0) {
                sum += A[i];
                continue;
            }

            if(sum >= i) {
                sum += A[i];
            } else {
                ans += abs(sum - i);
                sum += (ans + A[i]);
            }
        }
        test(tc);
        printf("%d\n", ans);
    }

    return 0;
}
/// @ END_OF_SOURCE_CODE

