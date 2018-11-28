#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cstring>
#include <cmath>
#include <climits>
#include <string>
#include <stdlib.h>
#include <bitset>
#include <ctime>

using namespace std;

#define ARGS_NUM(...) ARGS_NUM_IMPL_((0,__VA_ARGS__,5,4,3,2,1))
#define ARGS_NUM_IMPL_(arg) ARGS_NUM_IMPL arg
#define ARGS_NUM_IMPL(_0,_1,_2,_3,_4,_5, N,...) N
#define FUNC_CALL(func, ...) FUNC_CALL_NUM(func, ARGS_NUM(__VA_ARGS__))
#define FUNC_CALL_NUM(func, args) FUNC_CALL_NUM_(func, args)
#define FUNC_CALL_NUM_(func, args) FUNC_CALL_NUM__(func, args)
#define FUNC_CALL_NUM__(func, args) func ## args


//#define I64_IO

// i/o defines
#define read_int1(v) scanf("%d", &v)
#define read_int2(v1, v2) scanf("%d%d", &v1, &v2)
#define read_int3(v1, v2, v3) scanf("%d%d%d", &v1, &v2, &v3)
#define read_int4(v1, v2, v3, v4) scanf("%d%d%d%d", &v1, &v2, &v3, &v4)
#define read_int(...) FUNC_CALL(read_int, __VA_ARGS__)(__VA_ARGS__)
#ifdef I64_IO
#define read_ll1(v) scanf(MODE ? "%lld" : "%I64d", &v)
#define read_ll2(v1, v2) scanf(MODE ? "%lld%lld" : "%I64d%I64d", &v1, &v2)
#define read_ll3(v1, v2, v3) scanf(MODE ? "%lld%lld%lld" : "%I64d%I64d%I64d", &v1, &v2, &v3)
#define read_ll4(v1, v2, v3, v4) scanf(MODE ?"%lld%lld%lld%lld" : "%I64d%I64d%I64d%I64d", &v1, &v2, &v3, &v4)
#define print_ll(v) printf(MODE ? "%lld" : "%I64d", v)
#else
#define read_ll1(v) scanf( "%lld" , &v)
#define read_ll2(v1, v2) scanf( "%lld%lld" , &v1, &v2)
#define read_ll3(v1, v2, v3) scanf( "%lld%lld%lld" , &v1, &v2, &v3)
#define read_ll4(v1, v2, v3, v4) scanf("%lld%lld%lld%lld", &v1, &v2, &v3, &v4)
#define print_ll(v) printf("%lld" , v)
#endif
#define read_ll(...) FUNC_CALL(read_ll, __VA_ARGS__)(__VA_ARGS__)
#define read_str(v) scanf("%s", v)
#define print_str(v) printf("%s", v)
#define read_f(v) scanf("%f", &v)
#define print_f(v, prec) printf("%.*f", prec, v)
#define read_lf1(v) scanf("%lf", &v)
#define read_lf2(v1, v2) scanf("%lf%lf", &v1, &v2)
#define read_lf3(v1, v2, v3) scanf("%lf%lf%lf", &v1, &v2, &v3)
#define read_lf(...) FUNC_CALL(read_lf, __VA_ARGS__)(__VA_ARGS__)
#define print_lf(v, prec) printf("%.*lf", prec, v)
#define print_int(v) printf("%d", v)

//short defines
#define ll long long
#define ull unsigned long long
#define uchar unsigned char
//#define pi 3.14159265359
#define eps (1e-8)
#define minn(a, b) a = min((a), (b))
#define maxx(a, b) a = max((a), (b))
#define all(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define ln putchar('\n')
#define space putchar(' ')
#define pair_i pair <int,int>
#define pair_ll pair <ll,ll>



// debug defines
#define PRINT(...) MODE ? (FUNC_CALL(PRINT, __VA_ARGS__)(__VA_ARGS__)) : cout << ""
#define PRINT1(a) cout << #a << " = " << (a) << "\n"
#define PRINT2(a,b) cout << #a << " = " << (a) << "," << #b << " = " << (b) << "\n"
#define PRINT3(a,b,c) cout << #a << " = " << (a) << "," << #b << " = " << (b) << "," << #c << " = " << (c) << "\n"
#define PRINT4(a,b,c,d) cout << #a << " = " << (a) << "," << #b << " = " << (b) << "," << #c << " = " << (c) << "," << #d << " = " << (d) << "\n"
#define BP MODE ? break_point() : 0
#define LINE MODE ? printf("-------------------------------\n") : 0
#define LOG(...) MODE ? printf(__VA_ARGS__) : 0;


