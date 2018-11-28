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
#define IN(x,y) ((y).find((x))!=(y).end())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (__typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

// zastąpić tym maina
// wypełnić readInput(), compute() i writeOutput(); zmienne definiować wewnątrz klasy Instance
// PARALLEL - czy ma odpalić testy równolegle, CORES - liczba rdzeni
// uwaga - wersja równoległa może potrzebować dużo pamięci! (T razy więcej)
//         mozna sobie z tym poradzić tworząc duże tablice dynamicznie dopiero w compute()
//         (bo naraz wykonywane są co najwyżej CORES=3 kopie compute())
//         (pamiętać o delete [] na koniec compute)
// linkować z pthreads

#include <pthread.h>
#include <semaphore.h>
#define PARALLEL 0
#define CORES 3
struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here
   bool seen[1<<20];
   int smallest[1<<20];
   int n;
   vi start, contents[206];
   int opening[206];
   stringstream res;
   
   void readInput() { // should read input; will run sequentially
      int k;
      cin >> k >> n;
      while (k--) { start.pb(0); cin >> start.back(); }
      FOR(i,n) {
         int ki;
         cin >> opening[i] >> ki;
         while (ki--) { contents[i].pb(0); cin >> contents[i].back(); }
      }
   }
   
   void dfs (int v) {
      int keys[206];
      if (seen[v]++) return;
      smallest[v] = -1;
      if (v == (1<<n)-1) {
         smallest[v] = 0; // whatever
         return;
      }
      
      FOR(i,n) keys[opening[i]] = 0;
      FOREACH(x,start) {
         keys[*x]++;
      }
      FOR(i,n) if ((1<<i) & v) {
         keys[opening[i]]--;
         FOREACH(x,contents[i]) keys[*x]++;         
      }
      
      FOR(i,n) if (!( (1<<i) & v )) {
         if (keys[opening[i]] > 0) {
            dfs(v | (1<<i));
            if (smallest[v | (1<<i)] != -1) {
               if (smallest[v] == -1) smallest[v] = i;
            }
         }
      }
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      FOR(i,1<<n) seen[i] = 0;
      dfs(0);
      if (!seen[(1<<n)-1]) {
         res << "IMPOSSIBLE";
      } else {
         int mask = 0;
         while (mask != (1<<n)-1) {
            res << smallest[mask] + 1 << " ";
            mask = mask | (1 << smallest[mask]);
         }
      }
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      cout << res.str();
   }
};

Instance *instances;
sem_t coreSemaphore;
pthread_mutex_t cerr_lock = PTHREAD_MUTEX_INITIALIZER;

void* runner (void* input) {
   int testno = *reinterpret_cast<int*>(input);
   sem_wait(&coreSemaphore);
   instances[testno].compute();
   pthread_mutex_lock(&cerr_lock);
   cerr << "test " << testno+1 << " is finished" << endl;
   pthread_mutex_unlock(&cerr_lock);
   pthread_mutex_unlock(&instances[testno].finished);
   sem_post(&coreSemaphore);
   return 0;
}

int main () {
   freopen("d.in","r",stdin);
   freopen("d.out","w",stdout);
   string pierwszalinia;
   getline(cin,pierwszalinia);
   int tests = atoi(pierwszalinia.c_str());
   if (PARALLEL) {
      instances = new Instance[tests];
      // reading input
      FOR(i,tests) {
         instances[i].readInput();
      }
      
      // running computations in parallel
      sem_init(&coreSemaphore, 0, CORES);
      pthread_t irrelevant;
      FOR(i,tests) pthread_create(&irrelevant, NULL, runner, new int(i));
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
         cerr << "test " << i+1 << " is finished" << endl;
         delete instances;
      }
   }
}
