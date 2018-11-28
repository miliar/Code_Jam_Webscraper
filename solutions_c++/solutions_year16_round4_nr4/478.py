#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(auto i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(auto i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

namespace Notebook
{
    const int MAX_N = 100000;
    struct Eje{ long f,m; long d(){return m-f;}};
    typedef map <int, Eje> MIE; MIE red[MAX_N];
    int N,F,D;
    void iniG(int n, int f, int d){N=n; F=f; D=d;fill(red, red+N, MIE());}
    void aEje(int d, int h, int m){
      red[d][h].m=m;red[d][h].f=red[h][d].m=red[h][d].f=0;
    }
    #define DIF_F(i,j) (red[i][j].d())
    #define DIF_FI(i)  (i->second.d())
    int v[MAX_N];
    long camAu(){
      fill(v, v+N,-1);
      queue<int> c;
      c.push(F);
      while(!(c.empty()) && v[D]==-1){
        int n = c.front(); c.pop();
        for(MIE::iterator i = red[n].begin(); i!=red[n].end(); i++){
          if(v[i->first]==-1 && DIF_FI(i) > 0){
            v[i->first]=n;
            c.push(i->first);
          }
        }
      }
      if(v[D]==-1)return 0;
      int n = D;
      long f = DIF_F(v[n], n);
      while(n!=F){
        f = min(f, DIF_F(v[n], n));
        n=v[n];
      }
      n = D;
      while(n!=F){
        red[n][v[n]].f=-(red[v[n]][n].f+=f);
        n=v[n];
      }
      return f;
    }
    long flujo(){long tot=0, c;do{tot+=(c=camAu());}while(c>0); return tot;}
};

int mat[8][8];

int N;

bool works()
{
    forn(worker, N)
    {
        Notebook::iniG(2*N+2, 2*N, 2*N+1);
        bool okForWorker[16];
        forn(i,16) okForWorker[i] = false;
        int total = 0;
        forn(j,N)
        if (mat[worker][j])
        {
            okForWorker[j] = true;
            total++;
        }
        forn(i,N)
        forn(j,N)
        if (mat[i][j] && i != worker && okForWorker[j])
            Notebook::aEje(j, N+i, 1);
        forn(i,N)
            Notebook::aEje(2*N, i, 1);
        forn(i,N)
            Notebook::aEje(N+i,2*N+1, 1);
        if (Notebook::flujo() >= total)
            return false;
    }
    return true;
}

int main()
{
    int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        cin >> N;
        forn(i,N)
        {
            string cad; cin >> cad;
            forn(j,N)
                mat[i][j] = cad[j] != '0';
        }
            
        vector<pair<int, int> > masks;
        forn(mask, 1<<(N*N))
        {
            int fmask = 0;
            forn(i,N)
            forn(j,N)
            if (mat[i][j])
            {
                int pos = N*i + j;
                fmask |= (1<<pos);
            }
            int cost = 0;
            forn(i,N*N)
            if (((1<<i) & mask) && !((1<<i) & fmask))
                cost++;
            masks.push_back({cost, (fmask | mask)});
        }
        sort(all(masks));
        int ret = 1000000000;
        for (auto par : masks)
        {
            int mask = par.second;
            forn(i,N)
            forn(j,N)
            {
                int pos = N*i + j;
                mat[i][j] = (mask & (1<<pos)) != 0;
            }
            if (works())
            {
                ret = par.first;
                break;
            }
        }
        cout << "Case #" << caso + 1 << ": " << ret <<  "\n";
	}
	return 0;
}
