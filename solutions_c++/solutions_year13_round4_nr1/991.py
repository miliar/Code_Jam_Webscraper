#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>

#ifdef DEBUG
int _msgIndent=0,_msgCnt=0;
struct _indent{
    inline _indent(){++_msgIndent;}
    inline ~_indent(){--_msgIndent;}
};
#define MSGINDENT _indent _INDENT
#define MSGHEAD cerr.width(4),cerr<<(_msgCnt++)<<string(4*_msgIndent,' ')\
                                <<'('<<__LINE__<<')'<<__FUNCTION__<<':'
#define MSGENDL endl(cerr)
#define MSG(x) MSGHEAD<<x,MSGENDL
#define MSGPUT(x) cerr<<x
#else
#define MSGINDENT
#define MSGHEAD
#define MSGENDL
#define MSGPUT(x)
#define MSG(x)
#endif

using namespace std;

template<typename T = int>
T scan()
{
    bool seg = 0;char ch;
    while (!isdigit(ch = getchar()))
        seg |= (ch == '-');
    T x = ch - '0';
    while (isdigit(ch = getchar()))
        x = x*10 + ch - '0';
    return seg?-x:x;
}

template<typename T>
void maximize(T& a, const T b)
{ if (b>a) a=b; }
template<typename T>
void minimize(T& a, const T b)
{ if (b<a) a=b; }

struct node
{
    int x;
    int64_t p;
    node(int _x, int _p):
        x(_x), p(_p){ }
    inline bool operator<(const node& a)const
    {
        return x < a.x || (x == a.x && p > a.p);
    }
};

int n;

inline int64_t calc_cost(int b, int e)
{
    return ((int64_t)e-b)*(2*n-e+b+1)/2;
}

int64_t work()
{
    vector<node> l, s;
    n = scan();
    int m = scan();
    int64_t tot = 0;
    while (m--)
    {
        int b = scan(), e = scan(), p = scan();
        l.emplace_back(b, p);
        l.emplace_back(e, -p);
        tot += calc_cost(b, e) * p;
    }
    MSG(tot);
    sort(l.begin(), l.end());
    int64_t opt = 0;
    for(auto i = l.begin(); i != l.end(); ++i)
    {
        MSG(i->x<<' '<<i->p);
        if (i->p > 0)
            s.push_back(*i);
        else
        {
            i->p = -i->p;
            while (i->p)
            {
                int64_t cost = calc_cost(s.back().x, i->x);
                if (s.back().p > i->p)
                    opt += cost * i->p, s.back().p -= i->p, i->p = 0;
                else
                    opt += cost * s.back().p, i->p -= s.back().p, s.pop_back();
            }
        }
        MSG(opt);
    }
    return tot - opt;
}

int main()
{
    int z = scan();
    for (int i = 1; i <= z; ++i)
    {
        cout<<"Case #"<<i<<": "<<work()<<endl;
    }
}
