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
#define rep(i, s, e)for(LL i = (s); i < (e); i++)
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

vector < vector <int> > s[100];
//set < vector <int> > sv;

int main(void) {
    //__
    //___
    LL len = (1ll << 17ll), arr[20];
    for(LL i = 1; i <= len; i += 2) {
        LL n = i;
        vector <int> vc;
        while(n) {
            vc.push_back(n % 2);
            n /= 2;
        }
        reverse(all(vc));
        s[vc.size()].push_back(vc);
    }

    int cas, co = 0, n, j;
    read(cas);

    while(cas --) {
        read(n, j);
        printf("Case #%d:\n", ++co);

        rep(i, 0, s[n].size()) {
            mem(arr, 0);

            rep(k, 0, s[n][i].size()) {
                for(LL b = 2; b <= 10; b++) {
                    arr[b] += (s[n][i][k] * power(b, k));
                }
            }
            int c = 0;
            rep(b, 2, 11) {
                LL s = 0, sq = sqrt(arr[b]) + 1;
                rep(k, 2, sq) {
                    if(arr[b] % k == 0) {
                        c = c + 1;
                        arr[b] = k;
                        break;
                    }
                }
            }
            if(c == 9 && j) {
                //cout << 51 - j <<  "  ";
                j --;
                //sv.insert(s[n][i]);
                for(int k = s[n][i].size() - 1; k >= 0; k--)   printf("%d", s[n][i][k]);
                printf(" ");
                rep(b, 2, 11)   printf("%lld%c", arr[b], b == 10 ? '\n' : ' ');
            }
            if(j == 0)
                break;
        }
        //cout << sv.size() << endl;
    }
    return 0;
}

