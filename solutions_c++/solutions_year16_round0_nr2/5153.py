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

vector <char> vc;

int main(void) {
    //__
    //___
    int cas, co = 0;
    read(cas);
    while(cas --) {
        char ch[100 + 10];
        read(ch);
        int len = strlen(ch), ans = 0;
        vc.clear();
        rep(i, 0, len)      vc.push_back(ch[i]);
        while(true) {
            if(vc.empty())
                break;
            while(!vc.empty() && vc.back() == '+') {
                vc.pop_back();
            }
            int f = 0;
            while(!vc.empty() && vc[0] == '-') {
                f = 1;
                vc.erase(vc.begin());
            }
            if(f) {
                rep(i, 0, vc.size()) {
                    vc[i] = (vc[i] == '-' ? '+' : '-');
                }
                reverse(all(vc));
                ans ++;
            } else {
                int k = 0;
                rep(i, 0, vc.size()) {
                    k = 1;
                    if(vc[i] == '-')
                        break;
                    vc[i] = '-';
                }
                ans += k;
            }
        }
        printf("Case #%d: %d\n", ++co, ans);
    }
    return 0;
}

