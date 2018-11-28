#include <algorithm>
#include <functional>
#include <vector>
#include <iterator>
#include <array>
#include <cstdio>
#include <map>
namespace XX
{   
    template<template<typename> class Compare, typename T>
    inline T& UP(T& x, const T& y){if(Compare<T>()(y, x)) x = y; return x;}
    template<typename Compare, typename T>
    inline T& UP(T& x, const T& y, Compare comp){if(comp(y, x)) x = y; return x;}

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




namespace XX
{
    template<typename... Datas>
    class UnionFind
    {
        public:
            struct Node:public Datas...
            {
                int _parent = -1;
                int size(){return -_parent;}
                void operator+=(Node& other) { int dummy[] = {(Datas::operator+=(other), 0)...}; }
            };
            UnionFind(int size) :_data(size) {}

            Node& operator[](int idx)
            {
                return _data[(*this)(idx)];
            }

            int operator()(int n)
            {
                if(_data[n]._parent < 0)
                    return n;
                else
                    return _data[n]._parent = (*this)(_data[n]._parent);
            }

            bool operator()(int a, int b)
            {
                int pa = (*this)(a), pb = (*this)(b);
                if(pa == pb)
                    return false;
                else
                {
                    if(_data[pa]._parent == _data[pb]._parent)
                        _data[pa]._parent--;
                    else if(_data[pa]._parent > _data[pb]._parent)
                        std::swap(pa, pb);

                    _data[pa] += _data[pb];
                    _data[pb]._parent = pa;
                    return true;
                }
            }

        private:
            std::vector<Node> _data;
    };
}





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




//alias
//for union/find
template<typename... Datas>
using UF = XX::UnionFind<Datas...>; 
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

struct P
{
    int x, y, z, vx, vy, vz;
}ps[1234];

int sq(int n)
{
    return n * n;
}

void solve()
{
    int N, S;
    RD(N, S);

    for(int i = 0; i < N; i++)
        RD(ps[i].x, ps[i].y, ps[i].z, ps[i].vx, ps[i].vy, ps[i].vz);

    double l = 0, r = 10000;
    while(l + 1e-6 < r)
    {
        double m = (l + r) / 2;
        UF<> uf(N);
        for(int i = 0; i < N; i++)
            for(int j = i + 1; j < N; j++)
                if(sq(ps[i].x - ps[j].x) + sq(ps[i].y - ps[j].y) + sq(ps[i].z - ps[j].z) <= m * m)
                    uf(i, j);

        if(uf(0) == uf(1))
            r = m;
        else
            l = m;
    }

    WTL(l);
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



