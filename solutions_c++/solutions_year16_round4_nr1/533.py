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
#define DBG(vari) cout<<"["<<__LINE__<<"] "<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (__typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

// wersja template'a, w ktorej jest naraz odpalonych
// co najwyzej CORES watkow
// (czasami na loanerach normalna wersja nie dziala dobrze
// bo jest w stanie odpalic np. tylko 5 watkow)





// zast¹piæ tym maina
// wype³niæ readInput(), compute() i writeOutput(); zmienne definiowaæ wewn¹trz klasy Instance
// PARALLEL - czy ma odpaliæ testy równolegle, CORES - liczba rdzeni
// uwaga - wersja równoleg³a mo¿e potrzebowaæ du¿o pamiêci! (T razy wiêcej)
//         mozna sobie z tym poradziæ tworz¹c du¿e tablice dynamicznie dopiero w compute()
//         (bo naraz wykonywane s¹ co najwy¿ej CORES=3 kopie compute())
//         (pamiêtaæ o delete [] na koniec compute)
// linkowaæ z pthreads

#include <pthread.h>
#include <semaphore.h>
#define PARALLEL 0
#define CORES 4
struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here
   int N, p, r, s;
   string res;
   
   void readInput() { // should read input; will run sequentially
      cin >> N >> r >> p >> s;
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
   }
   
   int f (int a, int b) {
      if (a + b == 1) return 0;
      if (a + b == 2) return 2;
      if (a + b == 3) return 1;
      return -23423;
   }
   
   vi go (int n, array<int,3> c, array<int,3> ord) {
      if (n == 0) {
         int nonz = c[0] ? 0 : c[1] ? 1 : 2;
         return {nonz};
      }
      int c01 = (c[0] + c[1] - c[2]) / 2;
      int c02 = c[0] - c01;
      int c12 = c[1] - c01;
      if (c01 < 0 || c02 < 0 || c12 < 0) throw 0;
      vi v = go(n-1, {c01, c12, c02}, {f(ord[0], ord[1]), f(ord[0], ord[2]), f(ord[1], ord[2])});
      vi ordinv(3);
      FOR(i,3) ordinv[ord[i]] = i;
      vi ans;
      for (int x : v) {
         vi two;
         if (x == 0) two = {0,1};
         if (x == 1) two = {1,2};
         if (x == 2) two = {0,2};
         if (ordinv[two[0]] > ordinv[two[1]]) swap(two[0], two[1]);
         for (int y : two) ans.pb(y);
      }
      return ans;
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      try {
         vi ans = go(N,{p,r,s},{0,1,2});
         for (int x : ans) {
            if (x == 0) cout << "P";
            if (x == 1) cout << "R";
            if (x == 2) cout << "S";
         }
      } catch (int _) {
         cout << "IMPOSSIBLE";
      }
   }
};

Instance *instances;
pthread_mutex_t cerr_lock = PTHREAD_MUTEX_INITIALIZER,
                nextToStartLock = PTHREAD_MUTEX_INITIALIZER;
int tests, finishedTests = 0, nextToStart = 0;
void* runner (void* input) {
   (void)(input); // get rid of warning
   while (1) {
      pthread_mutex_lock(&nextToStartLock);
      int testno = nextToStart++;
      pthread_mutex_unlock(&nextToStartLock);
      if (testno >= tests) return 0;

      //pthread_mutex_lock(&cerr_lock);
      //cerr << "test " << testno+1 << " is starting" << endl;
      //pthread_mutex_unlock(&cerr_lock);
      instances[testno].compute();
      pthread_mutex_lock(&cerr_lock);
      cerr << "test " << testno+1 << " is finished (" << ++finishedTests << "/" << tests << ")" << endl;
      pthread_mutex_unlock(&cerr_lock);
      pthread_mutex_unlock(&instances[testno].finished);
   }
}

int main () {
   string pierwszalinia;
   getline(cin,pierwszalinia);
   tests = atoi(pierwszalinia.c_str());
   if (PARALLEL) {
      instances = new Instance[tests];
      // reading input
      FOR(i,tests) {
         instances[i].readInput();
      }
      
      // running computations in parallel
      pthread_t irrelevant;
      FOR(i,CORES) {
         pthread_create(&irrelevant, NULL, runner, NULL);
      }
      FOR(i,tests) pthread_mutex_lock(&instances[i].finished); // wait until all are finished
      
      // writing output
      FOR(i,tests) {
         printf("Case #%d: ", i+1);
         instances[i].writeOutput();
         printf("\n");
      }
   } else {
      FOR(i,tests) {
         instances = new Instance;
         instances->readInput();
         instances->compute();
         printf("Case #%d: ", i+1);
         instances->writeOutput();
         printf("\n");
         cerr << "test " << i+1 << " is finished (" << ++finishedTests << "/" << tests << ")" << endl;
         delete instances;
      }
   }
}

