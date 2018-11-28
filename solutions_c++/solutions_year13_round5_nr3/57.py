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
  #define N 2006
   int dist[N];//, parent[N];

struct comp {
   inline bool operator () (int v, int w) const {
      if (dist[v] != dist[w]) return dist[v] < dist[w];
      return v < w;
   }
};

void dijkstra (int n, vector<pii> *adj, int src) {
   FORI(i,n) {
      dist[i] = INF;
      //parent[i] = -1;
   }
   dist[src] = 0;
   set<int,comp> q;
   q.insert(src);
   while (!q.empty()) {
      int v = *(q.begin());
      q.erase(q.begin());
      FOREACH(it,adj[v]) {
         int d = dist[v] + it->se, w = it->fi;
         if (d < dist[w]) {
            q.erase(w);
            dist[w] = d;
            q.insert(w);
            //parent[w] = v;
         }
      }
   }
}

   bool dobry[N];
vi bfs1 (int n, int source, vi *adj) {
   vi odl(n+1,-1);
   deque<int> q;
   if (!dobry[source]) return odl;
   q.pb(source);
   odl[source] = 0;
   while (!q.empty()) {
      int v = q.front();
      q.pop_front();
      FOREACH(it,adj[v]) if (odl[*it] == -1 && dobry[*it]) {
         odl[*it] = odl[v] + 1;
         q.pb(*it);
      }
   }
   return odl;
}

#define CORES 3


struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here

   vi adj[N], adjklasyczny[N];
   int n,m,plen,from[20006],to[20007],a[20007],b[20007], route[20007];

   int res;
   int dmin[N][N], dmax[N][N];
   vector<pii> adjmin[N], adjmax[N];
   
   
   void readInput() { // should read input; will run sequentially
      cin >> n >> m >> plen;
      FORI(i,m) cin >> from[i] >> to[i] >> a[i] >> b[i];
      FORI(i,m) {
         adj[from[i]].pb(i);
         adjklasyczny[from[i]].pb(to[i]);
      }
      FORI(i,plen) cin >> route[i];
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      res = 0;
      
      FORI(i,n) {
         FOREACH(it,adj[i]) {
            adjmin[i].pb(mp(to[*it], a[*it]));
            adjmax[i].pb(mp(to[*it], b[*it]));
         }
      }
      
      FORI(i,n) {
         dijkstra(n,adjmin,i);
         FORI(j,n) dmin[i][j] = dist[j];
         dijkstra(n,adjmax,i);
         FORI(j,n) dmax[i][j] = dist[j];
      }
      
      /*DBG("dmin")
      FORI(i,n) {
         DBG(vi(dmax[i]+1, dmax[i] + n+1))
      }*/
      
      vi boczne;
      int aeeee = 0;
      FORI(i,plen) {
         int e = route[i];
         aeeee += a[e];
         int v = from[e];
         int ep = to[e];
         FOREACH(it,adj[v]) if (*it != e) {
            boczne.pb(*it);
         }
         
         FOREACH(it,boczne) {
            int f = *it;
            int fp = to[f];
            //DBG(mp(e,f));
            //DBG(mp(ep,fp));
            FORI(w,n) dobry[w] = (aeeee + dmin[ep][w] <= b[f] + dmax[fp][w] || b[f] + dmax[fp][w] >= INF);
            //DBG(vector<bool>(dobry+1,dobry+n+1))
            // czy da sie dojsc v -> ep -> ... -> 2 idac po dobrych wierzcholkach?
            vi odl = bfs1(n, ep, adjklasyczny);
            if (odl[2] != -1) {
               // da sie dojsc
            } else {
               // droga bez sensu
               res = e;
               return;
            }
         }
      }
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      if (res == 0) cout << "Looks Good To Me";
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
