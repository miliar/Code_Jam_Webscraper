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
   int n, res;
   vector<string> v;
   
   void readInput() { // should read input; will run sequentially
      cin >> n;
      FOR(i,n) {
         string s;
         cin >> s;
         v.pb(s);
      }
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      res = -1;
      vector<vector<char> > W0;
      vector<vi> W1;
      FOREACH(it,v) {
         vector<char> w0;
         vi w1;
         FOR(i,SZ(*it)) {
            if (i == 0 || (*it)[i] != (*it)[i-1]) {
               w0.pb((*it)[i]);
               w1.pb(0);
            }
            w1.back()++;
         }
         W0.pb(w0);
         W1.pb(w1);
      }
      FOREACH(it,W0) if (*it != W0[0]) return;
      int k = SZ(W0[0]);
      res = 0;
      FOR(i,k) {
         vi lens;
         FOREACH(it,W1) lens.pb((*it)[i]);
         //DBG(lens)
         int mini = INF;
         REP(x,0,100) {
            int s = 0;
            FOREACH(it,lens) s += abs(*it - x);
            REMIN(mini, s);
         }
         res += mini;
      }
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      if (res == -1) cout << "Fegla Won";
      else cout << res;
   }
};

Instance *instances;
sem_t coreSemaphore;
pthread_mutex_t cerr_lock = PTHREAD_MUTEX_INITIALIZER;
int tests, finishedTests = 0;

void* runner (void* input) {
   int testno = *reinterpret_cast<int*>(input);
   sem_wait(&coreSemaphore);
   instances[testno].compute();
   pthread_mutex_lock(&cerr_lock);
   cerr << "test " << testno+1 << " is finished (" << ++finishedTests << "/" << tests << ")" << endl;
   pthread_mutex_unlock(&cerr_lock);
   pthread_mutex_unlock(&instances[testno].finished);
   sem_post(&coreSemaphore);
   return 0;
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
         cerr << "test " << i+1 << " is finished (" << ++finishedTests << "/" << tests << ")" << endl;
         delete instances;
      }
   }
}
