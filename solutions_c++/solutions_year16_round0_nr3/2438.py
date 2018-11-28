/*
ID: hepic
PROG: sabotage
LANG: C++11
*/
#include <bits/stdc++.h>

#define FOR(i, a, b) for(auto i=a; i<=b; ++i)
#define REP(i, a, b) for(auto i=a; i<b; ++i)
#define FORI(i, a, b) for(auto i=a; i!=b+1-2*(a>b); i+=1-2*(a>b))
#define REPI(i, a, b) for(auto i=a-(a>b); i!=b-(a>b); i+=1-2*(a>b))
#define ALL(v) v.begin(),v.end()
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define eb(a, b) emplace_back(a, b)
#define fir first
#define sec second
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define type(x) typeid(x).name()
#define ms(arr, val) memset(arr, val, sizeof(arr))
#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)
#define SIZE 200010
#define MAXN 99999999
#define NUM 20
#define PI acos(-1)
#define open_read1 freopen("C:\\Users\\Hepic\\Desktop\\a.txt", "r", stdin)
#define open_write1 freopen("C:\\Users\\Hepic\\Desktop\\b.txt", "w", stdout)
#define open_read freopen("painting.in", "r", stdin)
#define open_write freopen("painting.out", "w", stdout)

using namespace std;

typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<double, double> PDD;
typedef pair<int, int> PII;
typedef pair<int, PII> PIPII;
typedef pair<PII, PII> PPIIPII;
typedef pair<LL, LL> PLL;
typedef pair<ULL, ULL> PUU;
typedef pair<LL, PLL> PLPLL;
typedef pair<PLL, PLL> PPLLPLL;


template<typename T, typename T1>
ostream& operator << (ostream &out, pair<T, T1> obj)
{
    out<<"("<<obj.first<<","<<obj.second<<")";
    return out;
}


template<typename T, typename T1>
ostream& operator << (ostream &out, map<T, T1> cont)
{
    typename map<T, T1>::const_iterator itr = cont.begin();
    typename map<T, T1>::const_iterator ends = cont.end();

    for(; itr!=ends; ++itr)
        out<<*itr<<" ";
    out<<endl;

    return out;
}


template<typename T>
ostream& operator << (ostream &out, set<T> cont)
{
    typename set<T>::const_iterator itr = cont.begin();
    typename set<T>::const_iterator ends = cont.end();

    for(; itr!=ends; ++itr)
        out<<*itr<<" ";
    out<<endl;

    return out;
}


template<typename T>
ostream& operator << (ostream &out, multiset<T> cont)
{
    typename multiset<T>::const_iterator itr = cont.begin();
    typename multiset<T>::const_iterator ends = cont.end();

    for(; itr!=ends; ++itr)
        out<<*itr<<" ";
    out<<endl;

    return out;
}


template<typename T, template<typename ELEM, typename ALLOC=allocator<ELEM>> class CONT>
ostream& operator << (ostream &out, CONT<T> cont)
{
    typename CONT<T>::const_iterator itr = cont.begin();
    typename CONT<T>::const_iterator ends = cont.end();

    for(; itr!=ends; ++itr)
        out<<*itr<<" ";
    out<<endl;

    return out;
}


template<typename T, unsigned int N, typename CTy, typename CTr>
typename enable_if<!is_same<T, char>::value, basic_ostream<CTy, CTr> &>::type
operator << (basic_ostream<CTy, CTr> &out, const T (&arr)[N])
{
     REP(i, 0, N)
        out<<arr[i]<<" ";
    out<<endl;

    return out;
}


template<typename T>
T gcd(T a, T b)
{
    T min_v = min(a, b);
    T max_v = max(a, b);

    while(min_v)
    {
        T temp = max_v % min_v;
        max_v = min_v;
        min_v = temp;
    }

    return max_v;
}


template<typename T>
T lcm(T a, T b)
{
    return (a*b) / gcd(a, b);
}


template<typename T>
T fast_exp_pow(T base, T exp, T mod)
{
    LL res = 1;

    while(exp)
    {
        if(exp&1)
        {
            res *= base;
            res %= mod;
        }

        exp >>= 1;
        base *= base;
        base %= mod;
    }

    return res;
}

/*#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################*/

int T, N, J;
bool found;
bool used_divisor[1000010], is_prime[1000010];
vector<LL> divisors;
LL base_10;



LL convert_to_base(LL num, int base)
{
    LL ret_num = 0, power = 1;

    while(num)
    {
        ret_num = (ret_num + (num&1)*power);
        power *= base;
        num >>= 1;
    }

    return ret_num;
}


bool is_jamcoin(LL num)
{
    ms(used_divisor, false);
    divisors.clear();

    FOR(base, 2, 10)
    {
        LL ret_num = convert_to_base(num, base);
        found = false;

        for(LL i=3; i*i<=ret_num; i+=2)
            if(ret_num%i == 0  &&  !used_divisor[i])
            {
                divisors.pb(i);
                used_divisor[i] = true;
                found = true;

                break;
            }

        if(!found)
            return false;
    }

    return true;
}


void print_base_two(LL num)
{
    stack<int> stc;

    while(num)
    {
        stc.push(num&1);
        num >>= 1;
    }

    while(!stc.empty())
    {
        printf("%d", stc.top());
        stc.pop();
    }

    printf(" ");
}




int main()
{
    open_read1;
    open_write1;
    scanf("%d", &T);


    FOR(t, 1, T)
    {
        scanf("%d%d", &N, &J);


        printf("Case #%d:\n", t);

        REP(num, 1LL<<(N-1LL), 1LL<<N)
        {
            if(!(num&1))
                continue;

            if(is_jamcoin(num))
            {
                print_base_two(num);
                cout<<divisors;
                --J;
            }

            if(!J)
                break;
        }

    }

    return 0;
}


