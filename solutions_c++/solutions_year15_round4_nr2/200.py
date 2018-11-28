// tested by Hightail: https://github.com/dj3500/hightail
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <cassert>
using namespace std;
#define pb push_back
#define INF 1001001001
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)((x).size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define DBG(vari) cerr<<"["<<__LINE__<<"] "<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (__typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

// max cx przy Ax <= b, x >= 0 (!), zwraca x (nieogr lub sprzeczny => x pusty)
const double EPS = 10e-12;
typedef long double T;
typedef vector<T> VT;
namespace Simplex{
  vector<VT> A;
  VT b,c,res;
  vi kt,N;
  int m;
  inline void pivot(int k,int l,int e){
      int x=kt[l]; T p=A[l][e];
      FOR(i,k) A[l][i]/=p; b[l]/=p; N[e]=0;
      FOR(i,m) if (i!=l) b[i]-=A[i][e]*b[l],A[i][x]=A[i][e]*-A[l][x];
      FOR(j,k) if (N[j]){
        c[j]-=c[e]*A[l][j];
        FOR(i,m) if (i!=l) A[i][j]-=A[i][e]*A[l][j];
      }
      kt[l]=e; N[x]=1; c[x]=c[e]*-A[l][x];
  }
  VT doit(int k){
    VT res; T best;
    while (1){
      int e=-1,l=-1; FOR(i,k) if (N[i] && c[i]>EPS) {e=i; break;}
      if (e==-1) break;
      FOR(i,m) if (A[i][e]>EPS && (l==-1 || best>b[i]/A[i][e]))
        best=b[ l=i ]/A[i][e];
      if (l==-1)
		return VT();
      pivot(k,l,e);
    }
    res.resize(k,0); FOR(i,m) res[kt[i]]=b[i];
    return res;
  }
  VT simplex (const vector<VT> &AA, const VT &bb, const VT &cc){
    int n=AA[0].size(),k;
    m=AA.size(); k=n+m+1; kt.resize(m); b=bb; c=cc; c.resize(n+m);
    A=AA; FOR(i,m){ A[i].resize(k); A[i][n+i]=1; A[i][k-1]=-1; kt[i]=n+i;}
    N=vi(k,1); FOR(i,m) N[kt[i]]=0;
    int pos=min_element(ALL(b))-b.begin();
    if (b[pos]<-EPS){
      c=VT(k,0); c[k-1]=-1; pivot(k,pos,k-1); res=doit(k);
      if (res[k-1]>EPS) return VT();
      FOR(i,m) if (kt[i]==k-1)
          FOR(j,k-1) if (N[j] && (A[i][j]<-EPS || EPS<A[i][j])){
            pivot(k,i,j); break;
          }
      c=cc; c.resize(k,0); FOR(i,m) FOR(j,k) if (N[j]) c[j]-=c[kt[i]]*A[i][j];
    }
    res=doit(k-1); if (!res.empty()) res.resize(n);
    return res;
  }
};


template <class NameType>
struct LP {
   int n;
   map<NameType,pair<bool,int> > ass; // name -> <isNonneg, id>
   LP () : n(0) {}

   void addVar (NameType name, bool isNonneg) {
      ass[name] = mp(isNonneg, n);
      n += (isNonneg ? 1 : 2);
   }

   VT makeConstraintVector (const map<NameType,T> &constraint) {
      VT v(n, 0.0);
      FOREACH(it,constraint) {
         int id = ass[it->fi].se;
         bool nonneg = ass[it->fi].fi;
         v[id] = it->se;
         if (!nonneg) v[id+1] = -it->se;
      }
      return v;
   }

   // types of constraints:
   #define LEQ 1
   #define GEQ 2
   #define EQ 3

   vector<VT> AA;
   VT bb;
   void addConstraint (const map<NameType,T> &constraint, int type, T val) {
      if (type == EQ) {
         addConstraint(constraint, LEQ, val);
         addConstraint(constraint, GEQ, val);
      } else {
         VT v = makeConstraintVector(constraint);
         if (type == GEQ) {
            FOR(i,n) v[i] = -v[i];
            val = -val;
         }
         AA.pb(v);
         bb.pb(val);
      }
   }

   #define MINIMIZE 1
   #define MAXIMIZE 0

   pair<map<NameType,T>, T> solve (const map<NameType,T> &weight, bool minimize) {
      VT cc = makeConstraintVector(weight);
      if (minimize) {
         FOR(i,n) cc[i] = -cc[i];
      }
      VT x = Simplex::simplex(AA,bb,cc);
      if (x.empty()) throw 0;
      map<NameType,T> res;
      FOREACH(it,ass) {
         int id = it->se.se;
         bool nonneg = it->se.fi;
         res[it->fi] = (nonneg ? x[id] : x[id] - x[id+1]);
      }
      T value = 0.0;
      FOR(i,n) value += cc[i] * x[i];
      return mp(res, value * (minimize ? -1 : 1));
   }
};

const int N = 105;
T R[N], C[N];

int main () {
    wez(te)
    FORI(testno,te) {
        printf("Case #%d: ", testno);
        wez(n)
        T V, X;
        cin >> V >> X;
        FOR(i,n) cin >> R[i] >> C[i];
        if (testno == 30) {
            DBG(mp(V,X))
            DBG(n)
            vector<pair<T,T>> v;
            FOR(i,n) v.pb(mp(R[i], C[i]));
            DBG(v)
        }
        T maxTemp = C[0], minTemp = C[0];
        FOR(i,n) {
            REMAX(maxTemp, C[i]);
            REMIN(minTemp, C[i]);
        }
        if (maxTemp + EPS < X || X + EPS < minTemp) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        LP<int> lp;
        REP(i,0,n) lp.addVar(i, true);
        FOR(i,n) lp.addConstraint({{i,1}, {n,-1}}, LEQ, 0);
        map<int,T> m1, m2;
        FOR(i,n) m1[i] = R[i];
        FOR(i,n) m2[i] = R[i] * C[i];
        lp.addConstraint(m1, EQ, V);
        lp.addConstraint(m2, EQ, V*X);
        try {
            pair<map<int,T>, T> res = lp.solve({{n,1}}, MINIMIZE);
            cout << setprecision(15) << fixed << res.se << "\n";
        } catch (int _exc) {
            cout << "IMPOSSIBLE\n";
            cerr << "Fail" << testno << "\n";
        }
    }
}
