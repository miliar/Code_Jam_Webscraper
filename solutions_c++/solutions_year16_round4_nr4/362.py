#include <functional>
#include <vector>
#include <cstdio>
#include <map>
#include <iterator>
#include <array>
template<typename T> struct ScanfSpecifier{};
#define DEF(T,V) template<> struct ScanfSpecifier<T>{static constexpr const char* value = V;};
DEF(int,"%d")DEF(double,"%lf")DEF(float,"%f")DEF(char,"%c")DEF(const char*,"%s")DEF(unsigned long,"%lu")DEF(char*,"%s")DEF(unsigned int, "%u")
#ifdef _MSC_VER
DEF(long long int,"%I64d")
#else
DEF(long long int,"%lld")
#endif
#undef DEF
template<typename T> int RD(T& arg){return std::scanf(ScanfSpecifier<T>::value, &arg);}
template<int S> int RD(char (&arg)[S]){return std::scanf("%s", arg);}
template<> int RD<char*>(char*& arg){return std::scanf("%s", arg);}
template<> int RD<char>(char& arg){return std::scanf(" %c", &arg);}
template<typename T, typename... Args> int RD(T& arg1, Args&... args) {return RD(arg1) + RD(args...);}
template<typename T> T RD(){T ret; RD(ret); return ret;}
template<typename It> void RDV(It begin, It end) { while(begin != end) RD(*begin++); }
template<typename C> void RDV(C& c) {RDV(std::begin(c), std::end(c));}
template<typename... Args> void WT(Args... args) { int alc = 0; int dummy[] = {((alc++? std::printf(" "): 0), std::printf(ScanfSpecifier<Args>::value, args), 0)...}; }
template<typename... Args> void WTL(Args... args) { WT(args...); std::printf("\n"); }
template<typename It> void WTV(It begin, It end) { int alc = 0; while(begin != end) (alc++? std::printf(" "): 0), WT(*begin++); }
template<typename C> void WTV(const C& c) {WTV(std::begin(c), std::end(c));}
template<typename It> void WTVL(It begin, It end) { WTV(begin, end); std::printf("\n"); }
template<typename C> void WTVL(const C& c) {WTVL(std::begin(c), std::end(c));}



#ifdef _MSC_VER
#include <intrin.h>
inline int CLZ(int n){unsigned long ret; _BitScanForward(&ret, n); return ret;}
//inline int CLZ(long long int n){unsigned long ret; _BitScanForward64(&ret, n); return ret;}
inline int CTZ(int n){unsigned long ret; _BitScanReverse( &ret, n); return 31 - ret;} 
//inline int CTZ(long long int n){unsigned long ret; _BitScanReverse64( &ret, n); return 63 - ret;} 
inline int POPCNT(int n){return __popcnt(n);}
//inline int POPCNT(long long int n){return __popcnt64(n);}
#endif

#ifdef __GNUC__
inline int CLZ(int n){return __builtin_clz(n);}
inline int CLZLL(long long int n){return __builtin_clzll(n);}
inline int CTZ(int n){return __builtin_ctz(n);}
inline int CTZLL(long long int n){return __builtin_ctzll(n);}
inline int POPCNT(int n){return __builtin_popcount(n);}
inline int POPCNTLL(long long int n){return __builtin_popcountll(n);}
#endif





namespace XX
{   
    template<template<typename> class Compare, typename T>
    inline T& UP(T& x, const T& y){Compare<T>()(y, x) && (x = y); return x;}
    template<typename Compare, typename T>
    inline T& UP(T& x, const T& y, Compare comp){comp(y, x) && (x = y); return x;}

    template<typename T> inline T& GT(T& x, const T& y){return UP<std::greater>(x, y);}
    template<typename T> inline T& LS(T& x, const T& y){return UP<std::less>(x, y);}

    template<typename T>
    struct Mapper
    {
        int operator[](const T& v) { int& ret = table[v]; if(!ret) rtable[ret = table.size()] = v; return ret - 1; }
        template<typename... Args> int operator()(Args... args) { return (*this)[T(args...)]; }
        T rev(int idx){return rtable[idx + 1];}
        std::map<T, int> table;
        std::map<int, T> rtable;
    };

    template<typename T, int S>
    struct ReferenceArray
    {
        struct It {typename std::array<T*, S>::iterator it; T& operator*(){return **it;} void operator++(){it++;} bool operator!=(const It& other){return it != other.it;} };
        int size()const{return _ptr.size();}
        It begin()const{return {_ptr.begin()};}
        It end()const{return {_ptr.end()};}
        T& operator[](int idx)const{return *_ptr[idx];}
        mutable std::array<T*, S> _ptr;
    };
    template<typename T, typename... Args> 
    ReferenceArray<T, sizeof...(Args) + 1> MAKEV(T& arg1, Args&... args) {return {&arg1, &args...};}

    struct Range
    {   
        struct It {   int num, step; int operator*(){return num;} void operator++(){num += step;} bool operator!=(const It& other){return num != other.num;} };
        Range(int ee):b(0),e(ee){}
        Range(int bb, int ee):b(bb), e(ee){}
        It begin(){return {b, (b < e? 1: -1)};}
        It end(){return {e, 0};}
        int b, e;
    };

}




//alias
//bit operation => CLZ,CTZ,POPCNT
//alias
//RD[L],RDV[L],WT[L],WTV[L] for i/o
template<typename T> T& UMAX(T& x, T y){return XX::UP<std::greater>(x, y);}
template<typename T> T& UMIN(T& x, T y){return XX::UP<std::less>(x, y);}
using XX::UP; //(x,y) comp
using RG = XX::Range;
using XX::MAKEV;
using XX::Mapper;
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <functional>
using namespace std;



void solve()
{
    int N;
    RD(N);

    int can[32] = {};

    for(int i: RG(N))
        for(int j: RG(N))
        {
            char c;
            RD(c);
            if(c == '1')
                can[i] |= 1 << j;
        }
    
    int ans = N * N;
    int all = (1 << N) - 1;
    for(int z = (1 << (N * N)) - 1; z >= 0; z--)
    {
        int m[32] = {};
        for(int i = 0; i < N; i++)
            m[i] = can[i] | ((z >> (N * i)) & ((1 << N) - 1));

        int amt[32] = {};
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                if(m[i] & (1 << j))
                    amt[j] |= (1 << i);
        bool check = true;
        for(int i = 0; i < N; i++)
        {
            int alc = 0;
            int w = 0;
            for(int j = 0; j < N; j++)
                if(m[i] & (1 << j))
                    w |= amt[j], alc++;

            if(!alc || POPCNT(w) > alc)
                check = false;
        }

        if(check)
            UMIN(ans, POPCNT(z));
    }


    WTL(ans);

}

int main()
{
    int T;
    RD(T);
    for(int tn: XX::Range(1, T + 1))
    {
        printf("Case #%d: ", tn);
        solve();
    }
}