// useful functions
int break_point(){ char c; while ((c = getchar()) != '\n'); return 0; }
template <typename T> void read_integer(T &r){ bool sign = 0; r = 0; char c; while (1){ c = getchar(); if (c == '-'){ sign = 1; break; }if (c != ' ' && c != '\n'){ r = c - '0'; break; } }while (1){ c = getchar(); if (c == ' ' || c == '\n')break; r = r * 10 + (c - '0'); }if (sign)r = -r; }
ll binpowmod(ll a, ll b, ll mod){if (b == 0)return 1; ll c = binpowmod(a, b >> 1, mod);return (((c*c) % mod) * (b & 1 ? a : 1)) % mod;}
ll binpow(ll a, ll b){if (b == 0)return 1;ll c = binpow(a, b >> 1);return c*c*(b & 1 ? a : 1);}
inline int getbit(int x, int b){return (x >> b) & 1;}
inline ll getbit(ll x, int b){return (x >> b) & 1;}
inline ull getbit(ull x, int b){return (x >> b) & 1;}
inline int setbit(int x, int b){return x | (1 << b);}
inline void _setbit(int &x, int b){x = setbit(x, b);}
inline ll setbit(ll x, int b){ return x | (1ll << b);}
inline void _setbit(ll &x, int b){x = setbit(x, b);}
inline int unsetbit(int x, int b){return x & (INT_MAX - (1 << b));}
inline void _unsetbit(int &x, int b){x = unsetbit(x, b);}
inline int countbit(int x){x = x - ((x >> 1) & 0x55555555);x = (x & 0x33333333) + ((x >> 2) & 0x33333333);return ((x + (x >> 4) & 0xF0F0F0F) * 0x1010101) >> 24;}
inline ll countbit(ll x){int p1 = (x >> 32) & ((1ll << 32)-1);int p2 = x & ((1ll << 32)-1);return countbit(p1) + countbit(p2);}
template <typename T> void printbit(T x, int len){for(int i = len-1; i >= 0; i--) print_int(getbit(x, i));}
int gcd(int a, int b){ return b == 0 ? a : gcd(b, a%b); }
ll gcd(ll a, ll b){ return b == 0 ? a : gcd(b, a%b); }

template <typename A,typename B> ostream& operator<<(ostream& stream, const pair <A, B> &p){stream << "{" << p.first << "," << p.second << "}";return stream;}
template <typename A> ostream& operator<<(ostream &stream, const vector <A> &v){stream << "[";for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " ";stream << "]";return stream;}
template <typename A, typename B> ostream& operator<<(ostream &stream, const map <A, B> &v){stream << "[";for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " ";stream << "]";return stream;}
template <typename A> ostream& operator<<(ostream &stream, const set <A> &v){stream << "[";for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " ";stream << "]";return stream;}
template <typename A> ostream& operator<<(ostream &stream, const stack <A> &v){stack <A> st=v;stream << "["; while (!st.empty()){ stream << st.top() << " "; st.pop(); }stream << "]";return stream;}
template <typename A> ostream& operator<<(ostream &stream, const priority_queue <A> &v){priority_queue <A> q = v;stream << "[";while (!q.empty()){stream << q.top() << " ";q.pop();}stream << "]";return stream;}
template <typename A> ostream& operator<<(ostream &stream, const queue <A> &v){queue <A> q = v;stream << "[";while (!q.empty()){stream << q.front() << " ";q.pop();}stream << "]";return stream;}

void run();

#ifndef MODE
#define MODE 0
#endif
//#define FILES "best"
//#define FROM_FILE


int main()
{
    srand(time(NULL));
#ifdef FILES
    freopen(FILES".in", "r", stdin);
    freopen(FILES".out", "w", stdout);
#else
#ifdef FROM_FILE
    freopen("file.in", "r", stdin);
#endif
#endif
    do
    {
        run();
        if (MODE)
        {
            LINE;
            LINE;
            BP;
        }
    } while (MODE);
    return 0;
}


//----------------------------------
//----------------------------------

#define N 2003
const int mod = 1e9+7;

bool a[10];

void run()
{
    int T;
    read_int(T);
    int test_case = 1;
    while(T--)
    {
        int n;
        read_int(n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", test_case++);
            continue;
        }
        int cnt = 0;
        for(int i = 0; i < 10; i++)
            a[i] = false;
        int i = 0;
        while(cnt < 10)
        {
            i++;
            ll d = n * i;
            while(d)
            {
                cnt += (!a[d % 10]);
                a[d % 10] = 1;
                d /= 10;
            }
        }
        printf("Case #%d: %lld\n", test_case++, 1ll*i*n);
    }
}