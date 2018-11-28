

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>
#include <bitset>


using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double, int> pdi;
typedef vector<int> vi;

typedef pair<int, string> pis;

struct Tr
{
    map<char, Tr*> next;
} rt, *prt = &rt;

int nodeCnt(vector<string> &arr)
{
    vector<Tr*> allocated;
    
    prt->next.clear();
    int res = 1;
    
    rep(i, 0, arr.size())
    {
        string &cur = arr[i];
        Tr *curNode = prt;
        rep(i, 0, cur.size())
        {
            char cs = cur[i];
            Tr *next = curNode->next[cs];
            if (next == nullptr)
            {
                next = new Tr;
                allocated.push_back(next);
                curNode->next[cs] = next;
                res++;
            }
            else;
            curNode = next;
        }
    }
    rep(i, 0, allocated.size())
    {
        delete allocated[i];
    }
    
    return res;
}

vector<string> sstr;
int m, n;

int res = 0, resCnt = 0;
void rec(int cp, vector<int> &place)
{
    if (cp == m)
    {
        int ccr = 0;
        rep(i, 0, n)
        {
            vector<string> cs;
            rep(j, 0, place.size())
            {
                if (place[j] == i)
                {
                    cs.push_back(sstr[j]);
                }
            }
            
            if (cs.size() == 0)
            return;
            int cr = nodeCnt(cs);
            ccr += cr;
        }
        if (ccr == ::res)
        ::resCnt++;
        else if (ccr > ::res)
        {
            ::res = ccr;
            ::resCnt = 1;
        }
        return;
    }
    
    rep(i, 0, n)
    {
        place.push_back(i);
        rec(cp+1, place);
        place.pop_back();
    }
}

char buf[200500];

void test(int tIndex)
{
    ::res = 0;
    ::resCnt = 0;
    printf("Case #%d: ", tIndex);
    scanf("%d%d", &m, &n);
    
    sstr.clear();
    rep(i, 0, m)
    {
        scanf(" %s", buf);
        sstr.push_back(buf);
    }
    
    vector<int> t;
    rec(0, t);
    
    printf("%d %d\n", res, resCnt);
}

void run()
{
	int T, t;
	scanf("%d", &T);
	for(t = 0; t < T; ++t)
	{
		test(t + 1);
	}
}

//#define prob "settling"


int main()
{
#ifdef LOCAL_DEBUG
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    time_t st=clock();
#else
#ifdef prob
    freopen(prob".in","r",stdin);
    freopen(prob".out","w",stdout);
#endif
#endif
    run();
#ifdef LOCAL_DEBUG
    fprintf(stderr,  "\n=============\n");
    fprintf(stderr, "Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif
    
    return 0;
}