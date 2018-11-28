/*
	Bismillahir_Rahmanir_Rahim
	I have not failed, I have just found 10000 ways that won't work
*/

#include <bits/stdc++.h>
#define _ std::ios_base::Init i;std::ios_base::sync_with_stdio(false);std::cin.tie(0);
#define __ freopen("C:\\Users\\Jobayer-sheikh\\Desktop\\input.txt","r", stdin);
#define ___ freopen("C:\\Users\\Jobayer-sheikh\\Desktop\\output.txt","w+", stdout);

using namespace std;

#define LL			long long int
#define Max 		1000000 + 10
#define pi  		2*acos(0.0)
#define test(i) 	printf("Case %d: ", ++ i);
#define angle(n)	n * (pi / 180)
#define mem(a, v)	memset(a, v, sizeof(a));
#define read(a)		scanf("%lld", &a)
#define rep(i, s, e)for(int i = (s); i < (e); i++)
#define all(v)		v.begin(), v.end()

#define read(args...) input, args
struct Input {
    inline Input& operator,(int &a) {
        scanf("%d", &a);
    }
    inline Input& operator,(long int &a) {
        scanf("%ld", &a);
    }
    inline Input& operator,(long long int &a) {
        scanf("%lld", &a);
    }
    inline Input& operator,(float &a) {
        scanf("%f", &a);
    }
    inline Input& operator,(char ch) {
        scanf("%s", &ch);
    }
    inline Input& operator,(double &d) {
        scanf("%lf", &d);
    }

    template<typename T> inline Input& operator,(T &a) {
        cin >> a;
    }
} input;

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




///*********************************** @ SOURCE_CODE_START_HERE@ **********************************

set <int> s;

void f(LL n) {
    while(n)    s.insert(n % 10), n /= 10;
    return;
}

int main(void) {
    //__
    //___
    int cas, co = 0;
    read(cas);
    while(cas --) {
        LL a, m = 2, n;
        read(a);
        printf("Case #%d: ", ++ co);
        if(a == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        n = a;
        s.clear();
        while(true) {
            f(n);
            if(s.size() == 10) {
                printf("%lld\n", n);
                break;
            }
            n = a * m;
            m ++;
        }
    }

    return 0;
}

