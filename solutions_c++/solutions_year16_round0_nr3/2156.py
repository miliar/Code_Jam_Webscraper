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


vector <string> str[11]
{
    {},
    {},
    {
        "1",
        "2",
        "4",
        "8",
        "16",
        "32",
        "64",
        "128",
        "256",
        "512",
        "1024",
        "2048",
        "4096",
        "8192",
        "16384",
        "32768",
        "65536",
        "131072",
        "262144",
        "524288",
        "1048576",
        "2097152",
        "4194304",
        "8388608",
        "16777216",
        "33554432",
        "67108864",
        "134217728",
        "268435456",
        "536870912",
        "1073741824",
        "2147483648",
    },
    {
        "1",
        "3",
        "9",
        "27",
        "81",
        "243",
        "729",
        "2187",
        "6561",
        "19683",
        "59049",
        "177147",
        "531441",
        "1594323",
        "4782969",
        "14348907",
        "43046721",
        "129140163",
        "387420489",
        "1162261467",
        "3486784401",
        "10460353203",
        "31381059609",
        "94143178827",
        "282429536481",
        "847288609443",
        "2541865828329",
        "7625597484987",
        "22876792454961",
        "68630377364883",
        "205891132094649",
        "617673396283947",
    },
    {
        "1",
        "4",
        "16",
        "64",
        "256",
        "1024",
        "4096",
        "16384",
        "65536",
        "262144",
        "1048576",
        "4194304",
        "16777216",
        "67108864",
        "268435456",
        "1073741824",
        "4294967296",
        "17179869184",
        "68719476736",
        "274877906944",
        "1099511627776",
        "4398046511104",
        "17592186044416",
        "70368744177664",
        "281474976710656",
        "1125899906842624",
        "4503599627370496",
        "18014398509481984",
        "72057594037927936",
        "288230376151711744",
        "1152921504606846976",
        "4611686018427387904",
    },
    {
        "1",
        "5",
        "25",
        "125",
        "625",
        "3125",
        "15625",
        "78125",
        "390625",
        "1953125",
        "9765625",
        "48828125",
        "244140625",
        "1220703125",
        "6103515625",
        "30517578125",
        "152587890625",
        "762939453125",
        "3814697265625",
        "19073486328125",
        "95367431640625",
        "476837158203125",
        "2384185791015625",
        "11920928955078125",
        "59604644775390625",
        "298023223876953125",
        "1490116119384765625",
        "7450580596923828125",
        "37252902984619140625",
        "186264514923095703125",
        "931322574615478515625",
        "4656612873077392578125",
    },
    {
        "1",
        "6",
        "36",
        "216",
        "1296",
        "7776",
        "46656",
        "279936",
        "1679616",
        "10077696",
        "60466176",
        "362797056",
        "2176782336",
        "13060694016",
        "78364164096",
        "470184984576",
        "2821109907456",
        "16926659444736",
        "101559956668416",
        "609359740010496",
        "3656158440062976",
        "21936950640377856",
        "131621703842267136",
        "789730223053602816",
        "4738381338321616896",
        "28430288029929701376",
        "170581728179578208256",
        "1023490369077469249536",
        "6140942214464815497216",
        "36845653286788892983296",
        "221073919720733357899776",
        "1326443518324400147398656",
    },
    {
        "1",
        "7",
        "49",
        "343",
        "2401",
        "16807",
        "117649",
        "823543",
        "5764801",
        "40353607",
        "282475249",
        "1977326743",
        "13841287201",
        "96889010407",
        "678223072849",
        "4747561509943",
        "33232930569601",
        "232630513987207",
        "1628413597910449",
        "11398895185373143",
        "79792266297612001",
        "558545864083284007",
        "3909821048582988049",
        "27368747340080916343",
        "191581231380566414401",
        "1341068619663964900807",
        "9387480337647754305649",
        "65712362363534280139543",
        "459986536544739960976801",
        "3219905755813179726837607",
        "22539340290692258087863249",
        "157775382034845806615042743",
    },
    {
        "1",
        "8",
        "64",
        "512",
        "4096",
        "32768",
        "262144",
        "2097152",
        "16777216",
        "134217728",
        "1073741824",
        "8589934592",
        "68719476736",
        "549755813888",
        "4398046511104",
        "35184372088832",
        "281474976710656",
        "2251799813685248",
        "18014398509481984",
        "144115188075855872",
        "1152921504606846976",
        "9223372036854775808",
        "73786976294838206464",
        "590295810358705651712",
        "4722366482869645213696",
        "37778931862957161709568",
        "302231454903657293676544",
        "2417851639229258349412352",
        "19342813113834066795298816",
        "154742504910672534362390528",
        "1237940039285380274899124224",
        "9903520314283042199192993792",
    },
    {
        "1",
        "9",
        "81",
        "729",
        "6561",
        "59049",
        "531441",
        "4782969",
        "43046721",
        "387420489",
        "3486784401",
        "31381059609",
        "282429536481",
        "2541865828329",
        "22876792454961",
        "205891132094649",
        "1853020188851841",
        "16677181699666569",
        "150094635296999121",
        "1350851717672992089",
        "12157665459056928801",
        "109418989131512359209",
        "984770902183611232881",
        "8862938119652501095929",
        "79766443076872509863361",
        "717897987691852588770249",
        "6461081889226673298932241",
        "58149737003040059690390169",
        "523347633027360537213511521",
        "4710128697246244834921603689",
        "42391158275216203514294433201",
        "381520424476945831628649898809",
    },
    {
        "1",
        "10",
        "100",
        "1000",
        "10000",
        "100000",
        "1000000",
        "10000000",
        "100000000",
        "1000000000",
        "10000000000",
        "100000000000",
        "1000000000000",
        "10000000000000",
        "100000000000000",
        "1000000000000000",
        "10000000000000000",
        "100000000000000000",
        "1000000000000000000",
        "10000000000000000000",
        "100000000000000000000",
        "1000000000000000000000",
        "10000000000000000000000",
        "100000000000000000000000",
        "1000000000000000000000000",
        "10000000000000000000000000",
        "100000000000000000000000000",
        "1000000000000000000000000000",
        "10000000000000000000000000000",
        "100000000000000000000000000000",
        "1000000000000000000000000000000",
        "10000000000000000000000000000000",
    }
};


