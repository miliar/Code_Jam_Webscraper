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
#include <cassert>
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
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
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
   vector<ll> bets, mybets;
   double best;
   ll budget;
   
   void readInput() { // should read input; will run sequentially
      cin >> budget;
      int n;
      cin >> n;
      while (n--) {
         ll x;
         cin >> x;
         bets.pb(x);
      }
   }
   
   bool licz () {
      int s = 0;
      while (mybets[s+1] + bets[s+1] == mybets[s] + bets[s]) ++s;
      // [0..s] maja rowne bety
      ll eqBets = 0, ourBets = 0;
      REP(i,0,s) eqBets += mybets[i];
      REP(i,0,37) ourBets += mybets[i];
      if (ourBets > budget) return 0; // nie da sie
      REMAX(best, eqBets * (36.0/(s+1)) - ourBets);
      return 1;
   }
   
   bool probuj (int male, ll h) {
      mybets.assign(38,0);
      assert(bets[male] <= h);
      //if (bets[male] > h) return 0; // nie da sie
      REP(i,0,male) {
         mybets[i] = h - bets[i];
      }
      REP(i,male+1,37) mybets[i] = max(0LL, h+1 - bets[i]);
      return licz();
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      best = 0;
      while (SZ(bets) < 37) bets.pb(0);
      sort(ALL(bets));
      bets.pb(1LL * 1000 * 1000 * 1000 * 1000 * 1000);
      mybets.assign(38,0);
      
      REP(male,1,36) {
         // [0..male] to male
         /*REP(h,0,1000) {
            // wysokosc malego
            probuj(male,h);
         }*/
         REP(i,0,36) {
            ll h = bets[i];
            if (h-1 >= 0 && bets[male] <= h-1) probuj(male,h-1);
            if (h >= 0 && bets[male] <= h) probuj(male,h);
            if (h+1 >= 0 && bets[male] <= h+1) probuj(male,h+1);
         }
         
         ll from = bets[male], to = bets[37] - 1000000;
         while (from <= to) {
            ll m = (from + to) / 2;
            if (probuj(male,m)) {
               from = m+1;
            } else {
               to = m-1;
            }
         }
      }
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      cout << setprecision(9) << fixed << best;
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
         //cerr << "test " << i+1 << " is finished (" << ++finishedTests << "/" << tests << ")" << endl;
         delete instances;
      }
   }
}
