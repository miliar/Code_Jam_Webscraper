#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

#define FOR(i,n) for (int i = 0 ; i< n;i++)
#define FORI(i,s,e) for (int i = s ; i<= e;i++)
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define RALL(x) x.rbegin(),x.rend()
#define SZ(x) x.size()
#define FZ(x) memset(x,0,sizeof(x))


using namespace std;

int dpx;
int dpo;
int dpt;

int dsx;
int dso;
int dst;

int lx[4];
int lo[4];
int lt[4];

int cx[4];
int co[4];
int ct[4];


int a[103][103];

int minl[103];
int minc[103];

bool v[103][103];
bool ok[103][103];
int ax[] = {0,0,-1,1};
int ay[] = {1,-1,0,0};

int m,n;
bool pali(int n)
{
    string s;
    while (n!=0)
    {
        s+=(n%10+'0');
        n/=10;
    }

    return (s == string ( s.rbegin(), s.rend() ));
}
int main()
{
    FILE* f = fopen("fair.in","r");
    FILE* fout = fopen("fair.out","w");
    int n,t;
    fscanf(f,"%d\n",&t);

    FOR(i,t)
    {

        int a,b;
        fscanf(f,"%d %d\n",&a,&b);
        fprintf(fout,"Case #%d: ",i+1);
        int palin=0;
        FORI(k,a,b)
        {
            if (pali(k))
            {
                int sq = (int)sqrt(k);
                if (sq*sq==k&&pali(sq))
                {
                    palin++;
                    continue;
                }
            }

        }

        fprintf(fout,"%d\n",palin);
    }
    fclose(fout);
}