struct answer
{
    ll s;
    vector <int> v;
};

char buf[N];


map <pair <pair <int, int>, int>, int> mp;

int calc_rem(int ss, int power, int d)
{
    if(mp.find({{ss, power}, d}) != mp.end())
        return mp[{{ss, power}, d}];
    int r = 0;
    for(int i = 0; i < sz(str[ss][power]); i++)
    {
        r = r * 10 + str[ss][power][i] - '0';
        r %= d;
    }
    //PRINT(str[ss][power], d, r);
    return mp[{{ss, power}, d}] = r;
}

void run()
{
    int T;
    read_int(T);
    vector <answer> result;
    while(T--)
    {
        int n, k;
        read_int(n, k);
        ll to = 1ll << (n-2);
        for(ll mask1 = 0; mask1 < to && sz(result) < k; mask1++)
        {
            ll mask = (mask1 << 1) ^ (to<<1) ^ 1;
            if(!getbit(mask, 0))
                continue;
            answer ans;
            ans.s = mask;
            for(int num = 2; num < 11; num++)
            {
                for(int j = 2; j < 1000; j++)
                {
                    int r = 0;
                    for(int i = 0; i < n; i++)
                    {
                        if(getbit(mask, i))
                            r = (r + calc_rem(num, i, j)) % j;
                    }
                    //LOG("reminder for %lld %d %d is %d\n", mask, num, j, r);
                    if(r == 0)
                    {
                        ans.v.push_back(j);
                        break;
                    }
                }
            }
            if(sz(ans.v) == 9)
                result.push_back(ans);
        }
        printf("Case #1:\n");
        for(int i = 0; i < sz(result); i++)
        {
            for(int j = n-1; j >= 0; j--)
                printf("%lld", getbit(result[i].s, j));
            space;
            for(int j = 0; j < 9; j++)
                printf("%d ", result[i].v[j]);
            ln;
        }
    }
}